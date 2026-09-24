# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T05:52:28.081356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9945`

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

- `market_context_high->unknown_1h` score `66.231` n `47` status `ready` deltaP `10.7148` edge `5.4549` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.891` n `46` status `ready` deltaP `26.2078` edge `3.0818` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `23.7024` n `46` status `ready` deltaP `21.1806` edge `1.834` maxDD `0.0`
- `market_context_high->equity_24h` score `22.4568` n `46` status `ready` deltaP `23.6036` edge `1.7241` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.4932` n `46` status `ready` deltaP `32.6314` edge `0.4156` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.1498` n `103` status `ready` deltaP `-1.4832` edge `1.3433` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.9251` n `103` status `ready` deltaP `14.6889` edge `0.4123` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8291` n `103` status `ready` deltaP `18.8048` edge `0.3348` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6808` n `105` status `ready` deltaP `14.5552` edge `0.1754` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.6596` n `47` status `ready` deltaP `31.13` edge `0.0295` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.6424` n `46` status `ready` deltaP `26.6078` edge `0.0662` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.172` n `105` status `ready` deltaP `16.651` edge `0.1135` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `2.1197` n `103` status `ready` deltaP `21.6643` edge `0.1501` maxDD `-2.431`
- `market_context_high->equity_4h` score `1.8258` n `47` status `ready` deltaP `13.9433` edge `0.101` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6014` n `103` status `ready` deltaP `23.3765` edge `0.0412` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.4403` n `103` status `ready` deltaP `-4.0621` edge `0.8484` maxDD `-49.7699`
- `news_risk_high->fx_24h` score `1.2288` n `103` status `ready` deltaP `29.6639` edge `0.1229` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8433` n `47` status `ready` deltaP `13.4125` edge `0.0087` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6593` n `105` status `ready` deltaP `15.402` edge `0.0116` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6526` n `47` status `ready` deltaP `9.3706` edge `0.0322` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
