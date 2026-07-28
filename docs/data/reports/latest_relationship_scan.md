# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T13:07:31.519354+00:00`
- Price records: `672`
- Market context records: `8199`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8340.4575` n `43` status `ready` deltaP `36.9792` edge `694.7916` maxDD `0.0`
- `market_context_high->equity_24h` score `21.6451` n `42` status `ready` deltaP `45.3125` edge `1.5927` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.8984` n `43` status `ready` deltaP `46.3024` edge `0.6038` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.0447` n `42` status `ready` deltaP `46.3542` edge `0.4447` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.7112` n `42` status `ready` deltaP `16.4435` edge `0.9431` maxDD `-8.7187`
- `news_risk_high->equity_4h` score `6.6275` n `54` status `ready` deltaP `24.5539` edge `0.4483` maxDD `-3.4427`
- `market_context_high->index_4h` score `4.3102` n `43` status `ready` deltaP `38.755` edge `0.1051` maxDD `-0.0092`
- `market_context_high->crypto_major_24h` score `4.1011` n `42` status `ready` deltaP `15.9227` edge `0.7693` maxDD `-21.3073`
- `market_context_high->metal_4h` score `3.9398` n `43` status `ready` deltaP `38.1062` edge `0.0921` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.8132` n `43` status `ready` deltaP `19.8475` edge `0.2001` maxDD `-0.1718`
- `news_risk_high->equity_1h` score `2.931` n `54` status `ready` deltaP `21.8286` edge `0.1296` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `2.7132` n `54` status `ready` deltaP `13.8325` edge `0.325` maxDD `-2.8833`
- `market_context_high->index_24h` score `2.6343` n `42` status `ready` deltaP `23.4127` edge `0.2449` maxDD `-1.0602`
- `news_risk_high->index_4h` score `2.5768` n `54` status `ready` deltaP `21.6576` edge `0.0894` maxDD `-0.191`
- `news_risk_high->crypto_major_1h` score `2.0081` n `54` status `ready` deltaP `13.7503` edge `0.1154` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8506` n `54` status `ready` deltaP `15.0033` edge `0.0976` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.6386` n `42` status `ready` deltaP `31.0516` edge `0.0679` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4424` n `54` status `ready` deltaP `17.5362` edge `0.2072` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.4215` n `43` status `ready` deltaP `25.1671` edge `0.0283` maxDD `-0.1069`
- `market_context_high->crypto_alt_4h` score `1.1837` n `43` status `ready` deltaP `5.736` edge `0.1862` maxDD `-2.4816`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
