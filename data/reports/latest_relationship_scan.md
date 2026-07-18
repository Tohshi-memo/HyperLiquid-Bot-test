# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T04:22:28.884273+00:00`
- Price records: `672`
- Market context records: `7102`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.3998` n `154` status `ready` deltaP `16.1031` edge `0.0139` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1393` n `154` status `ready` deltaP `0.0972` edge `0.0436` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1594` n `154` status `ready` deltaP `4.2947` edge `0.0032` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4436` n `154` status `ready` deltaP `0.4005` edge `0.0269` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5441` n `154` status `ready` deltaP `-0.2547` edge `-0.0061` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6041` n `154` status `ready` deltaP `3.2973` edge `0.0358` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8852` n `154` status `ready` deltaP `-4.7924` edge `-0.0199` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3881` n `154` status `ready` deltaP `-4.7137` edge `-0.043` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.561` n `154` status `ready` deltaP `-7.1993` edge `-0.0055` maxDD `-2.1273`
- `market_context_high->unknown_4h` score `-1.5758` n `154` status `ready` deltaP `-6.7093` edge `0.0029` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0987` n `154` status `ready` deltaP `2.4924` edge `-0.0434` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.4778` n `154` status `ready` deltaP `-0.5484` edge `-0.0441` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0361` n `154` status `ready` deltaP `3.8566` edge `0.0135` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1211` n `154` status `ready` deltaP `-0.39` edge `-0.019` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.2853` n `154` status `ready` deltaP `-7.4089` edge `-0.0935` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3706` n `154` status `ready` deltaP `-9.2262` edge `-0.02` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.4251` n `154` status `ready` deltaP `-8.9405` edge `-0.0111` maxDD `-5.511`
- `market_context_high->equity_4h` score `-8.6336` n `154` status `ready` deltaP `-0.7405` edge `-0.2149` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.0218` n `154` status `ready` deltaP `-24.9955` edge `-0.0705` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.9296` n `154` status `ready` deltaP `-25.3675` edge `-0.142` maxDD `-42.9744`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
