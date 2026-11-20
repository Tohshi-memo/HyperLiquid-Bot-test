# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T14:07:40.580132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2634`

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

- `market_context_high->unknown_1h` score `10536.5761` n `122` status `ready` deltaP `1.6983` edge `878.0565` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6987.8249` n `114` status `ready` deltaP `0.9093` edge `582.3411` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `6.327` n `105` status `ready` deltaP `28.7252` edge `1.2213` maxDD `-42.4648`
- `market_context_high->crypto_alt_24h` score `4.0087` n `105` status `ready` deltaP `15.3125` edge `1.0235` maxDD `-57.6556`
- `market_context_high->crypto_major_4h` score `1.069` n `114` status `ready` deltaP `4.1506` edge `0.3433` maxDD `-16.2179`
- `market_context_high->metal_4h` score `0.2889` n `114` status `ready` deltaP `16.3885` edge `0.0551` maxDD `-6.8892`
- `market_context_high->crypto_alt_4h` score `0.2852` n `114` status `ready` deltaP `5.2177` edge `0.2509` maxDD `-15.9296`
- `market_context_high->metal_1h` score `-0.1497` n `122` status `ready` deltaP `4.4984` edge `0.0173` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2891` n `122` status `ready` deltaP `3.0799` edge `0.0036` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.0895` n `122` status `ready` deltaP `3.0014` edge `0.0458` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2289` n `122` status `ready` deltaP `-6.8347` edge `-0.0009` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.4344` n `122` status `ready` deltaP `5.8383` edge `0.0277` maxDD `-11.559`
- `market_context_high->crypto_alt_1h` score `-1.8616` n `122` status `ready` deltaP `-2.7363` edge `0.0227` maxDD `-8.4343`
- `market_context_high->index_4h` score `-1.87` n `114` status `ready` deltaP `-1.9121` edge `-0.0083` maxDD `-4.7832`
- `market_context_high->commodity_1h` score `-1.9337` n `122` status `ready` deltaP `-5.1242` edge `-0.0138` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.1649` n `114` status `ready` deltaP `-11.2591` edge `-0.0009` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.3992` n `105` status `ready` deltaP `13.7301` edge `0.1027` maxDD `-41.5333`
- `market_context_high->fx_24h` score `-6.6122` n `105` status `ready` deltaP `-17.3115` edge `-0.0083` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.2066` n `114` status `ready` deltaP `-23.0049` edge `-0.0779` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.3412` n `114` status `ready` deltaP `-5.3862` edge `-0.0758` maxDD `-49.6711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
