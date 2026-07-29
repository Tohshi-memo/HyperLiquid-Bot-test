# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T02:52:25.258941+00:00`
- Price records: `672`
- Market context records: `8260`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7957.9334` n `43` status `ready` deltaP `39.0625` edge `662.9007` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1363` n `54` status `ready` deltaP `26.3832` edge `0.4785` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1937` n `54` status `ready` deltaP `22.4274` edge `0.1475` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7055` n `54` status `ready` deltaP `22.8771` edge `0.092` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2545` n `54` status `ready` deltaP `10.9361` edge `0.2855` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8866` n `54` status `ready` deltaP `15.0033` edge `0.1006` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7013` n `54` status `ready` deltaP `11.2054` edge `0.1068` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.352` n `54` status `ready` deltaP `16.6215` edge `0.2017` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1812` n `54` status `ready` deltaP `10.6538` edge `0.0742` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.531` n `54` status `ready` deltaP `7.5017` edge `0.0231` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.207` n `54` status `ready` deltaP `7.7456` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0616` n `54` status `ready` deltaP `3.4043` edge `0.0125` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4151` n `54` status `ready` deltaP `5.3748` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.16` n `54` status `ready` deltaP `-8.8102` edge `-0.0427` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0744` n `43` status `ready` deltaP `-18.6491` edge `-0.0436` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.5614` n `43` status `ready` deltaP `-19.2103` edge `-0.0839` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0901` n `54` status `ready` deltaP `-33.2487` edge `-0.2051` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6624` n `43` status `ready` deltaP `-24.3096` edge `-0.352` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-13.8279` n `43` status `ready` deltaP `-17.2238` edge `-0.4544` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-33.9532` n `43` status `ready` deltaP `-23.4415` edge `-1.1942` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
