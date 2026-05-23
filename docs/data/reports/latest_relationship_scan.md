# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T09:52:15.794302+00:00`
- Price records: `672`
- Market context records: `1619`
- Flow alert records: `6567`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.8863` n `189` status `ready` deltaP `26.3476` edge `0.9407` maxDD `-10.733`
- `market_context_high->index_24h` score `3.226` n `189` status `ready` deltaP `18.5103` edge `0.2749` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.3755` n `191` status `ready` deltaP `11.3818` edge `0.1482` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.8727` n `189` status `ready` deltaP `17.0883` edge `0.4009` maxDD `-30.0347`
- `market_context_high->crypto_alt_4h` score `0.5013` n `191` status `ready` deltaP `13.8081` edge `0.299` maxDD `-19.4759`
- `market_context_high->crypto_major_4h` score `0.2917` n `191` status `ready` deltaP `9.8383` edge `0.2427` maxDD `-13.3376`
- `market_context_high->crypto_major_24h` score `0.004` n `189` status `ready` deltaP `22.5199` edge `0.6026` maxDD `-54.5252`
- `market_context_high->fx_24h` score `-0.2615` n `189` status `ready` deltaP `7.7877` edge `0.0312` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2691` n `193` status `ready` deltaP `0.8346` edge `0.0623` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4361` n `193` status `ready` deltaP `1.8011` edge `0.0325` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6268` n `193` status `ready` deltaP `1.041` edge `0.004` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7835` n `193` status `ready` deltaP `0.1551` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8587` n `191` status `ready` deltaP `0.3208` edge `0.0352` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8936` n `193` status `ready` deltaP `-1.2263` edge `0.0293` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0395` n `193` status `ready` deltaP `0.6159` edge `0.0014` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2177` n `193` status `ready` deltaP `4.0815` edge `0.0049` maxDD `-6.3532`
- `market_context_high->crypto_alt_24h` score `-1.324` n `189` status `ready` deltaP `22.5943` edge `0.7763` maxDD `-77.9809`
- `market_context_high->fx_4h` score `-1.3828` n `191` status `ready` deltaP `-10.5279` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4191` n `191` status `ready` deltaP `8.6587` edge `0.0932` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.1976` n `191` status `ready` deltaP `-14.0332` edge `-0.1101` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
