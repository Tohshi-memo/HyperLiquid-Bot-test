# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T12:37:35.759144+00:00`
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

- `market_context_high->equity_24h` score `5.2687` n `86` status `ready` deltaP `3.0967` edge `0.7244` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.4668` n `86` status `ready` deltaP `13.5295` edge `0.2563` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4264` n `103` status `ready` deltaP `13.5241` edge `0.096` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.3901` n `86` status `ready` deltaP `30.3577` edge `0.0625` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9674` n `103` status `ready` deltaP `11.2377` edge `0.04` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.6615` n `86` status `ready` deltaP `7.6833` edge `0.1849` maxDD `-5.7715`
- `market_context_high->equity_1h` score `-0.4041` n `103` status `ready` deltaP `4.0478` edge `0.0222` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5345` n `103` status `ready` deltaP `1.606` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5693` n `103` status `ready` deltaP `-0.3567` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6475` n `103` status `ready` deltaP `-4.1596` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8273` n `103` status `ready` deltaP `1.6324` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0732` n `103` status `ready` deltaP `-3.5253` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7971` n `103` status `ready` deltaP `3.6556` edge `-0.0404` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8942` n `103` status `ready` deltaP `-10.5793` edge `-0.0244` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3966` n `103` status `ready` deltaP `-7.4356` edge `-0.0505` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6806` n `86` status `ready` deltaP `6.2944` edge `-0.1362` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.604` n `86` status `ready` deltaP `-20.1227` edge `-0.1836` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.0318` n `103` status `ready` deltaP `-10.2741` edge `-0.1023` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.6825` n `103` status `ready` deltaP `-12.8818` edge `-0.2152` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
