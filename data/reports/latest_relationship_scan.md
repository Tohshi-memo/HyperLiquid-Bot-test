# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T10:22:30.940554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `1.0403` n `169` status `ready` deltaP `12.9979` edge `0.0715` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7947` n `136` status `ready` deltaP `18.7634` edge `0.0219` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7332` n `169` status `ready` deltaP `10.0202` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.047` n `169` status `ready` deltaP `8.2489` edge `0.0089` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1335` n `169` status `ready` deltaP `4.1172` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6063` n `136` status `ready` deltaP `1.6528` edge `0.0916` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7919` n `169` status `ready` deltaP `-2.4271` edge `-0.0021` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7922` n `169` status `ready` deltaP `-4.359` edge `-0.0089` maxDD `-2.0884`
- `market_context_high->equity_24h` score `-0.9906` n `136` status `ready` deltaP `0.13` edge `0.2309` maxDD `-21.1456`
- `market_context_high->metal_24h` score `-1.1589` n `136` status `ready` deltaP `-1.9077` edge `0.0443` maxDD `-2.9193`
- `market_context_high->index_4h` score `-1.1906` n `169` status `ready` deltaP `-1.795` edge `-0.009` maxDD `-1.26`
- `market_context_high->equity_1h` score `-1.2232` n `169` status `ready` deltaP `-1.7565` edge `-0.0032` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.5575` n `169` status `ready` deltaP `-8.8288` edge `-0.0387` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9223` n `169` status `ready` deltaP `-5.9046` edge `-0.0307` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.183` n `169` status `ready` deltaP `-11.3138` edge `-0.1201` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6066` n `169` status `ready` deltaP `-10.2407` edge `-0.0589` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0036` n `169` status `ready` deltaP `-12.5143` edge `-0.1541` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4099` n `136` status `ready` deltaP `-11.9075` edge `-0.1438` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.6167` n `136` status `ready` deltaP `-2.3702` edge `-0.1195` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.583` n `136` status `ready` deltaP `-5.3752` edge `-0.193` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
