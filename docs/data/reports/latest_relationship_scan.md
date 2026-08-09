# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T03:07:22.668827+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.3768` n `103` status `ready` deltaP `4.5729` edge `0.5569` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6575` n `103` status `ready` deltaP `13.2535` edge `0.1907` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4353` n `126` status `ready` deltaP `14.685` edge `0.089` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9065` n `138` status `ready` deltaP `11.2709` edge `0.0347` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8384` n `103` status `ready` deltaP `21.9222` edge `0.048` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5088` n `103` status `ready` deltaP `9.1002` edge `0.1577` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.324` n `138` status `ready` deltaP `3.9226` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3762` n `126` status `ready` deltaP `7.0171` edge `-0.0028` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.6014` n `126` status `ready` deltaP `-0.5686` edge `-0.0128` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6479` n `138` status `ready` deltaP `-3.9876` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.7846` n `138` status `ready` deltaP `-2.9636` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.876` n `138` status `ready` deltaP `0.7441` edge `0.0049` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9845` n `126` status `ready` deltaP `-1.205` edge `-0.0173` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0193` n `138` status `ready` deltaP `-10.9346` edge `-0.0312` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4384` n `126` status `ready` deltaP `0.1089` edge `-0.0702` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2135` n `138` status `ready` deltaP `-10.9412` edge `-0.0648` maxDD `-7.0705`
- `market_context_high->crypto_major_24h` score `-3.5383` n `103` status `ready` deltaP `6.2197` edge `-0.0869` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.466` n `126` status `ready` deltaP `-11.1329` edge `-0.1323` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.4986` n `103` status `ready` deltaP `-12.4461` edge `-0.1476` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.3103` n `138` status `ready` deltaP `-5.5216` edge `-0.611` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
