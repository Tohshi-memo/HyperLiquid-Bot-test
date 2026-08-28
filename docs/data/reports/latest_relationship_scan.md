# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T18:52:29.444384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.4108` n `50` status `ready` deltaP `13.8648` edge `4.4418` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.9451` n `50` status `ready` deltaP `44.5269` edge `2.4927` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.3946` n `59` status `ready` deltaP `23.2146` edge `0.809` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `6.0587` n `50` status `ready` deltaP `23.688` edge `0.3963` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `5.8783` n `50` status `ready` deltaP `30.1005` edge `0.382` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.341` n `50` status `ready` deltaP `43.4073` edge `0.0766` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.8537` n `59` status `ready` deltaP `44.861` edge `0.0311` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.7195` n `120` status `ready` deltaP `7.1981` edge `0.3352` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.4047` n `70` status `ready` deltaP `9.1532` edge `0.2584` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.1582` n `120` status `ready` deltaP `28.7406` edge `0.1735` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.3758` n `50` status `ready` deltaP `26.9948` edge `0.0331` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3173` n `120` status `ready` deltaP `17.5508` edge `0.1168` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9059` n `120` status `ready` deltaP `9.3913` edge `0.0579` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6527` n `70` status `ready` deltaP `13.0753` edge `0.0059` maxDD `-0.094`
- `news_risk_high->commodity_1h` score `0.4606` n `70` status `ready` deltaP `12.9256` edge `0.0049` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0316` n `120` status `ready` deltaP `13.1504` edge `0.0081` maxDD `-3.3377`
- `news_risk_high->metal_4h` score `-0.1195` n `59` status `ready` deltaP `10.9188` edge `-0.0112` maxDD `-2.1528`
- `news_risk_high->equity_4h` score `-0.1555` n `59` status `ready` deltaP `16.882` edge `-0.0036` maxDD `-6.3111`
- `news_risk_high->index_4h` score `-0.2073` n `59` status `ready` deltaP `4.5602` edge `-0.0096` maxDD `-0.7902`
- `market_context_high->fx_1h` score `-0.4044` n `120` status `ready` deltaP `3.3134` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
