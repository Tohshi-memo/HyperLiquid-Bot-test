# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T05:07:23.990518+00:00`
- Price records: `672`
- Market context records: `8270`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7118.807` n `47` status `ready` deltaP `39.0625` edge `592.9735` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2743` n `54` status `ready` deltaP `26.3832` edge `0.49` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.2333` n `54` status `ready` deltaP `22.4274` edge `0.1508` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7559` n `54` status `ready` deltaP `22.8771` edge `0.0962` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1567` n `54` status `ready` deltaP `10.6313` edge `0.275` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9358` n `54` status `ready` deltaP `15.0033` edge `0.1047` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6713` n `54` status `ready` deltaP `10.906` edge `0.1063` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4307` n `54` status `ready` deltaP `16.6215` edge `0.2118` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1096` n `54` status `ready` deltaP `10.044` edge `0.0723` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5394` n `54` status `ready` deltaP `7.5017` edge `0.0238` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2366` n `54` status `ready` deltaP `8.1947` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.058` n `54` status `ready` deltaP `3.4043` edge `0.0128` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.412` n `54` status `ready` deltaP `5.3748` edge `0.0071` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1695` n `54` status `ready` deltaP `-8.9599` edge `-0.0425` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.4586` n `47` status `ready` deltaP `-19.4408` edge `-0.0469` maxDD `-4.6039`
- `news_risk_high->metal_24h` score `-5.9091` n `47` status `ready` deltaP `-21.3874` edge `-0.0752` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.9786` n `54` status `ready` deltaP `-32.334` edge `-0.2019` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.0746` n `47` status `ready` deltaP `-25.2992` edge `-0.3392` maxDD `-26.2018`
- `news_risk_high->commodity_24h` score `-12.7558` n `47` status `ready` deltaP `-14.1031` edge `-0.3835` maxDD `-33.1706`
- `news_risk_high->equity_24h` score `-35.5152` n `47` status `ready` deltaP `-24.4311` edge `-1.1738` maxDD `-116.1673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
