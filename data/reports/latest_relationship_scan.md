# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T18:22:30.341457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8651`

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

- `market_context_high->unknown_4h` score `80.7166` n `135` status `ready` deltaP `4.5472` edge `6.7113` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `2.3184` n `145` status `ready` deltaP `0.5142` edge `0.2387` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9855` n `135` status `ready` deltaP `27.1875` edge `0.053` maxDD `-2.17`
- `market_context_high->fx_4h` score `0.4383` n `135` status `ready` deltaP `12.8963` edge `0.0104` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.4155` n `145` status `ready` deltaP `10.0857` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0479` n `145` status `ready` deltaP `9.0646` edge `0.0081` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3368` n `135` status `ready` deltaP `6.8417` edge `0.0482` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.3812` n `145` status `ready` deltaP `1.1253` edge `0.0108` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.3834` n `145` status `ready` deltaP `7.1774` edge `0.0313` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.514` n `135` status `ready` deltaP `10.5208` edge `0.0212` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.6138` n `145` status `ready` deltaP `-1.1253` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8572` n `135` status `ready` deltaP `7.7089` edge `-0.0072` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.0002` n `135` status `ready` deltaP `15.5787` edge `0.0906` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4234` n `145` status `ready` deltaP `1.719` edge `-0.0027` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6962` n `135` status `ready` deltaP `8.0671` edge `0.1013` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.759` n `145` status `ready` deltaP `1.5052` edge `0.0008` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9766` n `135` status `ready` deltaP `-7.6897` edge `-0.0346` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7852` n `135` status `ready` deltaP `0.544` edge `-0.0032` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8657` n `135` status `ready` deltaP `3.0499` edge `-0.084` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5444` n `135` status `ready` deltaP `-0.5013` edge `-0.1841` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
