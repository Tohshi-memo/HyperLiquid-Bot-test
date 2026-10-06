# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T10:07:31.975415+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.5234` n `62` status `ready` deltaP `34.1611` edge `0.5862` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6099` n `62` status `ready` deltaP `20.1908` edge `0.4673` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5422` n `62` status `ready` deltaP `10.7305` edge `0.2336` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2424` n `62` status `ready` deltaP `22.6804` edge `0.119` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7786` n `117` status `ready` deltaP `14.0205` edge `0.2345` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5561` n `62` status `ready` deltaP `28.8012` edge `0.0472` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9827` n `62` status `ready` deltaP `7.7796` edge `0.1489` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.833` n `62` status `ready` deltaP `23.3775` edge `0.0119` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7006` n `62` status `ready` deltaP `16.8618` edge `0.0891` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1933` n `117` status `ready` deltaP `16.2967` edge `0.0608` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1868` n `62` status `ready` deltaP `17.2846` edge `0.0785` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.1843` n `117` status `ready` deltaP `22.7043` edge `0.023` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.8306` n `117` status `ready` deltaP `13.7405` edge `0.006` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7358` n `117` status `ready` deltaP `11.9057` edge `0.0216` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.7279` n `62` status `ready` deltaP `2.5594` edge `0.0955` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.714` n `62` status `ready` deltaP `27.0092` edge `0.0681` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `0.4851` n `117` status `ready` deltaP `-0.7218` edge `0.2176` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.008` n `114` status `ready` deltaP `4.0604` edge `0.2507` maxDD `-16.1682`
- `news_risk_high->metal_1h` score `-0.1259` n `62` status `ready` deltaP `4.0564` edge `0.0043` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.133` n `117` status `ready` deltaP `7.3661` edge `0.0287` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
