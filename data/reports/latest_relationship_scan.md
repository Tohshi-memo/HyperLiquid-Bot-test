# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T04:07:26.124119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7712`

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

- `market_context_high->unknown_4h` score `52.5009` n `95` status `ready` deltaP `0.8408` edge `4.403` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.8615` n `107` status `ready` deltaP `3.7271` edge `1.5125` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.1583` n `42` status `ready` deltaP `15.7986` edge `0.0821` maxDD `-3.6055`
- `market_context_high->crypto_alt_24h` score `0.8182` n `42` status `ready` deltaP `18.4028` edge `0.2887` maxDD `-21.5194`
- `market_context_high->fx_1h` score `-0.3291` n `107` status `ready` deltaP `-1.3977` edge `0.0023` maxDD `-0.1472`
- `market_context_high->commodity_1h` score `-0.357` n `107` status `ready` deltaP `1.5474` edge `0.01` maxDD `-1.0053`
- `market_context_high->crypto_major_24h` score `-0.3999` n `42` status `ready` deltaP `10.9871` edge `0.0719` maxDD `-11.0468`
- `market_context_high->index_1h` score `-0.5312` n `107` status `ready` deltaP `0.3582` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.5618` n `95` status `ready` deltaP `-2.6974` edge `0.0058` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.5742` n `95` status `ready` deltaP `0.2872` edge `0.0398` maxDD `-1.165`
- `market_context_high->fx_24h` score `-0.6135` n `42` status `ready` deltaP `3.125` edge `0.0028` maxDD `-0.9804`
- `market_context_high->metal_1h` score `-0.79` n `107` status `ready` deltaP `2.7534` edge `-0.005` maxDD `-1.6682`
- `market_context_high->crypto_major_1h` score `-1.0123` n `107` status `ready` deltaP `5.399` edge `-0.0077` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-2.3413` n `107` status `ready` deltaP `2.0049` edge `-0.0862` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.3544` n `107` status `ready` deltaP `2.0776` edge `-0.031` maxDD `-11.3243`
- `market_context_high->metal_4h` score `-2.355` n `95` status `ready` deltaP `0.6996` edge `-0.0271` maxDD `-5.5719`
- `market_context_high->metal_24h` score `-2.5538` n `42` status `ready` deltaP `-6.4732` edge `-0.0173` maxDD `-6.522`
- `market_context_high->index_4h` score `-3.772` n `95` status `ready` deltaP `-11.7715` edge `-0.0452` maxDD `-4.5862`
- `market_context_high->crypto_major_4h` score `-6.3583` n `95` status `ready` deltaP `-11.9239` edge `-0.2052` maxDD `-35.7712`
- `market_context_high->index_24h` score `-6.8905` n `42` status `ready` deltaP `-34.8958` edge `-0.194` maxDD `-5.8059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
