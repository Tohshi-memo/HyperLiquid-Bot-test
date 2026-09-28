# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T08:22:30.458037+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7872`

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

- `news_risk_high->unknown_24h` score `762.9072` n `139` status `ready` deltaP `1.2153` edge `63.5675` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.6373` n `139` status `ready` deltaP `18.0044` edge `0.6616` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.1773` n `139` status `ready` deltaP `22.5395` edge `0.1007` maxDD `-2.2287`
- `news_risk_high->crypto_major_24h` score `1.9455` n `139` status `ready` deltaP `13.4355` edge `0.516` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `1.7817` n `139` status `ready` deltaP `16.9077` edge `0.2914` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.2943` n `139` status `ready` deltaP `20.9236` edge `0.1293` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.2066` n `139` status `ready` deltaP `20.3013` edge `0.1507` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.5296` n `139` status `ready` deltaP `6.4188` edge `0.0924` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3368` n `139` status `ready` deltaP `6.3641` edge `0.2516` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.2431` n `139` status `ready` deltaP `5.7576` edge `0.048` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2275` n `139` status `ready` deltaP `6.2067` edge `0.0066` maxDD `-0.3214`
- `news_risk_high->metal_1h` score `-0.5472` n `139` status `ready` deltaP `1.1911` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.602` n `139` status `ready` deltaP `2.6946` edge `0.0172` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.7539` n `139` status `ready` deltaP `-1.0501` edge `0.0386` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1656` n `139` status `ready` deltaP `-8.8184` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2539` n `139` status `ready` deltaP `9.5247` edge `-0.0029` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5897` n `139` status `ready` deltaP `-11.2903` edge `0.0209` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9649` n `139` status `ready` deltaP `-10.8183` edge `-0.0123` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.3144` n `139` status `ready` deltaP `-7.8347` edge `0.027` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.7388` n `139` status `ready` deltaP `-10.56` edge `0.0007` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
