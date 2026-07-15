# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T03:52:27.904195+00:00`
- Price records: `672`
- Market context records: `6778`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11714`

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

- `market_context_high->unknown_24h` score `0.9603` n `176` status `ready` deltaP `-0.5051` edge `0.5017` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0285` n `176` status `ready` deltaP `8.144` edge `0.1349` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0304` n `177` status `ready` deltaP `7.5738` edge `0.0316` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1658` n `177` status `ready` deltaP `5.1304` edge `0.0284` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3951` n `177` status `ready` deltaP `-0.4127` edge `0.0006` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6094` n `177` status `ready` deltaP `-0.1522` edge `-0.0088` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6286` n `177` status `ready` deltaP `-1.4801` edge `0.0007` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7464` n `177` status `ready` deltaP `-5.8307` edge `-0.0043` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.2184` n `177` status `ready` deltaP `2.7547` edge `-0.0172` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.253` n `176` status `ready` deltaP `6.1391` edge `-0.0136` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2628` n `176` status `ready` deltaP `6.7766` edge `-0.0007` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5295` n `176` status `ready` deltaP `-3.4507` edge `-0.0241` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5965` n `177` status `ready` deltaP `-6.0963` edge `-0.0023` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6598` n `176` status `ready` deltaP `-6.4718` edge `-0.0118` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.7717` n `176` status `ready` deltaP `2.8963` edge `-0.0432` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9243` n `176` status `ready` deltaP `1.1502` edge `-0.0424` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3673` n `176` status `ready` deltaP `-14.648` edge `0.0536` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2237` n `176` status `ready` deltaP `2.7023` edge `-0.1326` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3561` n `176` status `ready` deltaP `-8.3965` edge `-0.0034` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.915` n `176` status `ready` deltaP `-16.4142` edge `-0.185` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
