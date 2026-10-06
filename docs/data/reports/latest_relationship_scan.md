# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T09:22:30.328743+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.504` n `62` status `ready` deltaP `34.0087` edge `0.5856` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5703` n `62` status `ready` deltaP `20.1908` edge `0.464` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5506` n `62` status `ready` deltaP `10.7305` edge `0.2343` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2496` n `62` status `ready` deltaP `22.6804` edge `0.1196` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7592` n `117` status `ready` deltaP `13.8681` edge `0.2339` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5537` n `62` status `ready` deltaP `28.8012` edge `0.047` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9959` n `62` status `ready` deltaP `7.7796` edge `0.15` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8211` n `62` status `ready` deltaP `23.2278` edge `0.0119` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6898` n `62` status `ready` deltaP `16.8618` edge `0.0882` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2269` n `117` status `ready` deltaP `23.1616` edge `0.0235` maxDD `-0.3868`
- `news_risk_high->metal_4h` score `1.186` n `62` status `ready` deltaP `17.2846` edge `0.0784` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1849` n `117` status `ready` deltaP `16.2967` edge `0.0601` maxDD `-1.6002`
- `market_context_high->crypto_major_24h` score `0.9295` n `111` status `ready` deltaP `6.0045` edge `0.2836` maxDD `-14.6935`
- `market_context_high->fx_1h` score `0.8689` n `117` status `ready` deltaP `14.1896` edge `0.0062` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7346` n `117` status `ready` deltaP `11.9057` edge `0.0215` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.7315` n `62` status `ready` deltaP `2.5594` edge `0.0958` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7164` n `62` status `ready` deltaP `27.0092` edge `0.0684` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `0.4455` n `117` status `ready` deltaP `-0.7218` edge `0.2143` maxDD `-7.1222`
- `market_context_high->crypto_major_1h` score `-0.1198` n `117` status `ready` deltaP `7.3661` edge `0.0298` maxDD `-3.7778`
- `market_context_high->metal_24h` score `-0.1383` n `111` status `ready` deltaP `12.6405` edge `0.048` maxDD `-5.6663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
