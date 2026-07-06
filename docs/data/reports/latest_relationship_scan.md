# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T12:07:29.067188+00:00`
- Price records: `672`
- Market context records: `5877`
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

- `news_risk_high->fx_4h` score `3.774` n `30` status `ready` deltaP `39.3902` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5249` n `232` status `ready` deltaP `8.8046` edge `0.1784` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9431` n `30` status `ready` deltaP `11.8363` edge `0.0887` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3089` n `30` status `ready` deltaP `5.6188` edge `0.0483` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.3613` n `236` status `ready` deltaP `4.9528` edge `0.0339` maxDD `-4.7624`
- `news_risk_high->metal_1h` score `-0.4188` n `30` status `ready` deltaP `1.6866` edge `-0.0283` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.4645` n `236` status `ready` deltaP `-1.4691` edge `-0.0009` maxDD `-0.5751`
- `market_context_high->metal_1h` score `-0.4772` n `236` status `ready` deltaP `3.438` edge `0.0044` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5251` n `236` status `ready` deltaP `-1.294` edge `-0.0016` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.6011` n `236` status `ready` deltaP `0.5709` edge `0.0039` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8158` n `236` status `ready` deltaP `3.5877` edge `0.0402` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.8869` n `236` status `ready` deltaP `2.7657` edge `0.0411` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1579` n `232` status `ready` deltaP `0.7464` edge `0.0153` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2331` n `30` status `ready` deltaP `-12.3952` edge `-0.024` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8228` n `30` status `ready` deltaP `-13.8821` edge `-0.0536` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8397` n `228` status `ready` deltaP `4.8794` edge `0.0134` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9767` n `232` status `ready` deltaP `-7.9374` edge `-0.0056` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.0749` n `232` status `ready` deltaP `9.8297` edge `0.1988` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2553` n `232` status `ready` deltaP `-0.4626` edge `-0.0135` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
