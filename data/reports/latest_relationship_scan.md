# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T11:52:23.133619+00:00`
- Price records: `672`
- Market context records: `2660`
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

- `market_context_high->unknown_24h` score `7.9747` n `118` status `ready` deltaP `17.1581` edge `0.583` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.8545` n `118` status `ready` deltaP `13.5593` edge `0.9135` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `4.8945` n `121` status `ready` deltaP `24.4759` edge `0.5126` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4017` n `121` status `ready` deltaP `13.9009` edge `0.3718` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5746` n `121` status `ready` deltaP `8.0679` edge `0.1824` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0949` n `133` status `ready` deltaP `9.7013` edge `0.1453` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6079` n `133` status `ready` deltaP `8.0512` edge `0.1164` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.3618` n `118` status `ready` deltaP `9.3191` edge `0.0661` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `0.1213` n `133` status `ready` deltaP `3.5467` edge `0.0444` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.0619` n `121` status `ready` deltaP `7.4985` edge `0.029` maxDD `-2.3986`
- `market_context_high->metal_4h` score `-0.2325` n `121` status `ready` deltaP `4.8982` edge `0.0296` maxDD `-2.5301`
- `market_context_high->index_1h` score `-0.3007` n `133` status `ready` deltaP `2.0463` edge `0.0107` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3142` n `133` status `ready` deltaP `4.132` edge `0.0075` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.3459` n `118` status `ready` deltaP `8.5747` edge `0.0012` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.5102` n `133` status `ready` deltaP `-0.0765` edge `0.0045` maxDD `-1.8854`
- `market_context_high->fx_1h` score `-0.6132` n `133` status `ready` deltaP `-1.4205` edge `0.003` maxDD `-0.2373`
- `market_context_high->fx_4h` score `-0.6971` n `121` status `ready` deltaP `-0.6778` edge `0.0118` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.0504` n `121` status `ready` deltaP `5.348` edge `0.0217` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2159` n `133` status `ready` deltaP `-4.3908` edge `0.0118` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.5227` n `118` status `ready` deltaP `6.4589` edge `-0.0722` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
