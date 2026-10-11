# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T23:52:26.698796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1445.3913` n `40` status `ready` deltaP `-22.5694` edge `120.6361` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `42.3287` n `104` status `ready` deltaP `-7.2232` edge `3.6336` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8056` n `40` status `ready` deltaP `27.6736` edge `0.5922` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.424` n `40` status `ready` deltaP `52.4306` edge `0.1858` maxDD `0.0`
- `market_context_high->fx_24h` score `2.9573` n `40` status `ready` deltaP `33.6458` edge `0.0351` maxDD `-0.0374`
- `market_context_high->unknown_1h` score `2.8031` n `116` status `ready` deltaP `-2.803` edge `0.2859` maxDD `-1.0231`
- `risk_on_high->crypto_alt_1h` score `2.3445` n `37` status `ready` deltaP `15.3302` edge `0.1487` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `2.3445` n `37` status `ready` deltaP `15.3302` edge `0.1487` maxDD `-2.4421`
- `market_context_high->crypto_major_24h` score `1.3516` n `40` status `ready` deltaP `-21.1111` edge `0.5682` maxDD `-17.8526`
- `risk_on_high->metal_1h` score `0.9661` n `37` status `ready` deltaP `12.7691` edge `0.0193` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.9661` n `37` status `ready` deltaP `12.7691` edge `0.0193` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `0.7213` n `37` status `ready` deltaP `9.4595` edge `0.0947` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.7213` n `37` status `ready` deltaP `9.4595` edge `0.0947` maxDD `-3.2233`
- `risk_on_high->commodity_1h` score `0.6834` n `37` status `ready` deltaP `17.8832` edge `-0.0081` maxDD `-0.8809`
- `risk_on_and_context->commodity_1h` score `0.6834` n `37` status `ready` deltaP `17.8832` edge `-0.0081` maxDD `-0.8809`
- `market_context_high->commodity_4h` score `0.416` n `104` status `ready` deltaP `11.5501` edge `0.011` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.2594` n `116` status `ready` deltaP `6.2668` edge `0.0949` maxDD `-4.9401`
- `risk_on_high->equity_1h` score `0.1271` n `37` status `ready` deltaP `0.6191` edge `0.031` maxDD `-0.296`
- `risk_on_and_context->equity_1h` score `0.1271` n `37` status `ready` deltaP `0.6191` edge `0.031` maxDD `-0.296`
- `risk_on_high->fx_1h` score `0.0972` n `37` status `ready` deltaP `7.2221` edge `-0.0003` maxDD `-0.164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
