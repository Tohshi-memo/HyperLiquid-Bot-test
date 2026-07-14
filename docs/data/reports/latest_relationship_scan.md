# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T11:07:25.807204+00:00`
- Price records: `672`
- Market context records: `6703`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.0219` n `182` status `ready` deltaP `1.0703` edge `0.4991` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.3` n `182` status `ready` deltaP `9.1926` edge `0.0497` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1131` n `182` status `ready` deltaP `6.2463` edge `0.0442` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.0782` n `182` status `ready` deltaP `9.0755` edge `0.1198` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3622` n `182` status `ready` deltaP `0.2451` edge `0.0006` maxDD `-0.5606`
- `market_context_high->unknown_1h` score `-0.4543` n `182` status `ready` deltaP `-6.4437` edge `0.0952` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.534` n `182` status `ready` deltaP `-0.051` edge `0.0033` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5823` n `182` status `ready` deltaP `-3.4991` edge `0.0012` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6667` n `182` status `ready` deltaP `-0.7452` edge `-0.0122` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9794` n `182` status `ready` deltaP `9.5568` edge `-0.0013` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9937` n `182` status `ready` deltaP `2.999` edge `-0.0001` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.286` n `182` status `ready` deltaP `7.0725` edge `-0.0005` maxDD `-2.5883`
- `market_context_high->crypto_major_4h` score `-1.6163` n `182` status `ready` deltaP `7.3556` edge `0.0752` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-1.8277` n `182` status `ready` deltaP `5.7391` edge `0.0676` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.8455` n `182` status `ready` deltaP `-5.9736` edge `-0.0473` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-2.3035` n `182` status `ready` deltaP `-3.6117` edge `0.0148` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.9572` n `182` status `ready` deltaP `-17.1318` edge `0.021` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5517` n `182` status `ready` deltaP `-9.0182` edge `-0.0015` maxDD `-6.7485`
- `market_context_high->equity_4h` score `-5.4744` n `182` status `ready` deltaP `6.2567` edge `-0.071` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0785` n `182` status `ready` deltaP `-6.643` edge `-0.0147` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
