# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T12:22:23.717222+00:00`
- Price records: `672`
- Market context records: `2662`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `8.1952` n `116` status `ready` deltaP `14.308` edge `0.9369` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.1245` n `116` status `ready` deltaP `17.2294` edge `0.595` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.5802` n `121` status `ready` deltaP `23.1279` edge `0.4954` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.025` n `121` status `ready` deltaP `12.5529` edge `0.3494` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.2951` n `121` status `ready` deltaP `6.7199` edge `0.1681` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7945` n `133` status `ready` deltaP `8.4969` edge `0.1283` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.316` n `133` status `ready` deltaP `6.8468` edge `0.1001` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.2236` n `116` status `ready` deltaP `8.8662` edge `0.0576` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1267` n `121` status `ready` deltaP `7.4985` edge `0.0236` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.2199` n `133` status `ready` deltaP `2.3423` edge `0.024` maxDD `-1.9684`
- `market_context_high->fx_24h` score `-0.2658` n `116` status `ready` deltaP `9.4109` edge `0.0023` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.2784` n `133` status `ready` deltaP `4.132` edge `0.0121` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3151` n `133` status `ready` deltaP `2.0463` edge `0.0095` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.4687` n `121` status `ready` deltaP `3.5502` edge `0.0189` maxDD `-2.5301`
- `market_context_high->fx_1h` score `-0.5547` n `133` status `ready` deltaP `-0.8183` edge `0.0036` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5595` n `133` status `ready` deltaP `-0.6787` edge `0.0022` maxDD `-1.8854`
- `market_context_high->fx_4h` score `-0.636` n `121` status `ready` deltaP `-0.0037` edge `0.0124` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1073` n `121` status `ready` deltaP `4.6739` edge `0.0189` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2375` n `133` status `ready` deltaP `-4.3908` edge `0.01` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.6023` n `116` status `ready` deltaP `6.0644` edge `-0.0762` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
