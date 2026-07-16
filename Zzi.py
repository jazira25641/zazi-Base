from web3 import Web3
d
w3 = Web3(Web3.HTTPProvider("https://ethereum-rpc.publicnode.com"))
token = Web3.to_checksum_address("0xYourTokenAddress")
wallet = Web3.to_checksum_address("0xYourWalletAddress")
abi = [{
 "constant":Fulse,
 "inputs":[{"name":"owner","type":"address"}],
 "name":"balanceOf",
 "outputs":["name":"","type":"uint256"],
 "type":"function"
}]
contract = w3.eth.contract(address=token, abi=abi)
balance = contract.functions.balanceOf(wallet).call()
print("Raw Balance:", balance)
print("Connected:", w3.is_connected())
print("Done")
[{done}]
 "type":"function"
 "name":"balanceOf",
token = Web3.to_checksum_address("0xYourTokenAddress")
abi = [{
 "constant":True,
 "inputs":[{"name":"owner","type":"address"}],
contract = w3.eth.contract(address=token, abi=abi)
abi = [{
"constant":True,
"inputs":[{"name":"owner","type":"address"}],
 "name":"balanceOf",
 "outputs":["name":"","type":"uint256"],
"type":"function"
}]
const params = {
amount: "1.00",
token: "USDC",
 from: [{ adapter: evmAdapter }, { adapter: solanaAdapter }],
to: {
    adapter: destinationAdapter,
chain: "Arc_Testnet",
   recipientAddress,
  },
}
const estimate = await kit.unifiedBalance.estimateSpend(params)
const feeSummary = {
 providerFee: estimate.fees.find((fee) => fee.type === "provider")?.amount ?? "0",
 gasFee: estimate.fees.find((fee) => fee.type === "gasFee")?.amount ?? "0",
forwarderFee: estimate.fees.find((fee) => fee.type === 
"forwarder")?.amount ?? "0",
}
console.log(feeSummary)
// ​​{
//   providerFee: "0",
//   gasFee: "0.0011",
//   forwarderFee: "0",
// }
kit.unifiedBalance.setCustomFeePolicy({
computeFee: (params) => {
const total = Number(params.amount)
return (total * 0.01).toFixed(6) // Example: 1% product fee
},
 resolveFeeRecipientAddress: (feePayoutChain) => {
 return feePayoutChain.type === "solana"
   ? process.env.SOLANA_FEE_RECIPIENT!
 : process.env.EVM_FEE_RECIPIENT!
  },
})
const estimate = await kit.unifiedBalance.estimateSpend({
amount: "100.00",
token: "USDC",
from: [{ adapter: evmAdapter }, { adapter: solanaAdapter }],
to: {
    adapter: destinationAdapter,
  chain: "Arc_Testnet",
    recipientAddress,
  },
})
[
{
    type: "provider",
    token: "USDC",
    amount: "0.004287",
    allocations: [
      { chain: "Sei_Testnet", amount: "0.001294" },
      { chain: "Avalanche_Fuji", amount: "0.000971" },
      { chain: "Base_Sepolia", amount: "0.000895" },
    ],
  },
  {
    type: "gasFee",
    token: "USDC",
    amount: "0.205586",
    allocations: [
      { chain: "Arc_Testnet", amount: "0.0011" },
      { chain: "Sei_Testnet", amount: "0.001231" },
      { chain: "Avalanche_Fuji", amount: "0.022098" },
  ],
  },
  {
    type: "kit",
    token: "USDC",
    amount: "1.000000",
    allocations: [{ chain: "Arc_Testnet", amount: "1.000000" }],
    recipientAddress: "<EVM_FEE_RECIPIENT>",
  },
]
const delegateConfig = {
  from: { adapter: ownerAdapter, chain: "Ethereum" },
  delegateAddress,
}
await kit.unifiedBalance.addDelegate(delegateConfig)
