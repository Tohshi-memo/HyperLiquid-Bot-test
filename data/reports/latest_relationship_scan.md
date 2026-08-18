# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T10:01:36.389607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2173` n `85` status `ready` deltaP `7.75` edge `0.2539` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5155` n `85` status `ready` deltaP `16.5623` edge `0.2672` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0626` n `97` status `ready` deltaP `9.3247` edge `0.0568` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7852` n `97` status `ready` deltaP `9.874` edge `0.1017` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7314` n `97` status `ready` deltaP `14.3748` edge `0.0227` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6662` n `97` status `ready` deltaP `12.9514` edge `0.0079` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5255` n `97` status `ready` deltaP `9.4605` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3802` n `97` status `ready` deltaP `11.0935` edge `0.1065` maxDD `-5.5373`
- `market_context_high->metal_1h` score `0.0041` n `97` status `ready` deltaP `4.5064` edge `0.009` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0891` n `85` status `ready` deltaP `13.6487` edge `-0.0796` maxDD `-0.1719`
- `market_context_high->equity_4h` score `-0.1504` n `97` status `ready` deltaP `1.5778` edge `0.0674` maxDD `-2.5696`
- `market_context_high->fx_4h` score `-0.2739` n `97` status `ready` deltaP `2.3526` edge `-0.0003` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2917` n `97` status `ready` deltaP `3.1591` edge `0.0217` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.4141` n `97` status `ready` deltaP `3.6522` edge `0.0076` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4219` n `97` status `ready` deltaP `1.9785` edge `0.0172` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4767` n `97` status `ready` deltaP `-3.8907` edge `0.001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6065` n `97` status `ready` deltaP `0.7277` edge `0.0101` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.912` n `97` status `ready` deltaP `-7.2829` edge `-0.0071` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.9885` n `85` status `ready` deltaP `-7.1709` edge `0.0175` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.4427` n `85` status `ready` deltaP `-15.0433` edge `-0.181` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
