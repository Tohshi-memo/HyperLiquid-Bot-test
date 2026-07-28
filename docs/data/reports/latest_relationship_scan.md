# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T14:37:42.991171+00:00`
- Price records: `672`
- Market context records: `8205`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8187.4779` n `43` status `ready` deltaP `36.9792` edge `682.0433` maxDD `0.0`
- `market_context_high->equity_24h` score `22.6798` n `36` status `ready` deltaP `43.5764` edge `1.6905` maxDD `-4.9489`
- `market_context_high->crypto_alt_24h` score `14.2237` n `36` status `ready` deltaP `25.1736` edge `1.1353` maxDD `-4.7588`
- `market_context_high->equity_4h` score `9.3358` n `37` status `ready` deltaP `46.84` edge `0.47` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.9889` n `36` status `ready` deltaP `47.3958` edge `0.4331` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `8.1715` n `36` status `ready` deltaP `24.6528` edge `1.0904` maxDD `-11.9028`
- `news_risk_high->equity_4h` score `7.0931` n `54` status `ready` deltaP `25.4686` edge `0.481` maxDD `-3.4427`
- `market_context_high->index_4h` score `3.9795` n `37` status `ready` deltaP `38.3858` edge `0.08` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.7707` n `37` status `ready` deltaP `37.2075` edge `0.084` maxDD `-0.0926`
- `market_context_high->crypto_alt_4h` score `3.5996` n `37` status `ready` deltaP `14.0327` edge `0.2393` maxDD `-0.9638`
- `market_context_high->crypto_major_4h` score `3.5871` n `37` status `ready` deltaP `16.7354` edge `0.2718` maxDD `-3.4225`
- `market_context_high->index_24h` score `3.2237` n `36` status `ready` deltaP `30.7292` edge `0.2704` maxDD `-0.9576`
- `news_risk_high->equity_1h` score `3.2189` n `54` status `ready` deltaP `22.7268` edge `0.1476` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.1703` n `37` status `ready` deltaP `16.2203` edge `0.1707` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `2.7139` n `54` status `ready` deltaP `13.8325` edge `0.3251` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6737` n `54` status `ready` deltaP `22.4198` edge `0.0924` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `2.0093` n `54` status `ready` deltaP `13.6006` edge `0.1165` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8926` n `54` status `ready` deltaP `15.153` edge `0.1001` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.7787` n `36` status `ready` deltaP `33.1597` edge `0.0718` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4557` n `54` status `ready` deltaP `17.5362` edge `0.2089` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
