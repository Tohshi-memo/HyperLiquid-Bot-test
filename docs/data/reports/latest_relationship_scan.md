# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T12:52:31.358015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.1216` n `90` status `ready` deltaP `-5.8468` edge `3.103` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.5943` n `62` status `ready` deltaP `36.4477` edge `0.6602` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3896` n `62` status `ready` deltaP `24.0018` edge `0.5902` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.7964` n `62` status `ready` deltaP `27.4306` edge `0.1335` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2426` n `62` status `ready` deltaP `8.3053` edge `0.2248` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0399` n `62` status `ready` deltaP `33.6792` edge `0.055` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3772` n `62` status `ready` deltaP `9.576` edge `0.1698` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.2859` n `62` status `ready` deltaP `19.4532` edge `0.1206` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.0895` n `90` status `ready` deltaP `14.5122` edge `0.1738` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0223` n `62` status `ready` deltaP `25.4733` edge `0.0137` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.7254` n `90` status `ready` deltaP `6.3889` edge `0.476` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.4601` n `62` status `ready` deltaP `20.4858` edge `0.0922` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2258` n `62` status `ready` deltaP `3.6073` edge `0.13` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7909` n `90` status `ready` deltaP `12.994` edge `0.0035` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.7786` n `90` status `ready` deltaP `18.6246` edge `0.0154` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.6838` n `90` status `ready` deltaP `18.7152` edge `0.1114` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.1952` n `62` status `ready` deltaP `7.3498` edge `0.0091` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `0.1481` n `62` status `ready` deltaP `24.7648` edge `0.0105` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.0801` n `90` status `ready` deltaP `9.5043` edge `0.0358` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0407` n `90` status `ready` deltaP `4.2315` edge `0.006` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
