# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T21:52:30.455086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11752`

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

- `market_context_high->unknown_4h` score `56.0087` n `88` status `ready` deltaP `7.525` edge `4.662` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2724` n `88` status `ready` deltaP `33.6489` edge `2.9555` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.6326` n `88` status `ready` deltaP `28.9457` edge `1.1668` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9352` n `88` status `ready` deltaP `30.1136` edge `0.3401` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.9934` n `88` status `ready` deltaP `24.2582` edge `0.0597` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3653` n `88` status `ready` deltaP `3.1369` edge `0.0005` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.3796` n `88` status `ready` deltaP `3.4976` edge `0.0127` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.516` n `88` status `ready` deltaP `4.9196` edge `-0.0012` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5319` n `88` status `ready` deltaP `3.2567` edge `0.0207` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0088` n `88` status `ready` deltaP `-7.8048` edge `0.0058` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0197` n `88` status `ready` deltaP `-0.5959` edge `0.0116` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2167` n `88` status `ready` deltaP `-12.4115` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5691` n `88` status `ready` deltaP `-7.5054` edge `0.0335` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.7286` n `88` status `ready` deltaP `3.9931` edge `-0.0107` maxDD `-3.4642`
- `market_context_high->crypto_alt_1h` score `-1.8079` n `88` status `ready` deltaP `1.2316` edge `-0.0421` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8156` n `88` status `ready` deltaP `-1.5798` edge `-0.0041` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-2.9468` n `88` status `ready` deltaP `-3.7629` edge `-0.0904` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.8595` n `88` status `ready` deltaP `2.5915` edge `-0.1244` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.421` n `88` status `ready` deltaP `5.7608` edge `0.5057` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.1345` n `88` status `ready` deltaP `4.8365` edge `-0.1983` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
