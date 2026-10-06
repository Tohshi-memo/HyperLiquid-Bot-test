# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T10:22:28.252837+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.5306` n `62` status `ready` deltaP `34.1611` edge `0.5868` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6135` n `62` status `ready` deltaP `20.1908` edge `0.4676` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.535` n `62` status `ready` deltaP `10.7305` edge `0.233` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2388` n `62` status `ready` deltaP `22.6804` edge `0.1187` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7858` n `117` status `ready` deltaP `14.0205` edge `0.2351` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5561` n `62` status `ready` deltaP `28.8012` edge `0.0472` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9983` n `62` status `ready` deltaP `7.9293` edge `0.1492` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8199` n `62` status `ready` deltaP `23.2278` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6994` n `62` status `ready` deltaP `16.8618` edge `0.089` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1933` n `117` status `ready` deltaP `16.2967` edge `0.0608` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1876` n `62` status `ready` deltaP `17.2846` edge `0.0786` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.1709` n `117` status `ready` deltaP `22.5519` edge `0.0229` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.8174` n `117` status `ready` deltaP `13.5908` edge `0.0059` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7358` n `117` status `ready` deltaP `11.9057` edge `0.0216` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.7279` n `62` status `ready` deltaP `2.5594` edge `0.0955` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7156` n `62` status `ready` deltaP `27.0092` edge `0.0683` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `0.4887` n `117` status `ready` deltaP `-0.7218` edge `0.2179` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.1127` n `62` status `ready` deltaP `4.2061` edge `0.0044` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.1174` n `117` status `ready` deltaP `7.5158` edge `0.029` maxDD `-3.7778`
- `market_context_high->crypto_major_24h` score `-0.2459` n `115` status `ready` deltaP `3.4349` edge `0.2416` maxDD `-16.4662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
