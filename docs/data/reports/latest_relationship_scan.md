# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T02:07:26.702799+00:00`
- Price records: `672`
- Market context records: `4996`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10472`

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

- `market_context_high->unknown_1h` score `16.551` n `93` status `ready` deltaP `4.5667` edge `1.3989` maxDD `-1.674`
- `market_context_high->unknown_24h` score `6.2022` n `74` status `ready` deltaP `29.6406` edge `0.3535` maxDD `-1.4072`
- `market_context_high->crypto_major_4h` score `6.1846` n `87` status `ready` deltaP `17.944` edge `0.5443` maxDD `-7.8836`
- `market_context_high->crypto_alt_4h` score `5.1394` n `87` status `ready` deltaP `12.4317` edge `0.4848` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5907` n `87` status `ready` deltaP `21.0418` edge `0.0945` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8453` n `93` status `ready` deltaP `7.8874` edge `0.0752` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8057` n `93` status `ready` deltaP `6.1039` edge `0.1182` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.6702` n `87` status `ready` deltaP `5.7699` edge `0.1856` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.444` n `87` status `ready` deltaP `6.2149` edge `0.0438` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3604` n `93` status `ready` deltaP `6.2536` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1547` n `93` status `ready` deltaP `4.8113` edge `0.09` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2412` n `74` status `ready` deltaP `6.0858` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3275` n `93` status `ready` deltaP `1.5582` edge `0.0136` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5934` n `93` status `ready` deltaP `1.7626` edge `0.0129` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8176` n `87` status `ready` deltaP `-1.032` edge `-0.0009` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.3208` n `87` status `ready` deltaP `3.4343` edge `-0.0077` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7593` n `93` status `ready` deltaP `-11.9986` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.0345` n `74` status `ready` deltaP `7.0101` edge `-0.0531` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.2109` n `74` status `ready` deltaP `-0.5208` edge `0.0091` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
