# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T12:07:28.495926+00:00`
- Price records: `672`
- Market context records: `5661`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.3064` n `189` status `ready` deltaP `15.3439` edge `0.5978` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9008` n `239` status `ready` deltaP `11.2371` edge `0.2294` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.5008` n `239` status `ready` deltaP `7.7699` edge `0.1538` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.2749` n `189` status `ready` deltaP `17.6918` edge `0.0546` maxDD `-2.304`
- `market_context_high->crypto_alt_4h` score `0.1821` n `239` status `ready` deltaP `7.4683` edge `0.1503` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2541` n `251` status `ready` deltaP `2.0922` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4305` n `251` status `ready` deltaP `4.9682` edge `0.0317` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5161` n `251` status `ready` deltaP `0.2475` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5785` n `251` status `ready` deltaP `1.8364` edge `0.0357` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8295` n `251` status `ready` deltaP `2.8383` edge `0.0365` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8692` n `251` status `ready` deltaP `1.0974` edge `-0.0032` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9282` n `251` status `ready` deltaP `0.6435` edge `0.0052` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.245` n `239` status `ready` deltaP `2.5673` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-2.0028` n `239` status `ready` deltaP `-1.2795` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.354` n `189` status `ready` deltaP `8.8625` edge `0.0378` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0388` n `239` status `ready` deltaP `-14.4351` edge `-0.055` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7771` n `239` status `ready` deltaP `-1.9805` edge `-0.034` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7863` n `189` status `ready` deltaP `3.5797` edge `0.0313` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4404` n `189` status `ready` deltaP `-13.9964` edge `-0.2527` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.5949` n `189` status `ready` deltaP `-13.5417` edge `-0.0984` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
