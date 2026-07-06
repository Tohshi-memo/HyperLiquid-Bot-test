# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T11:52:30.654107+00:00`
- Price records: `672`
- Market context records: `5876`
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

- `news_risk_high->fx_4h` score `3.7728` n `30` status `ready` deltaP `39.3902` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4811` n `233` status `ready` deltaP `8.5124` edge `0.1767` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9267` n `30` status `ready` deltaP `11.8363` edge `0.0866` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.291` n `30` status `ready` deltaP `5.6188` edge `0.046` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.4042` n `237` status `ready` deltaP `4.8397` edge `0.0332` maxDD `-4.932`
- `news_risk_high->metal_1h` score `-0.411` n `30` status `ready` deltaP `1.8363` edge `-0.0283` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.4521` n `237` status `ready` deltaP `-1.2456` edge `-0.0008` maxDD `-0.5751`
- `market_context_high->metal_1h` score `-0.4851` n `237` status `ready` deltaP `3.3553` edge `0.0043` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5283` n `237` status `ready` deltaP `-1.341` edge `-0.0017` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.605` n `237` status `ready` deltaP `0.4971` edge `0.0039` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8668` n `237` status `ready` deltaP `3.3553` edge `0.0375` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9447` n `237` status `ready` deltaP `2.5386` edge `0.0378` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1708` n `233` status `ready` deltaP `0.4985` edge `0.0153` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2245` n `30` status `ready` deltaP `-12.2455` edge `-0.0239` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8205` n `30` status `ready` deltaP `-13.8821` edge `-0.0533` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8397` n `228` status `ready` deltaP `4.8794` edge `0.0134` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9631` n `233` status `ready` deltaP `-7.6913` edge `-0.0055` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.1568` n `233` status `ready` deltaP `9.5559` edge `0.1938` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2275` n `233` status `ready` deltaP `-0.2055` edge `-0.0129` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
