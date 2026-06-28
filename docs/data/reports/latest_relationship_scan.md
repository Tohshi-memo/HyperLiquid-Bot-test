# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T01:37:28.877162+00:00`
- Price records: `672`
- Market context records: `4993`
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

- `market_context_high->unknown_1h` score `22.5774` n `93` status `ready` deltaP `4.7164` edge `1.9001` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.21` n `87` status `ready` deltaP `18.0964` edge `0.5454` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.1216` n `74` status `ready` deltaP `29.2934` edge `0.3491` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1854` n `87` status `ready` deltaP `12.7366` edge `0.4866` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5557` n `87` status `ready` deltaP `20.8894` edge `0.0926` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8453` n `93` status `ready` deltaP `7.8874` edge `0.0752` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8441` n `93` status `ready` deltaP `6.4033` edge `0.1194` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.6481` n `87` status `ready` deltaP `5.4651` edge `0.1848` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4172` n `87` status `ready` deltaP `5.9101` edge `0.0436` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3604` n `93` status `ready` deltaP `6.2536` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1781` n `93` status `ready` deltaP `5.1107` edge `0.091` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2593` n `74` status `ready` deltaP `5.7386` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3259` n `93` status `ready` deltaP `1.5582` edge `0.0138` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5946` n `93` status `ready` deltaP `1.7626` edge `0.0128` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8176` n `87` status `ready` deltaP `-1.032` edge `-0.0009` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.31` n `87` status `ready` deltaP `3.4343` edge `-0.0068` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7725` n `93` status `ready` deltaP `-12.1483` edge `-0.0057` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-3.9954` n `74` status `ready` deltaP `7.3573` edge `-0.0504` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.2383` n `74` status `ready` deltaP `-0.8681` edge `0.0079` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
