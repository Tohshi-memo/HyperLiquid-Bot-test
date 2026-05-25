# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T07:37:14.143698+00:00`
- Price records: `672`
- Market context records: `1822`
- Flow alert records: `7142`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->metal_24h` score `6.8632` n `178` status `ready` deltaP `27.5905` edge `0.6306` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.8236` n `185` status `ready` deltaP `22.1696` edge `0.5353` maxDD `-5.1574`
- `news_risk_high->commodity_4h` score `6.5364` n `30` status `ready` deltaP `29.4106` edge `0.4141` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4326` n `185` status `ready` deltaP `26.0786` edge `0.4868` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.6185` n `185` status `ready` deltaP `16.9307` edge `0.4744` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6274` n `178` status `ready` deltaP `17.8683` edge `0.306` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2242` n `30` status `ready` deltaP `24.5709` edge `0.1366` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0118` n `185` status `ready` deltaP `15.9196` edge `0.2543` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5404` n `178` status `ready` deltaP `13.8655` edge `0.6513` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.521` n `178` status `ready` deltaP `17.1036` edge `0.5859` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.905` n `30` status `ready` deltaP `21.6362` edge `-0.001` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8333` n `185` status `ready` deltaP `11.7057` edge `0.1003` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4142` n `193` status `ready` deltaP `6.0043` edge `0.0931` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3101` n `193` status `ready` deltaP `6.2114` edge `0.0958` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.2737` n `30` status `ready` deltaP `8.9126` edge `0.048` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0773` n `193` status `ready` deltaP `4.6105` edge `0.0422` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.1402` n `178` status `ready` deltaP `18.1648` edge `0.7258` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1953` n `178` status `ready` deltaP `11.435` edge `0.0124` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3773` n `193` status `ready` deltaP `0.4196` edge `0.012` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4107` n `30` status `ready` deltaP `16.8563` edge `-0.1178` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
