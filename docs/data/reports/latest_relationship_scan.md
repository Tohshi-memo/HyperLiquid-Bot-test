# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T09:22:28.484760+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.0645` n `169` status `ready` deltaP `13.1501` edge `0.0725` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8103` n `136` status `ready` deltaP `18.7634` edge `0.0232` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7476` n `169` status `ready` deltaP `10.1699` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0774` n `169` status `ready` deltaP `8.5533` edge `0.0094` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1413` n `169` status `ready` deltaP `3.9675` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6087` n `136` status `ready` deltaP `1.6528` edge `0.0914` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.8039` n `169` status `ready` deltaP `-2.5768` edge `-0.0021` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8109` n `169` status `ready` deltaP `-4.6584` edge `-0.0093` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.1347` n `169` status `ready` deltaP `-1.1862` edge `-0.0084` maxDD `-1.26`
- `market_context_high->equity_24h` score `-1.1666` n `136` status `ready` deltaP `-0.3899` edge `0.2197` maxDD `-21.1456`
- `market_context_high->metal_24h` score `-1.2113` n `136` status `ready` deltaP `-2.4276` edge `0.0434` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2352` n `169` status `ready` deltaP `-1.9062` edge `-0.0032` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5777` n `169` status `ready` deltaP `-9.1282` edge `-0.0393` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9341` n `169` status `ready` deltaP `-6.0568` edge `-0.0312` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.1234` n `169` status `ready` deltaP `-10.8572` edge `-0.1155` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6294` n `169` status `ready` deltaP `-10.3904` edge `-0.0598` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.973` n `169` status `ready` deltaP `-12.2099` edge `-0.1522` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4375` n `136` status `ready` deltaP `-11.9075` edge `-0.1461` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7483` n `136` status `ready` deltaP `-2.8902` edge `-0.127` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5776` n `136` status `ready` deltaP `-5.3752` edge `-0.1923` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
