# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T21:37:26.271875+00:00`
- Price records: `672`
- Market context records: `6020`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11124`

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

- `news_risk_high->fx_24h` score `7.7277` n `30` status `ready` deltaP `69.7917` edge `0.1787` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2455` n `30` status `ready` deltaP `43.9634` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.2971` n `30` status `ready` deltaP `28.6806` edge `0.1041` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.243` n `30` status `ready` deltaP `26.9261` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5507` n `208` status `ready` deltaP `8.6773` edge `0.1631` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.3188` n `182` status `ready` deltaP `28.892` edge `0.5216` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8356` n `30` status `ready` deltaP `10.3393` edge `0.0849` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2255` n `30` status `ready` deltaP `5.4691` edge `0.0386` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1405` n `30` status `ready` deltaP `9.2361` edge `0.0436` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.372` n `208` status `ready` deltaP `3.9728` edge `0.0057` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4032` n `30` status `ready` deltaP `1.5369` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.6058` n `182` status `ready` deltaP `4.8039` edge `0.0728` maxDD `-6.5994`
- `market_context_high->fx_1h` score `-0.6294` n `208` status `ready` deltaP `-0.7341` edge `-0.0016` maxDD `-0.6765`
- `market_context_high->commodity_1h` score `-0.6534` n `208` status `ready` deltaP `-1.379` edge `-0.0005` maxDD `-0.5804`
- `market_context_high->index_4h` score `-0.98` n `208` status `ready` deltaP `2.3452` edge `0.0176` maxDD `-2.3768`
- `market_context_high->metal_4h` score `-0.9913` n `208` status `ready` deltaP `4.6553` edge `0.0051` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-1.0043` n `208` status `ready` deltaP `0.6074` edge `0.0251` maxDD `-4.3608`
- `market_context_high->crypto_major_1h` score `-1.0253` n `208` status `ready` deltaP `3.256` edge `0.0236` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.0256` n `208` status `ready` deltaP `3.1293` edge `0.0229` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.0275` n `30` status `ready` deltaP `-9.2515` edge `-0.0186` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
