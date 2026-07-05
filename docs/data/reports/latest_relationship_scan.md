# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T11:37:30.734214+00:00`
- Price records: `672`
- Market context records: `5767`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `0.7109` n `228` status `ready` deltaP `15.3052` edge `0.497` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1592` n `285` status `ready` deltaP `7.4743` edge `0.1273` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3799` n `297` status `ready` deltaP `2.301` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4164` n `297` status `ready` deltaP `2.2254` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.622` n `297` status `ready` deltaP `3.2335` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.662` n `297` status `ready` deltaP `-0.2439` edge `0.0036` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7955` n `297` status `ready` deltaP `-2.3378` edge `-0.0059` maxDD `-3.7734`
- `market_context_high->fx_24h` score `-0.9086` n `228` status `ready` deltaP `14.9488` edge `0.0422` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9177` n `297` status `ready` deltaP `3.3484` edge `0.0333` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1136` n `297` status `ready` deltaP `1.6271` edge `0.0298` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.202` n `285` status `ready` deltaP `0.5894` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2572` n `285` status `ready` deltaP `2.6171` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5656` n `285` status `ready` deltaP `-6.6554` edge `-0.0486` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.7144` n `285` status `ready` deltaP `7.8198` edge `0.1542` maxDD `-25.2692`
- `market_context_high->index_24h` score `-2.9306` n `228` status `ready` deltaP `1.4619` edge `0.029` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7504` n `285` status `ready` deltaP `-2.562` edge `-0.0279` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.0573` n `285` status `ready` deltaP `5.913` edge `0.1047` maxDD `-27.2448`
- `market_context_high->crypto_major_24h` score `-5.1414` n `228` status `ready` deltaP `5.4368` edge `-0.019` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.2089` n `228` status `ready` deltaP `-8.4339` edge `-0.2435` maxDD `-28.2922`
- `market_context_high->commodity_24h` score `-11.1165` n `228` status `ready` deltaP `-13.0574` edge `-0.0795` maxDD `-41.7863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
