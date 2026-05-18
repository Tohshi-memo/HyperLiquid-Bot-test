# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T14:07:22.911128+00:00`
- Price records: `672`
- Market context records: `1124`
- Flow alert records: `5140`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8723`

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

- `market_context_high->crypto_major_24h` score `18.9937` n `150` status `ready` deltaP `40.8542` edge `1.3568` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `8.7476` n `150` status `ready` deltaP `17.2152` edge `0.7376` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.8656` n `150` status `ready` deltaP `16.6944` edge `0.5105` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5475` n `150` status `ready` deltaP `-1.8889` edge `0.6416` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.4035` n `150` status `ready` deltaP `15.4791` edge `0.3779` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.586` n `168` status `ready` deltaP `9.2698` edge `0.1367` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.7092` n `168` status `ready` deltaP `6.7653` edge `0.0823` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.3959` n `168` status `ready` deltaP `6.8969` edge `0.0187` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2584` n `168` status `ready` deltaP `2.7302` edge `0.0411` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1496` n `168` status `ready` deltaP `8.4652` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0465` n `168` status `ready` deltaP `7.1322` edge `0.0329` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `-0.0603` n `168` status `ready` deltaP `7.5421` edge `0.1341` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.2826` n `168` status `ready` deltaP `2.9441` edge `0.0411` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.2844` n `168` status `ready` deltaP `6.651` edge `-0.007` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.6803` n `168` status `ready` deltaP `-1.4756` edge `0.0034` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7215` n `168` status `ready` deltaP `0.9364` edge `0.0009` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1196` n `168` status `ready` deltaP `4.9289` edge `0.1201` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.525` n `168` status `ready` deltaP `5.9378` edge `-0.0546` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.0871` n `168` status `ready` deltaP `-10.9683` edge `-0.0059` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.4624` n `150` status `ready` deltaP `-0.9098` edge `-0.0302` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
