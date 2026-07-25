# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T09:21:05.531951+00:00`
- Price records: `672`
- Market context records: `7864`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.7637` n `125` status `ready` deltaP `29.0087` edge `0.9211` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.7883` n `126` status `ready` deltaP `6.8953` edge `0.3381` maxDD `-6.384`
- `market_context_high->metal_24h` score `1.7665` n `126` status `ready` deltaP `11.5361` edge `0.2478` maxDD `-2.1996`
- `market_context_high->commodity_24h` score `1.3941` n `125` status `ready` deltaP `21.8435` edge `0.1289` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.3706` n `126` status `ready` deltaP `15.7835` edge `0.1808` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1233` n `126` status `ready` deltaP `12.9978` edge `0.0469` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.0106` n `126` status `ready` deltaP `9.8602` edge `0.1302` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.9291` n `125` status `ready` deltaP `26.9217` edge `0.0484` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.5852` n `126` status `ready` deltaP `8.773` edge `0.0983` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4414` n `126` status `ready` deltaP `8.3152` edge `0.0407` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.2962` n `126` status `ready` deltaP `4.971` edge `0.0348` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.2171` n `126` status `ready` deltaP `8.151` edge `0.0165` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.0989` n `126` status `ready` deltaP `6.006` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2016` n `126` status `ready` deltaP `10.3466` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3183` n `126` status `ready` deltaP `-0.2789` edge `-0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9078` n `126` status `ready` deltaP `0.5679` edge `0.0209` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.0583` n `126` status `ready` deltaP `3.3537` edge `0.0822` maxDD `-1.4202`
- `market_context_high->index_24h` score `-1.0866` n `125` status `ready` deltaP `-4.7652` edge `0.0978` maxDD `-2.0943`
- `market_context_high->fx_4h` score `-1.4034` n `126` status `ready` deltaP `-2.7013` edge `0.0006` maxDD `-1.6677`
- `market_context_high->crypto_alt_24h` score `-1.5312` n `126` status `ready` deltaP `15.3022` edge `0.2312` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
