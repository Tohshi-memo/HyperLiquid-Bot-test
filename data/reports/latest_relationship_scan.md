# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T16:52:15.746346+00:00`
- Price records: `672`
- Market context records: `1757`
- Flow alert records: `6957`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1811` n `167` status `ready` deltaP `27.4087` edge `0.6583` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.0095` n `196` status `ready` deltaP `20.9713` edge `0.5376` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5084` n `196` status `ready` deltaP `22.7196` edge `0.4648` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.0934` n `167` status `ready` deltaP `18.6678` edge `0.3395` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.6021` n `167` status `ready` deltaP `14.7777` edge `0.7337` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1378` n `30` status `ready` deltaP `24.5709` edge `0.1294` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0927` n `196` status `ready` deltaP `16.7216` edge `0.2557` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `2.8947` n `196` status `ready` deltaP `12.7271` edge `0.3835` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.762` n `167` status `ready` deltaP `16.9671` edge `0.6069` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9218` n `196` status `ready` deltaP `12.0178` edge `0.1056` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7441` n `196` status `ready` deltaP `7.2712` edge `0.1159` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.4827` n `167` status `ready` deltaP `19.171` edge `0.771` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.1981` n `196` status `ready` deltaP `4.598` edge `0.0932` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0802` n `196` status `ready` deltaP `5.1204` edge `0.0534` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2047` n `196` status `ready` deltaP `3.767` edge `0.021` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2365` n `196` status `ready` deltaP `12.444` edge `0.1559` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5167` n `196` status `ready` deltaP `5.7956` edge `0.0287` maxDD `-6.3532`
- `news_risk_high->fx_1h` score `-0.5177` n `30` status `ready` deltaP `-5.8782` edge `-0.001` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.5736` n `30` status `ready` deltaP `15.8084` edge `-0.1317` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.5925` n `167` status `ready` deltaP `7.2344` edge `0.0073` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
