# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T06:52:35.861507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.8547` n `92` status `ready` deltaP `4.4686` edge `0.9624` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2698` n `109` status `ready` deltaP `14.3615` edge `0.0947` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8586` n `92` status `ready` deltaP `2.7626` edge `0.2085` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5971` n `92` status `ready` deltaP `21.7542` edge `0.0521` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4814` n `109` status `ready` deltaP `8.3585` edge `0.026` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0243` n `109` status `ready` deltaP `5.3837` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1517` n `109` status `ready` deltaP `8.8569` edge `0.0075` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.565` n `109` status `ready` deltaP `-2.159` edge `-0.0086` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7619` n `109` status `ready` deltaP `-3.656` edge `-0.0199` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8311` n `109` status `ready` deltaP `2.3272` edge `0.0014` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2833` n `92` status `ready` deltaP `0.8077` edge `-0.0256` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.3931` n `92` status `ready` deltaP `-3.7968` edge `0.0662` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5217` n `109` status `ready` deltaP `-5.2876` edge `-0.0205` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8557` n `109` status `ready` deltaP `0.9697` edge `-0.0908` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.0933` n `109` status `ready` deltaP `1.5369` edge `-0.0457` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1438` n `109` status `ready` deltaP `-13.1252` edge `-0.0619` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-2.3069` n `109` status `ready` deltaP `1.7332` edge `-0.1591` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3522` n `109` status `ready` deltaP `-11.7481` edge `-0.0637` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3704` n `92` status `ready` deltaP `7.4124` edge `-0.034` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
