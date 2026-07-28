# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T20:07:34.977849+00:00`
- Price records: `672`
- Market context records: `8229`
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

- `news_risk_high->unknown_24h` score `7957.2461` n `43` status `ready` deltaP `38.5417` edge `662.8469` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.476` n `54` status `ready` deltaP `27.4503` edge `0.4997` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1409` n `54` status `ready` deltaP `22.4274` edge `0.1431` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6519` n `54` status `ready` deltaP `22.2674` edge `0.0916` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3156` n `54` status `ready` deltaP `11.241` edge `0.2913` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7763` n `54` status `ready` deltaP `14.4045` edge `0.0954` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7647` n `54` status `ready` deltaP `12.1036` edge `0.1061` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3175` n `54` status `ready` deltaP `16.4691` edge `0.1983` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8713` n `54` status `ready` deltaP `8.5196` edge `0.0626` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4938` n `54` status `ready` deltaP `7.352` edge `0.021` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1518` n `54` status `ready` deltaP `6.6977` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1503` n `54` status `ready` deltaP `2.6558` edge `0.0101` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5078` n `54` status `ready` deltaP `3.698` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0952` n `54` status `ready` deltaP `-8.5108` edge `-0.0393` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0984` n `43` status `ready` deltaP `-18.6491` edge `-0.0456` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-6.1424` n `43` status `ready` deltaP `-23.2033` edge `-0.1057` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.8625` n `54` status `ready` deltaP `-32.6389` edge `-0.1902` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.7235` n `43` status `ready` deltaP `-23.9624` edge `-0.3594` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.7489` n `43` status `ready` deltaP `-21.9113` edge `-0.4999` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.6924` n `43` status `ready` deltaP `-23.4415` edge `-1.2558` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
