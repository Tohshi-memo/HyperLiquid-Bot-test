# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T13:52:24.486840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3233.8848` n `31` status `ready` deltaP `1.7819` edge `269.4961` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.0739` n `31` status `ready` deltaP `3.4815` edge `268.2386` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `34.5376` n `31` status `ready` deltaP `43.0556` edge `2.5911` maxDD `0.0`
- `news_risk_high->equity_24h` score `33.7302` n `31` status `ready` deltaP `42.1875` edge `2.5296` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.5841` n `31` status `ready` deltaP `42.3611` edge `2.0996` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.5531` n `31` status `ready` deltaP `26.3031` edge `0.7911` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2988` n `31` status `ready` deltaP `38.4442` edge `0.65` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.2246` n `31` status `ready` deltaP `28.7355` edge `0.5213` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8843` n `31` status `ready` deltaP `19.3696` edge `0.8952` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6713` n `31` status `ready` deltaP `43.5764` edge `0.1821` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9192` n `31` status `ready` deltaP `41.3643` edge `0.147` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7758` n `31` status `ready` deltaP `20.4365` edge `0.1971` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4036` n `31` status `ready` deltaP `37.0722` edge `0.0625` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7597` n `31` status `ready` deltaP `32.5913` edge `0.0212` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5031` n `31` status `ready` deltaP `10.0106` edge `0.3003` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2721` n `31` status `ready` deltaP `13.0046` edge `0.2403` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4604` n `31` status `ready` deltaP `28.6845` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.989` n `31` status `ready` deltaP `15.5586` edge `0.0788` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.4531` n `31` status `ready` deltaP `12.7901` edge `0.0126` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3831` n `31` status `ready` deltaP `-2.2117` edge `0.009` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
