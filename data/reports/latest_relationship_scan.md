# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T01:22:35.320247+00:00`
- Price records: `672`
- Market context records: `4992`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `22.9434` n `93` status `ready` deltaP `4.8661` edge `1.9296` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.21` n `87` status `ready` deltaP `18.0964` edge `0.5454` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.0669` n `74` status `ready` deltaP `29.1198` edge `0.3457` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1878` n `87` status `ready` deltaP `12.7366` edge `0.4868` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5461` n `87` status `ready` deltaP `20.8894` edge `0.0918` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8584` n `93` status `ready` deltaP `6.553` edge `0.1196` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.8309` n `93` status `ready` deltaP `7.7377` edge `0.075` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6362` n `87` status `ready` deltaP `5.3126` edge `0.1843` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4026` n `87` status `ready` deltaP `5.7576` edge `0.0434` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3485` n `93` status `ready` deltaP `6.1039` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1789` n `93` status `ready` deltaP `5.1107` edge `0.0911` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2593` n `74` status `ready` deltaP `5.7386` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3158` n `93` status `ready` deltaP `1.7079` edge `0.0141` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6066` n `93` status `ready` deltaP `1.6129` edge `0.0128` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8176` n `87` status `ready` deltaP `-1.032` edge `-0.0009` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.304` n `87` status `ready` deltaP `3.4343` edge `-0.0063` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7713` n `93` status `ready` deltaP `-12.1483` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-3.977` n `74` status `ready` deltaP `7.5309` edge `-0.0492` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.2543` n `74` status `ready` deltaP `-1.0417` edge `0.007` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
