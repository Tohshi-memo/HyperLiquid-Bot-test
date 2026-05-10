# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T09:52:17.630530+00:00`
- Price records: `672`
- Market context records: `963`
- Flow alert records: `2698`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.9387` n `153` status `ready` deltaP `33.5376` edge `1.0547` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.202` n `153` status `ready` deltaP `10.0694` edge `0.6997` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2687` n `153` status `ready` deltaP `1.4706` edge `0.3564` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.535` n `153` status `ready` deltaP `-0.0613` edge `0.2445` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3388` n `204` status `ready` deltaP `2.0312` edge `0.0011` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.387` n `204` status `ready` deltaP `1.6995` edge `0.0372` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.5776` n `204` status `ready` deltaP `1.8199` edge `0.0166` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6724` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6935` n `204` status `ready` deltaP `3.2347` edge `0.006` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2753` n `192` status `ready` deltaP `2.2993` edge `0.0936` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.2833` n `204` status `ready` deltaP `-2.2602` edge `-0.0147` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.5709` n `192` status `ready` deltaP `-0.8003` edge `0.0267` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6062` n `204` status `ready` deltaP `6.4283` edge `-0.0044` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.8352` n `204` status `ready` deltaP `1.9109` edge `-0.0217` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8954` n `204` status `ready` deltaP `-2.5155` edge `-0.0303` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.4737` n `192` status `ready` deltaP `8.9939` edge `0.1045` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.5911` n `192` status `ready` deltaP `-0.7749` edge `0.081` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2616` n `192` status `ready` deltaP `-2.2485` edge `0.021` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.2686` n `192` status `ready` deltaP `7.0249` edge `-0.1314` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.0505` n `153` status `ready` deltaP `5.9232` edge `-0.0082` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
