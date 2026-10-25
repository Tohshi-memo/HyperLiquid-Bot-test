# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T01:22:35.814938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7250`

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

- `market_context_high->unknown_4h` score `21.8145` n `95` status `ready` deltaP `0.8408` edge `1.8458` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.6212` n `53` status `ready` deltaP `21.6752` edge `0.0815` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.7476` n `95` status `ready` deltaP `10.1894` edge `0.0506` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2278` n `107` status `ready` deltaP `3.1171` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3314` n `107` status `ready` deltaP `-1.3977` edge `0.0023` maxDD `-0.1712`
- `market_context_high->metal_1h` score `-0.9232` n `107` status `ready` deltaP `1.1836` edge `-0.0054` maxDD `-1.6873`
- `market_context_high->index_1h` score `-0.9621` n `107` status `ready` deltaP `-1.2116` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-1.0384` n `95` status `ready` deltaP `-4.4977` edge `0.004` maxDD `-0.5107`
- `market_context_high->fx_24h` score `-1.4564` n `53` status `ready` deltaP `-3.7932` edge `-0.0022` maxDD `-1.5104`
- `market_context_high->crypto_major_1h` score `-1.5275` n `107` status `ready` deltaP `1.4746` edge `-0.0336` maxDD `-10.432`
- `market_context_high->crypto_major_24h` score `-1.8743` n `53` status `ready` deltaP `1.592` edge `-0.0215` maxDD `-13.6859`
- `market_context_high->equity_1h` score `-2.6057` n `107` status `ready` deltaP `-1.1347` edge `-0.0936` maxDD `-12.6316`
- `market_context_high->metal_4h` score `-3.1801` n `95` status `ready` deltaP `-8.3023` edge `-0.0317` maxDD `-5.9033`
- `market_context_high->metal_24h` score `-3.2238` n `53` status `ready` deltaP `-10.4265` edge `0.0051` maxDD `-7.006`
- `market_context_high->crypto_alt_1h` score `-3.3685` n `107` status `ready` deltaP `-0.277` edge `-0.0572` maxDD `-14.3999`
- `market_context_high->index_4h` score `-4.7268` n `95` status `ready` deltaP `-21.6736` edge `-0.0519` maxDD `-5.1342`
- `market_context_high->crypto_alt_24h` score `-6.3562` n `53` status `ready` deltaP `4.5663` edge `-0.1976` maxDD `-45.1525`
- `market_context_high->index_24h` score `-7.5643` n `53` status `ready` deltaP `-37.3133` edge `-0.1788` maxDD `-6.5573`
- `market_context_high->unknown_1h` score `-8.0173` n `107` status `ready` deltaP `-0.1973` edge `-0.6179` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-12.7555` n `95` status `ready` deltaP `-21.8261` edge `-0.3174` maxDD `-41.3371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
