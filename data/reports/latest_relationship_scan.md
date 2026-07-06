# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T14:22:31.858535+00:00`
- Price records: `672`
- Market context records: `5886`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.7497` n `30` status `ready` deltaP `39.0854` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0621` n `30` status `ready` deltaP `24.98` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1178` n `228` status `ready` deltaP `7.6915` edge `0.1519` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.94` n `30` status `ready` deltaP `11.5369` edge `0.0903` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2614` n `30` status `ready` deltaP `5.1697` edge `0.0452` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.138` n `231` status `ready` deltaP `5.2856` edge `0.0397` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3018` n `231` status `ready` deltaP `3.4652` edge `0.0053` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4359` n `30` status `ready` deltaP `1.3872` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.4783` n `231` status `ready` deltaP `4.0478` edge `0.0438` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.5192` n `231` status `ready` deltaP `-1.151` edge `-0.0018` maxDD `-1.9006`
- `market_context_high->crypto_alt_1h` score `-0.5548` n `231` status `ready` deltaP `3.0485` edge `0.042` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.5648` n `231` status `ready` deltaP `1.1186` edge `0.0049` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.7967` n `231` status `ready` deltaP `-2.4659` edge `-0.0011` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.272` n `30` status `ready` deltaP `-12.994` edge `-0.025` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.6606` n `228` status `ready` deltaP `8.9458` edge `0.1647` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7968` n `30` status `ready` deltaP `-13.5772` edge `-0.0523` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.9079` n `224` status `ready` deltaP `3.869` edge `0.0114` maxDD `-5.5435`
- `market_context_high->index_4h` score `-1.9311` n `228` status `ready` deltaP `-0.7194` edge `0.0126` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.2985` n `30` status `ready` deltaP `-16.8598` edge `-0.0789` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.4308` n `228` status `ready` deltaP `-2.086` edge `-0.0173` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
