# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T08:52:47.376440+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.5088` n `62` status `ready` deltaP `34.0087` edge `0.586` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5511` n `62` status `ready` deltaP `20.1908` edge `0.4624` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.547` n `62` status `ready` deltaP `10.7305` edge `0.234` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.252` n `62` status `ready` deltaP `22.6804` edge `0.1198` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.764` n `117` status `ready` deltaP `13.8681` edge `0.2343` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5549` n `62` status `ready` deltaP `28.8012` edge `0.0471` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0115` n `62` status `ready` deltaP `7.9293` edge `0.1503` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8079` n `62` status `ready` deltaP `23.0781` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6838` n `62` status `ready` deltaP `16.8618` edge `0.0877` maxDD `-2.7837`
- `market_context_high->crypto_major_24h` score `1.5099` n `109` status `ready` deltaP `7.36` edge `0.3046` maxDD `-13.8942`
- `market_context_high->fx_4h` score `1.2525` n `117` status `ready` deltaP `23.4665` edge `0.0236` maxDD `-0.3868`
- `news_risk_high->metal_4h` score `1.1852` n `62` status `ready` deltaP `17.2846` edge `0.0783` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1825` n `117` status `ready` deltaP `16.2967` edge `0.0599` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.8809` n `117` status `ready` deltaP `14.3393` edge `0.0062` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7358` n `117` status `ready` deltaP `11.9057` edge `0.0216` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.7234` n `62` status `ready` deltaP `27.0092` edge `0.0693` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7064` n `62` status `ready` deltaP `2.4097` edge `0.0947` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.4263` n `117` status `ready` deltaP `-0.7218` edge `0.2127` maxDD `-7.1222`
- `market_context_high->metal_24h` score `-0.0213` n `109` status `ready` deltaP `13.3548` edge `0.0499` maxDD `-5.6663`
- `market_context_high->crypto_major_1h` score `-0.1042` n `117` status `ready` deltaP `7.5158` edge `0.0301` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
