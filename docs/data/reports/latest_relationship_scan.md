# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T13:22:32.057482+00:00`
- Price records: `672`
- Market context records: `5882`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10248`

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

- `news_risk_high->fx_4h` score `3.7764` n `30` status `ready` deltaP `39.3902` edge `0.0567` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4214` n `231` status `ready` deltaP `8.4106` edge `0.1724` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9657` n `30` status `ready` deltaP `11.8363` edge `0.0916` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3035` n `30` status `ready` deltaP `5.4691` edge `0.0486` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1913` n `235` status `ready` deltaP `5.2179` edge `0.0419` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3046` n `235` status `ready` deltaP `3.3966` edge `0.0054` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4079` n `30` status `ready` deltaP `1.8363` edge `-0.0279` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5039` n `235` status `ready` deltaP `-0.946` edge `-0.0012` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5079` n `235` status `ready` deltaP `3.8221` edge `0.0415` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.5599` n `235` status `ready` deltaP `1.1983` edge `0.005` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.5654` n `235` status `ready` deltaP `2.845` edge `0.042` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7338` n `235` status `ready` deltaP `-1.6945` edge `-0.001` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2619` n `30` status `ready` deltaP `-12.8443` edge `-0.0247` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.481` n `231` status `ready` deltaP `9.2645` edge `0.1856` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7984` n `30` status `ready` deltaP `-13.5772` edge `-0.0525` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.8331` n `231` status `ready` deltaP `0.1307` edge `0.0151` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.3127` n `30` status `ready` deltaP `-17.0122` edge `-0.0797` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.3437` n `231` status `ready` deltaP `-1.2829` edge `-0.0154` maxDD `-6.3754`
- `market_context_high->metal_4h` score `-2.4794` n `231` status `ready` deltaP `-2.0826` edge `-0.0295` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
