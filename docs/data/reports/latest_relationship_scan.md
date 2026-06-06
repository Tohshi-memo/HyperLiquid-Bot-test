# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T21:52:18.958532+00:00`
- Price records: `672`
- Market context records: `3115`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->commodity_24h` score `14.6494` n `94` status `ready` deltaP `46.5019` edge `0.9536` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.4` n `94` status `ready` deltaP `11.4288` edge `2.3952` maxDD `-51.6089`
- `market_context_high->unknown_24h` score `13.1448` n `94` status `ready` deltaP `22.9942` edge `0.9909` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.4014` n `94` status `ready` deltaP `33.2152` edge `0.9008` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.7022` n `94` status `ready` deltaP `14.0181` edge `1.3326` maxDD `-45.9334`
- `market_context_high->commodity_4h` score `2.9906` n `120` status `ready` deltaP `17.9878` edge `0.1751` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0058` n `132` status `ready` deltaP `2.1412` edge `0.0275` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3841` n `132` status `ready` deltaP `5.4346` edge `0.0208` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5617` n `94` status `ready` deltaP `3.9376` edge `-0.0003` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7362` n `132` status `ready` deltaP `3.611` edge `0.0945` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0091` n `132` status `ready` deltaP `1.2158` edge `0.0111` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3439` n `120` status `ready` deltaP `-12.7235` edge `-0.0031` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4328` n `120` status `ready` deltaP `9.4817` edge `0.044` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.5857` n `132` status `ready` deltaP `-10.166` edge `-0.0055` maxDD `-0.7095`
- `market_context_high->crypto_major_1h` score `-2.0224` n `132` status `ready` deltaP `-0.0817` edge `0.0583` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-2.025` n `120` status `ready` deltaP `4.1362` edge `0.0054` maxDD `-13.8046`
- `market_context_high->metal_1h` score `-2.2449` n `132` status `ready` deltaP `-5.9563` edge `-0.008` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7712` n `132` status `ready` deltaP `2.926` edge `-0.0478` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9902` n `120` status `ready` deltaP `11.7479` edge `0.2146` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0703` n `120` status `ready` deltaP `5.9146` edge `-0.0307` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
