# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T09:07:26.071882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6595`

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

- `market_context_high->unknown_24h` score `1763.4218` n `134` status `ready` deltaP `-2.7908` edge `147.0134` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `341.2845` n `30` status `ready` deltaP `-0.459` edge `28.456` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.7841` n `134` status `ready` deltaP `4.0749` edge `2.8848` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0726` n `134` status `ready` deltaP `33.3541` edge `0.052` maxDD `-0.1315`
- `news_risk_high->index_1h` score `2.1095` n `30` status `ready` deltaP `27.1557` edge `0.0085` maxDD `-0.0996`
- `news_risk_high->crypto_alt_1h` score `1.681` n `30` status `ready` deltaP `11.3074` edge `0.1064` maxDD `-1.669`
- `market_context_high->equity_24h` score `1.6408` n `134` status `ready` deltaP `16.3117` edge `0.3037` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3322` n `134` status `ready` deltaP `10.1551` edge `0.0128` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2657` n `134` status `ready` deltaP `15.0688` edge `0.0232` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2001` n `134` status `ready` deltaP `13.3281` edge `0.0497` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.1106` n `134` status `ready` deltaP `4.3324` edge `0.0679` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0203` n `134` status `ready` deltaP `6.7164` edge `0.0563` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1049` n `134` status `ready` deltaP `3.5794` edge `-0.0015` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3152` n `134` status `ready` deltaP `1.7942` edge `0.0132` maxDD `-0.4475`
- `news_risk_high->equity_1h` score `-0.3911` n `30` status `ready` deltaP `4.6806` edge `-0.0221` maxDD `-2.4064`
- `market_context_high->equity_4h` score `-0.4622` n `134` status `ready` deltaP `0.8668` edge `0.0934` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5915` n `134` status `ready` deltaP `-1.6927` edge `-0.0047` maxDD `-0.4545`
- `news_risk_high->metal_1h` score `-0.7526` n `30` status `ready` deltaP `-4.7206` edge `-0.0113` maxDD `-0.9639`
- `market_context_high->crypto_alt_1h` score `-0.8173` n `134` status `ready` deltaP `3.1482` edge `0.0607` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9013` n `134` status `ready` deltaP `-2.8443` edge `-0.0003` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
