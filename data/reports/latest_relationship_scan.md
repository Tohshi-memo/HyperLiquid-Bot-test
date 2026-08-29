# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T03:22:13.907119+00:00`
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

- `news_risk_high->unknown_24h` score `57.3002` n `50` status `ready` deltaP `19.7574` edge `4.6433` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.5227` n `50` status `ready` deltaP `46.6066` edge `2.6103` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `10.0593` n `50` status `ready` deltaP `28.0208` edge `0.7008` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.8765` n `71` status `ready` deltaP `18.3485` edge `0.6484` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.1503` n `50` status `ready` deltaP `30.1005` edge `0.488` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.6089` n `120` status `ready` deltaP `13.0907` edge `0.5367` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.5138` n `50` status `ready` deltaP `43.4073` edge `0.091` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.331` n `120` status `ready` deltaP `28.7406` edge `0.1879` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.479` n `50` status `ready` deltaP `26.9948` edge `0.0417` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.3627` n `79` status `ready` deltaP `4.6635` edge `0.2015` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.319` n `120` status `ready` deltaP `18.0082` edge `0.1139` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.3015` n `71` status `ready` deltaP `33.5258` edge `0.0232` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.8999` n `120` status `ready` deltaP `9.2416` edge `0.0584` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5761` n `79` status `ready` deltaP `12.1883` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4387` n `79` status `ready` deltaP `12.4744` edge `0.0051` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0861` n `120` status `ready` deltaP `10.4065` edge `0.0113` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3476` n `120` status `ready` deltaP `4.3613` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3794` n `79` status `ready` deltaP `0.47` edge `-0.0081` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4109` n `120` status `ready` deltaP `13.7906` edge `0.2189` maxDD `-20.9394`
- `news_risk_high->equity_1h` score `-0.5506` n `79` status `ready` deltaP `9.0313` edge `-0.0374` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
