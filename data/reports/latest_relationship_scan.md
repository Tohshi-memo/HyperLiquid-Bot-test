# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T11:37:35.568148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11644`

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

- `market_context_high->unknown_24h` score `280.4679` n `88` status `ready` deltaP `6.3778` edge `23.3439` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `102.043` n `88` status `ready` deltaP `7.525` edge `8.4982` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.7367` n `53` status `ready` deltaP `21.0486` edge `2.2417` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.411` n `88` status `ready` deltaP `14.9379` edge `1.2739` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.4451` n `53` status `ready` deltaP `36.8969` edge `1.4179` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2374` n `53` status `ready` deltaP `34.106` edge `0.8221` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.112` n `53` status `ready` deltaP `41.3495` edge `0.317` maxDD `0.0`
- `market_context_high->metal_24h` score `5.0313` n `88` status `ready` deltaP `35.0071` edge `0.2412` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.7834` n `88` status `ready` deltaP `34.9638` edge `0.8896` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.5732` n `53` status `ready` deltaP `43.8047` edge `0.1267` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9448` n `53` status `ready` deltaP `21.6579` edge `0.3331` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6202` n `53` status `ready` deltaP `18.0149` edge `0.2446` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5805` n `53` status `ready` deltaP `19.129` edge `0.2012` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `2.9068` n `53` status `ready` deltaP `25.7967` edge `0.0956` maxDD `-0.3611`
- `market_context_high->index_24h` score `2.716` n `88` status `ready` deltaP `16.8134` edge `0.1605` maxDD `-2.3671`
- `news_risk_high->index_4h` score `2.1754` n `53` status `ready` deltaP `20.7461` edge `0.0866` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1618` n `53` status `ready` deltaP `25.5903` edge `0.035` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1597` n `53` status `ready` deltaP `25.4314` edge `0.2712` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3185` n `53` status `ready` deltaP `17.3257` edge `0.0245` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7792` n `53` status `ready` deltaP `18.9413` edge `0.0788` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
