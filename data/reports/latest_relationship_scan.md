# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T12:07:17.506867+00:00`
- Price records: `672`
- Market context records: `974`
- Flow alert records: `2727`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.2505` n `150` status `ready` deltaP `35.0348` edge `1.0707` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.7122` n `150` status `ready` deltaP `11.6319` edge `0.7318` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2688` n `150` status `ready` deltaP `0.8264` edge `0.3607` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5891` n `150` status `ready` deltaP `-0.9444` edge `0.2549` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2176` n `210` status `ready` deltaP `3.5928` edge `0.0387` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.6033` n `210` status `ready` deltaP `1.0194` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.638` n `210` status `ready` deltaP `1.2746` edge `0.0152` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6496` n `198` status `ready` deltaP `2.125` edge `0.0022` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7186` n `210` status `ready` deltaP `3.071` edge `0.005` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1215` n `210` status `ready` deltaP `5.5232` edge `-0.0083` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1872` n `210` status `ready` deltaP `-1.2247` edge `-0.0136` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5103` n `198` status `ready` deltaP `0.8623` edge `0.0836` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6707` n `198` status `ready` deltaP `-1.3581` edge `0.0221` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8191` n `210` status `ready` deltaP `-1.199` edge `-0.0293` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0697` n `210` status `ready` deltaP `-0.0157` edge `-0.0284` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.5568` n `198` status `ready` deltaP `8.7199` edge `0.0994` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9205` n `198` status `ready` deltaP `-0.8115` edge `0.0788` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1242` n `198` status `ready` deltaP `8.2148` edge `-0.1273` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.2215` n `198` status `ready` deltaP `-1.3119` edge `0.0181` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.9904` n `150` status `ready` deltaP `5.1875` edge `0.0044` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
