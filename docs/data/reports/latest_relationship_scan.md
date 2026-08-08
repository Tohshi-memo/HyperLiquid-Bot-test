# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T12:52:33.762673+00:00`
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

- `market_context_high->equity_24h` score `4.9197` n `87` status `ready` deltaP `2.3348` edge `0.7004` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.3054` n `87` status `ready` deltaP `12.7274` edge `0.2482` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4264` n `103` status `ready` deltaP `13.5241` edge `0.096` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.3992` n `87` status `ready` deltaP `30.5316` edge `0.0625` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9674` n `103` status `ready` deltaP `11.2377` edge `0.04` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.5908` n `87` status `ready` deltaP `7.0283` edge `0.1802` maxDD `-5.7715`
- `market_context_high->equity_1h` score `-0.4041` n `103` status `ready` deltaP `4.0478` edge `0.0222` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4882` n `103` status `ready` deltaP `-3.1844` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5345` n `103` status `ready` deltaP `1.606` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5693` n `103` status `ready` deltaP `-0.3567` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8395` n `103` status `ready` deltaP `1.4799` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0652` n `103` status `ready` deltaP `-3.3729` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.8129` n `103` status `ready` deltaP `3.5031` edge `-0.0407` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9134` n `103` status `ready` deltaP `-10.729` edge `-0.025` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4134` n `103` status `ready` deltaP `-7.5853` edge `-0.0509` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.7271` n `87` status `ready` deltaP `5.6394` edge `-0.1378` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.5614` n `87` status `ready` deltaP `-19.5881` edge `-0.1817` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.0572` n `103` status `ready` deltaP `-10.4266` edge `-0.1034` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.7055` n `103` status `ready` deltaP `-13.0343` edge `-0.2161` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
