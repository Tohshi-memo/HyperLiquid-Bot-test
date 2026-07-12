# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T22:22:26.956946+00:00`
- Price records: `672`
- Market context records: `6546`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4135` n `144` status `ready` deltaP `11.8934` edge `0.7852` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7214` n `34` status `ready` deltaP `39.3024` edge `0.0527` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2697` n `34` status `ready` deltaP `28.0204` edge `0.0204` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0117` n `199` status `ready` deltaP `-5.7684` edge `0.2962` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3237` n `144` status `ready` deltaP `12.784` edge `0.2119` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.4851` n `191` status `ready` deltaP `12.2039` edge `0.0267` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.4823` n `34` status `ready` deltaP `4.3854` edge `0.0863` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2258` n `191` status `ready` deltaP `9.2086` edge `0.1128` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.2485` n `34` status `ready` deltaP `-2.6418` edge `0.0367` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2795` n `191` status `ready` deltaP `10.9716` edge `0.0609` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4498` n `199` status `ready` deltaP `-0.7854` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.4547` n `191` status `ready` deltaP `11.6939` edge `0.0928` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.512` n `199` status `ready` deltaP `0.7748` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5926` n `199` status `ready` deltaP `6.0783` edge `0.0148` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.6083` n `199` status `ready` deltaP `5.7894` edge `0.01` maxDD `-6.7936`
- `market_context_high->equity_1h` score `-0.7029` n `199` status `ready` deltaP `2.7744` edge `0.0024` maxDD `-4.2147`
- `market_context_high->index_1h` score `-0.7996` n `199` status `ready` deltaP `0.1978` edge `0.004` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.9247` n `34` status `ready` deltaP `-5.081` edge `-0.0223` maxDD `-1.6568`
- `market_context_high->metal_4h` score `-1.0231` n `191` status `ready` deltaP `0.8587` edge `0.0381` maxDD `-2.6662`
- `market_context_high->unknown_4h` score `-1.0926` n `191` status `ready` deltaP `-19.1825` edge `0.2774` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
