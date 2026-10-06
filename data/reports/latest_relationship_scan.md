# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T09:37:34.245870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8612`

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

- `news_risk_high->crypto_major_4h` score `9.5282` n `62` status `ready` deltaP `34.1611` edge `0.5866` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5943` n `62` status `ready` deltaP `20.1908` edge `0.466` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5506` n `62` status `ready` deltaP `10.7305` edge `0.2343` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2472` n `62` status `ready` deltaP `22.6804` edge `0.1194` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7834` n `117` status `ready` deltaP `14.0205` edge `0.2349` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5549` n `62` status `ready` deltaP `28.8012` edge `0.0471` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9935` n `62` status `ready` deltaP `7.7796` edge `0.1498` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8211` n `62` status `ready` deltaP `23.2278` edge `0.0119` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6946` n `62` status `ready` deltaP `16.8618` edge `0.0886` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2135` n `117` status `ready` deltaP `23.0092` edge `0.0234` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.1873` n `117` status `ready` deltaP `16.2967` edge `0.0603` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1868` n `62` status `ready` deltaP `17.2846` edge `0.0785` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.8557` n `117` status `ready` deltaP `14.0399` edge `0.0061` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7358` n `117` status `ready` deltaP `11.9057` edge `0.0216` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.7351` n `62` status `ready` deltaP `2.5594` edge `0.0961` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.714` n `62` status `ready` deltaP `27.0092` edge `0.0681` maxDD `-8.196`
- `market_context_high->crypto_major_24h` score `0.6181` n `112` status `ready` deltaP `5.3449` edge `0.2727` maxDD `-15.2129`
- `market_context_high->crypto_alt_4h` score `0.4695` n `117` status `ready` deltaP `-0.7218` edge `0.2163` maxDD `-7.1222`
- `market_context_high->crypto_major_1h` score `-0.1222` n `117` status `ready` deltaP `7.3661` edge `0.0296` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `-0.1522` n `62` status `ready` deltaP `3.757` edge `0.0041` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
