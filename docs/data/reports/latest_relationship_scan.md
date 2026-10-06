# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T10:52:32.020123+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8618`

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

- `market_context_high->unknown_24h` score `37.0544` n `115` status `ready` deltaP `10.7979` edge `3.0539` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.5498` n `62` status `ready` deltaP `34.1611` edge `0.5884` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6291` n `62` status `ready` deltaP `20.1908` edge `0.4689` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.517` n `62` status `ready` deltaP `10.7305` edge `0.2315` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2316` n `62` status `ready` deltaP `22.6804` edge `0.1181` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.805` n `117` status `ready` deltaP `14.0205` edge `0.2367` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5561` n `62` status `ready` deltaP `28.8012` edge `0.0472` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0043` n `62` status `ready` deltaP `7.9293` edge `0.1497` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.7947` n `62` status `ready` deltaP `22.9284` edge `0.0117` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7042` n `62` status `ready` deltaP `16.8618` edge `0.0894` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1921` n `117` status `ready` deltaP `16.2967` edge `0.0607` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1868` n `62` status `ready` deltaP `17.2846` edge `0.0785` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.1429` n `117` status `ready` deltaP `22.247` edge `0.0226` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.8054` n `117` status `ready` deltaP `13.4411` edge `0.0059` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7358` n `117` status `ready` deltaP `11.9057` edge `0.0216` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.7327` n `62` status `ready` deltaP `2.5594` edge `0.0959` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7265` n `62` status `ready` deltaP `27.0092` edge `0.0697` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `0.5043` n `117` status `ready` deltaP `-0.7218` edge `0.2192` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0983` n `62` status `ready` deltaP `4.3558` edge `0.0046` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.1114` n `117` status `ready` deltaP `7.5158` edge `0.0295` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
