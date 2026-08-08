# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T13:22:35.628107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `4.4001` n `89` status `ready` deltaP `1.8239` edge `0.6605` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.036` n `89` status `ready` deltaP `11.1892` edge `0.236` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4252` n `103` status `ready` deltaP `13.5241` edge `0.0959` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.4129` n `89` status `ready` deltaP `30.8559` edge `0.0621` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9674` n `103` status `ready` deltaP `11.2377` edge `0.04` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4529` n `89` status `ready` deltaP `5.774` edge `0.1725` maxDD `-5.9008`
- `market_context_high->equity_1h` score `-0.4029` n `103` status `ready` deltaP `4.0478` edge `0.0223` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4882` n `103` status `ready` deltaP `-3.1844` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5225` n `103` status `ready` deltaP `1.7557` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5685` n `103` status `ready` deltaP `-0.3567` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6311` n `103` status `ready` deltaP `-3.8602` edge `-0.0056` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8407` n `103` status `ready` deltaP `1.4799` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0565` n `103` status `ready` deltaP `-3.2204` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.8311` n `103` status `ready` deltaP `3.3507` edge `-0.0412` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9457` n `103` status `ready` deltaP `-11.0284` edge `-0.0257` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4433` n `103` status `ready` deltaP `-7.8847` edge `-0.0514` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.8181` n `89` status `ready` deltaP `4.3851` edge `-0.1411` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.4781` n `89` status `ready` deltaP `-18.5549` edge `-0.1779` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.1044` n `103` status `ready` deltaP `-10.7314` edge `-0.1053` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.7491` n `103` status `ready` deltaP `-13.3392` edge `-0.2177` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
