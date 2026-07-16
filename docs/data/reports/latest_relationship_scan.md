# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T17:57:28.944860+00:00`
- Price records: `672`
- Market context records: `6943`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11728`

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

- `market_context_high->fx_1h` score `-0.2384` n `236` status `ready` deltaP `2.4206` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5473` n `236` status `ready` deltaP `2.5145` edge `0.0204` maxDD `-4.2882`
- `market_context_high->index_1h` score `-0.724` n `236` status `ready` deltaP `-0.1954` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7327` n `236` status `ready` deltaP `-2.3622` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8504` n `226` status `ready` deltaP `13.1921` edge `0.0094` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.101` n `236` status `ready` deltaP `2.9636` edge `0.0142` maxDD `-6.7235`
- `market_context_high->commodity_1h` score `-1.2652` n `236` status `ready` deltaP `-2.7428` edge `-0.015` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.2764` n `219` status `ready` deltaP `-8.1107` edge `0.3233` maxDD `-16.9626`
- `market_context_high->index_4h` score `-1.6221` n `226` status `ready` deltaP `9.0762` edge `-0.0105` maxDD `-11.3047`
- `market_context_high->unknown_1h` score `-1.628` n `236` status `ready` deltaP `-2.3648` edge `-0.0298` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6281` n `226` status `ready` deltaP `-4.3277` edge `-0.0309` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.9324` n `236` status `ready` deltaP `2.4459` edge `-0.017` maxDD `-15.4311`
- `market_context_high->metal_4h` score `-1.9785` n `226` status `ready` deltaP `4.8403` edge `0.0124` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7781` n `226` status `ready` deltaP `1.5878` edge `-0.0084` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7855` n `226` status `ready` deltaP `-0.1039` edge `-0.0237` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0177` n `226` status `ready` deltaP `-7.6529` edge `0.0361` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.5323` n `219` status `ready` deltaP `-5.0006` edge `-0.0742` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.2903` n `219` status `ready` deltaP `-6.3445` edge `-0.0116` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4925` n `226` status `ready` deltaP `5.763` edge `-0.0763` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.03` n `219` status `ready` deltaP `-13.6472` edge `-0.1204` maxDD `-35.3718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
