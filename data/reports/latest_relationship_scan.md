# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T07:07:31.947690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.1627` n `169` status `ready` deltaP `14.0634` edge `0.0746` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.9355` n `136` status `ready` deltaP `19.8032` edge `0.0267` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8318` n `169` status `ready` deltaP `10.9967` edge `0.0303` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.1405` n `169` status `ready` deltaP `9.1622` edge `0.0106` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1038` n `169` status `ready` deltaP `4.6435` edge `0.0009` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6171` n `136` status `ready` deltaP `1.6528` edge `0.0907` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7985` n `169` status `ready` deltaP `-2.4943` edge `-0.0022` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8337` n `169` status `ready` deltaP `-5.0229` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.052` n `169` status `ready` deltaP `-0.2729` edge `-0.0076` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.2288` n `136` status `ready` deltaP `-2.6009` edge `0.0431` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2315` n `169` status `ready` deltaP `-1.8149` edge `-0.0035` maxDD `-4.6286`
- `market_context_high->equity_24h` score `-1.506` n `136` status `ready` deltaP `-1.2565` edge `0.1972` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5389` n `169` status `ready` deltaP `-8.5919` edge `-0.0379` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.8955` n `169` status `ready` deltaP `-5.448` edge `-0.0303` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0314` n `169` status `ready` deltaP `-9.9439` edge `-0.1098` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.5812` n `169` status `ready` deltaP `-10.0122` edge `-0.0583` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.8511` n `169` status `ready` deltaP `-10.9922` edge `-0.1447` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4315` n `136` status `ready` deltaP `-11.9075` edge `-0.1456` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8527` n `136` status `ready` deltaP `-2.8902` edge `-0.1357` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5557` n `136` status `ready` deltaP `-5.3752` edge `-0.1895` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
