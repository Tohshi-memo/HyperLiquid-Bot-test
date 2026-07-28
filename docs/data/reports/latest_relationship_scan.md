# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T12:52:29.105047+00:00`
- Price records: `672`
- Market context records: `8198`
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

- `news_risk_high->unknown_24h` score `8365.9731` n `43` status `ready` deltaP `36.9792` edge `696.9179` maxDD `0.0`
- `market_context_high->equity_24h` score `21.2284` n `43` status `ready` deltaP `43.3745` edge `1.5709` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.1448` n `44` status `ready` deltaP `46.2029` edge `0.625` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.0308` n `43` status `ready` deltaP `46.1806` edge `0.4447` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.0091` n `53` status `ready` deltaP `25.8341` edge `0.4607` maxDD `-2.9069`
- `market_context_high->crypto_alt_24h` score `6.289` n `43` status `ready` deltaP `15.2253` edge `0.9118` maxDD `-9.562`
- `market_context_high->index_4h` score `4.3515` n `44` status `ready` deltaP `38.7611` edge `0.1085` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9517` n `44` status `ready` deltaP `38.1652` edge `0.0927` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.852` n `44` status `ready` deltaP `20.4818` edge `0.1991` maxDD `-0.1718`
- `market_context_high->crypto_major_24h` score `3.4764` n `43` status `ready` deltaP `14.7045` edge `0.7222` maxDD `-22.9634`
- `news_risk_high->equity_1h` score `2.931` n `54` status `ready` deltaP `21.8286` edge `0.1296` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `2.7115` n `53` status `ready` deltaP `13.2162` edge `0.3289` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.69` n `53` status `ready` deltaP `22.9378` edge `0.0903` maxDD `-0.191`
- `market_context_high->index_24h` score `2.5063` n `43` status `ready` deltaP `22.0284` edge `0.2393` maxDD `-1.1866`
- `news_risk_high->crypto_major_1h` score `2.0237` n `54` status `ready` deltaP `13.9` edge `0.1157` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8686` n `54` status `ready` deltaP `15.153` edge `0.0981` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.5581` n `43` status `ready` deltaP `29.6673` edge `0.0668` maxDD `-0.5196`
- `market_context_high->index_1h` score `1.4486` n `44` status `ready` deltaP `25.7485` edge `0.0279` maxDD `-0.1069`
- `news_risk_high->crypto_alt_4h` score `1.4008` n `53` status `ready` deltaP `16.9898` edge `0.2055` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `1.0416` n `44` status `ready` deltaP `4.7256` edge `0.1812` maxDD `-2.6662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
