# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T07:50:12.723984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2754`

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

- `market_context_high->unknown_1h` score `11995.58` n `108` status `ready` deltaP `1.1367` edge `999.6439` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7437.8113` n `108` status `ready` deltaP `0.2146` edge `619.8446` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4565` n `102` status `ready` deltaP `30.77` edge `1.3422` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.502` n `102` status `ready` deltaP `16.8812` edge `1.1166` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.6595` n `108` status `ready` deltaP `5.0079` edge `0.3868` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5812` n `108` status `ready` deltaP `6.5322` edge `0.2958` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7031` n `108` status `ready` deltaP `18.7839` edge `0.0678` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0931` n `108` status `ready` deltaP `5.8383` edge `0.0198` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2397` n `108` status `ready` deltaP `3.7148` edge `0.0057` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.275` n `108` status `ready` deltaP `4.9956` edge `0.0711` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.6413` n `108` status `ready` deltaP `-1.1865` edge `0.0479` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0655` n `108` status `ready` deltaP `6.9417` edge `0.0428` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.5834` n `108` status `ready` deltaP `-11.1` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7456` n `108` status `ready` deltaP `-1.3098` edge `-0.0024` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.3612` n `108` status `ready` deltaP `-9.2205` edge `-0.0271` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.3731` n `108` status `ready` deltaP `-14.7979` edge `-0.004` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.9343` n `102` status `ready` deltaP `14.5425` edge `0.0882` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5522` n `102` status `ready` deltaP `-16.8913` edge `-0.0061` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0166` n `108` status `ready` deltaP `-28.1955` edge `-0.1108` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.1231` n `108` status `ready` deltaP `-5.9846` edge `-0.0382` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
