# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T15:37:35.887549+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `37.1397` n `90` status `ready` deltaP `-5.5707` edge `3.186` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7456` n `62` status `ready` deltaP `36.9888` edge `0.6692` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5997` n `62` status `ready` deltaP `24.5422` edge `0.6041` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.0712` n `62` status `ready` deltaP `29.2894` edge `0.144` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.8229` n `62` status `ready` deltaP `9.3196` edge `0.2664` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.1301` n `62` status `ready` deltaP `34.3718` edge `0.0579` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4581` n `62` status `ready` deltaP `10.1065` edge `0.173` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4047` n `62` status `ready` deltaP `20.1576` edge `0.1258` maxDD `-2.7837`
- `market_context_high->crypto_major_24h` score `2.3216` n `90` status `ready` deltaP `7.3541` edge `0.546` maxDD `-16.7906`
- `market_context_high->crypto_major_4h` score `2.2408` n `90` status `ready` deltaP `15.0533` edge `0.1828` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0764` n `62` status `ready` deltaP `25.9994` edge `0.0147` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4646` n `62` status `ready` deltaP `20.5577` edge `0.0923` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3364` n `62` status `ready` deltaP `4.1347` edge `0.1357` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.852` n `90` status `ready` deltaP `19.452` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.7694` n `90` status `ready` deltaP `18.9659` edge `0.1207` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7439` n `90` status `ready` deltaP `12.4664` edge `0.0031` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.1604` n `62` status `ready` deltaP `6.9748` edge `0.0087` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1327` n `90` status `ready` deltaP `10.0348` edge `0.039` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `0.0901` n `90` status `ready` deltaP `-4.4901` edge `0.2098` maxDD `-7.1222`
- `market_context_high->commodity_1h` score `-0.0684` n `90` status `ready` deltaP `4.0059` edge `0.0052` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
