# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T21:07:48.994317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.868` n `90` status `ready` deltaP `4.4445` edge `1.047` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9753` n `107` status `ready` deltaP `-2.402` edge `0.3635` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2905` n `107` status `ready` deltaP `14.7111` edge `0.0941` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9078` n `90` status `ready` deltaP `2.0139` edge `0.2198` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.87` n `90` status `ready` deltaP `24.7223` edge `0.0673` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4599` n `109` status `ready` deltaP `8.0591` edge `0.0262` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0667` n `109` status `ready` deltaP `6.4316` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1004` n `107` status `ready` deltaP `9.6934` edge `0.0085` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5012` n `109` status `ready` deltaP `-1.1111` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7219` n `107` status `ready` deltaP `3.6628` edge `0.0065` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8327` n `109` status `ready` deltaP `-4.7039` edge `-0.022` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4188` n `90` status `ready` deltaP `0.5555` edge `-0.0413` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5753` n `107` status `ready` deltaP `0.1097` edge `-0.0637` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.6321` n `109` status `ready` deltaP `-5.4373` edge `-0.0287` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.9547` n `109` status `ready` deltaP `0.2212` edge `-0.0985` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.2398` n `107` status `ready` deltaP `-14.2666` edge `-0.0666` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2729` n `90` status `ready` deltaP `-9.1667` edge `-0.0108` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4686` n `109` status `ready` deltaP `-11.8978` edge `-0.0724` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6952` n `109` status `ready` deltaP `1.2841` edge `-0.2718` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0566` n `90` status `ready` deltaP `10.6598` edge `-0.0261` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
