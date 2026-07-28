# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T23:22:27.080314+00:00`
- Price records: `672`
- Market context records: `8244`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `news_risk_high->unknown_24h` score `7957.4489` n `43` status `ready` deltaP `38.5417` edge `662.8638` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.411` n `54` status `ready` deltaP `27.2979` edge `0.4953` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1913` n `54` status `ready` deltaP `22.4274` edge `0.1473` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7833` n `54` status `ready` deltaP `23.6393` edge `0.0934` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3502` n `54` status `ready` deltaP `11.6983` edge `0.2927` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7895` n `54` status `ready` deltaP `14.4045` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7001` n `54` status `ready` deltaP `11.2054` edge `0.1067` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.36` n `54` status `ready` deltaP `16.9264` edge `0.2007` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0736` n `54` status `ready` deltaP `10.044` edge `0.0693` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4878` n `54` status `ready` deltaP `7.2023` edge `0.0215` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1666` n `54` status `ready` deltaP `6.9971` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1096` n `54` status `ready` deltaP `3.1049` edge `0.0105` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4832` n `54` status `ready` deltaP `4.1553` edge `0.0061` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1684` n `54` status `ready` deltaP `-8.8102` edge `-0.0434` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0876` n `43` status `ready` deltaP `-18.6491` edge `-0.0447` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.7747` n `43` status `ready` deltaP `-20.9464` edge `-0.0901` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.9359` n `54` status `ready` deltaP `-32.7913` edge `-0.1953` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6539` n `43` status `ready` deltaP `-23.9624` edge `-0.3536` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.2623` n `43` status `ready` deltaP `-19.6544` edge `-0.4744` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.168` n `43` status `ready` deltaP `-23.4415` edge `-1.2121` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
