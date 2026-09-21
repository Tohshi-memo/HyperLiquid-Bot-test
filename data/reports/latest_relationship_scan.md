# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T06:37:27.937209+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9194`

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

- `market_context_high->unknown_4h` score `32.4505` n `58` status `ready` deltaP `1.23` edge `2.711` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.9242` n `98` status `ready` deltaP `11.4017` edge `2.6035` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.4883` n `98` status `ready` deltaP `11.9685` edge `1.949` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.4468` n `101` status `ready` deltaP `19.6812` edge `0.3603` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0131` n `101` status `ready` deltaP `21.5105` edge `0.3168` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7558` n `101` status `ready` deltaP `16.3811` edge `0.167` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.124` n `101` status `ready` deltaP `18.1775` edge `0.1081` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2609` n `98` status `ready` deltaP `23.9902` edge `0.1323` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0236` n `58` status `ready` deltaP `7.6554` edge `0.0596` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8143` n `58` status `ready` deltaP `11.7747` edge `0.0149` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6317` n `101` status `ready` deltaP `14.7477` edge `0.0145` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.3896` n `58` status `ready` deltaP `15.696` edge `0.009` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.3864` n `101` status `ready` deltaP `15.422` edge `0.0348` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3537` n `58` status `ready` deltaP `6.2978` edge `0.0183` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3331` n `58` status `ready` deltaP `8.6259` edge `0.0059` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1797` n `101` status `ready` deltaP `8.3358` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0512` n `101` status `ready` deltaP `3.2682` edge `0.0145` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1609` n `58` status `ready` deltaP `-1.6415` edge `0.0694` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.216` n `101` status `ready` deltaP `2.9925` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3326` n `98` status `ready` deltaP `10.1226` edge `-0.0257` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
