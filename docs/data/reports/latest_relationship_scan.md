# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T15:22:34.173657+00:00`
- Price records: `672`
- Market context records: `5156`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.2974` n `63` status `ready` deltaP `34.4494` edge `2.3141` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.3148` n `133` status `ready` deltaP `19.8835` edge `0.4959` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `4.9031` n `63` status `ready` deltaP `19.8909` edge `0.8347` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.9015` n `133` status `ready` deltaP `14.876` edge `0.4692` maxDD `-9.46`
- `market_context_high->unknown_1h` score `4.8281` n `144` status `ready` deltaP `10.0632` edge `0.3994` maxDD `-2.7986`
- `market_context_high->crypto_major_24h` score `4.6915` n `63` status `ready` deltaP `18.0803` edge `0.8471` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `3.947` n `133` status `ready` deltaP `13.5246` edge `0.468` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0189` n `63` status `ready` deltaP `20.2381` edge `0.1566` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9629` n `63` status `ready` deltaP `0.9424` edge `0.248` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.7323` n `144` status `ready` deltaP `7.5266` edge `0.1354` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7115` n `144` status `ready` deltaP `5.0773` edge `0.1216` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.6995` n `133` status `ready` deltaP `9.3985` edge `0.1595` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.0277` n `144` status `ready` deltaP `6.6575` edge `0.0557` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0767` n `144` status `ready` deltaP `4.886` edge `0.0149` maxDD `-1.918`
- `market_context_high->index_1h` score `-0.1186` n `144` status `ready` deltaP `3.5803` edge `0.0113` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.1832` n `144` status `ready` deltaP `3.1728` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.3979` n `133` status `ready` deltaP `4.6546` edge `0.0297` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.424` n `63` status `ready` deltaP `6.8701` edge `0.0084` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.5666` n `133` status `ready` deltaP `3.6368` edge `0.0065` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6326` n `144` status `ready` deltaP `0.0541` edge `-0.0006` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
