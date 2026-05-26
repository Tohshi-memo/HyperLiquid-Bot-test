# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T08:37:22.910435+00:00`
- Price records: `672`
- Market context records: `1929`
- Flow alert records: `7452`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.3755` n `208` status `ready` deltaP `23.159` edge `0.5747` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8782` n `208` status `ready` deltaP `28.213` edge `0.5097` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.5557` n `208` status `ready` deltaP `17.1904` edge `0.3841` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1582` n `208` status `ready` deltaP `13.5906` edge `0.1987` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.6828` n `220` status `ready` deltaP `8.1927` edge `0.1009` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6376` n `196` status `ready` deltaP `13.9916` edge `0.4919` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.4984` n `220` status `ready` deltaP `7.1557` edge `0.1052` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3378` n `196` status `ready` deltaP `12.2626` edge `0.189` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.1985` n `208` status `ready` deltaP `8.3607` edge `0.0697` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1766` n `196` status `ready` deltaP `4.2233` edge `0.1094` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1978` n `220` status `ready` deltaP `4.4992` edge `0.0329` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2441` n `196` status `ready` deltaP `10.1793` edge `0.0167` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6539` n `220` status `ready` deltaP `-3.1818` edge `0.0006` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6852` n `220` status `ready` deltaP `4.5509` edge `0.0154` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6876` n `220` status `ready` deltaP `-0.2286` edge `0.0074` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9167` n `208` status `ready` deltaP `-4.1862` edge `-0.0008` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-1.0798` n `208` status `ready` deltaP `9.3456` edge `0.1169` maxDD `-12.5349`
- `market_context_high->equity_24h` score `-1.2568` n `196` status `ready` deltaP `7.111` edge `0.3377` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.2901` n `220` status `ready` deltaP `1.5569` edge `-0.0227` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9745` n `220` status `ready` deltaP `1.3745` edge `-0.0065` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
