# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T11:53:03.236896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10803`

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

- `market_context_high->equity_4h` score `1.0355` n `102` status `ready` deltaP `7.6279` edge `0.1571` maxDD `-5.0663`
- `market_context_high->metal_4h` score `0.4616` n `102` status `ready` deltaP `13.5522` edge `0.0057` maxDD `-1.273`
- `market_context_high->equity_1h` score `0.2705` n `105` status `ready` deltaP `8.7197` edge `0.0459` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.258` n `105` status `ready` deltaP `9.809` edge `0.0048` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0396` n `102` status `ready` deltaP `7.3858` edge `0.0061` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.052` n `105` status `ready` deltaP `4.5851` edge `0.0038` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.0775` n `96` status `ready` deltaP `4.5139` edge `0.1433` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.178` n `105` status `ready` deltaP `1.3744` edge `0.0039` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.1938` n `102` status `ready` deltaP `6.0138` edge `0.0179` maxDD `-1.2645`
- `market_context_high->unknown_1h` score `-0.333` n `105` status `ready` deltaP `7.4808` edge `-0.0549` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4269` n `105` status `ready` deltaP `1.6995` edge `0.0141` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5876` n `105` status `ready` deltaP `1.8363` edge `-0.0031` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7867` n `102` status `ready` deltaP `-3.1534` edge `0.0052` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.793` n `105` status `ready` deltaP `-6.477` edge `-0.0019` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.0271` n `102` status `ready` deltaP `5.8644` edge `0.0023` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `-1.0437` n `96` status `ready` deltaP `17.7083` edge `-0.1544` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `-1.3095` n `102` status `ready` deltaP `7.7804` edge `-0.0589` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.594` n `96` status `ready` deltaP `-19.618` edge `-0.0104` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7334` n `96` status `ready` deltaP `-0.5209` edge `-0.0584` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.7976` n `96` status `ready` deltaP `-19.6181` edge `-0.1535` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
