# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T10:22:33.348756+00:00`
- Price records: `672`
- Market context records: `5869`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7181` n `30` status `ready` deltaP `38.7805` edge `0.0559` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.013` n `30` status `ready` deltaP `24.3812` edge `0.0191` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1711` n `239` status `ready` deltaP `6.9625` edge `0.1612` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9353` n `30` status `ready` deltaP `12.1357` edge `0.0857` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2917` n `30` status `ready` deltaP `5.7685` edge `0.0451` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.4159` n `242` status `ready` deltaP `-0.605` edge `-0.0005` maxDD `-0.5699`
- `news_risk_high->metal_1h` score `-0.4204` n `30` status `ready` deltaP `1.6866` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4399` n `242` status `ready` deltaP `3.7252` edge `0.0056` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.4699` n `242` status `ready` deltaP `4.2349` edge `0.0333` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5548` n `242` status `ready` deltaP `-1.737` edge `-0.0024` maxDD `-1.905`
- `market_context_high->index_1h` score `-0.6476` n `242` status `ready` deltaP `-0.2932` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7755` n `242` status `ready` deltaP `3.7611` edge `0.0424` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.8729` n `242` status `ready` deltaP `2.8208` edge `0.0419` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2082` n `30` status `ready` deltaP `-11.9461` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2242` n `239` status `ready` deltaP `-0.1831` edge `0.013` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-1.8197` n `30` status `ready` deltaP `-13.8821` edge `-0.0532` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8335` n `228` status `ready` deltaP `4.8794` edge `0.0142` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9125` n `239` status `ready` deltaP `-6.868` edge `-0.0045` maxDD `-2.2593`
- `market_context_high->equity_24h` score `-2.1917` n `228` status `ready` deltaP `13.0574` edge `0.2382` maxDD `-31.6316`
- `news_risk_high->index_4h` score `-2.2652` n `30` status `ready` deltaP `-16.25` edge `-0.0787` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
