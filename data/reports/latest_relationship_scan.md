# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T18:37:29.180859+00:00`
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

- `news_risk_high->unknown_24h` score `54.3381` n `50` status `ready` deltaP `13.6915` edge `4.4369` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.8257` n `50` status `ready` deltaP `44.3536` edge `2.4839` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.6015` n `58` status `ready` deltaP `23.1918` edge `0.8264` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `5.8877` n `50` status `ready` deltaP `23.5147` edge `0.3832` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `5.8411` n `50` status `ready` deltaP `30.1005` edge `0.3789` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.335` n `50` status `ready` deltaP `43.4073` edge `0.0761` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.975` n `58` status `ready` deltaP `46.2573` edge `0.0319` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.6468` n `120` status `ready` deltaP `7.0248` edge `0.3303` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.6363` n `69` status `ready` deltaP `10.0387` edge `0.2718` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.1522` n `120` status `ready` deltaP `28.7406` edge `0.173` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.3734` n `50` status `ready` deltaP `26.9948` edge `0.0329` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3403` n `120` status `ready` deltaP `17.7033` edge `0.1177` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.8831` n `120` status `ready` deltaP `9.2416` edge `0.057` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7132` n `69` status `ready` deltaP `13.8158` edge `0.006` maxDD `-0.094`
- `news_risk_high->commodity_1h` score `0.5154` n `69` status `ready` deltaP `13.8158` edge `0.006` maxDD `-0.5618`
- `news_risk_high->equity_4h` score `0.2388` n `58` status `ready` deltaP `17.8984` edge `0.0206` maxDD `-4.7449`
- `news_risk_high->metal_4h` score `0.1109` n `58` status `ready` deltaP `12.0585` edge `0.0009` maxDD `-1.3656`
- `market_context_high->metal_4h` score `0.0222` n `120` status `ready` deltaP `13.1504` edge `0.0069` maxDD `-3.3377`
- `news_risk_high->index_4h` score `-0.0954` n `58` status `ready` deltaP `5.5246` edge `-0.0052` maxDD `-0.5091`
- `news_risk_high->index_1h` score `-0.4069` n `69` status `ready` deltaP `0.0304` edge `-0.0092` maxDD `-0.787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
