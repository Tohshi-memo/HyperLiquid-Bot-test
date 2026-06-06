# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T09:37:24.497999+00:00`
- Price records: `672`
- Market context records: `3060`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.67` n `94` status `ready` deltaP `11.994` edge `2.4489` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.1804` n `94` status `ready` deltaP `45.7003` edge `0.9011` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.392` n `94` status `ready` deltaP `23.7552` edge `1.0041` maxDD `-1.7175`
- `market_context_high->index_24h` score `10.9121` n `94` status `ready` deltaP `27.5931` edge `0.8301` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.2711` n `94` status `ready` deltaP `24.6602` edge `1.4276` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4682` n `128` status `ready` deltaP `16.8445` edge `0.1581` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.2294` n `131` status `ready` deltaP `0.2617` edge `0.0214` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.2944` n `128` status `ready` deltaP `2.6105` edge `0.0634` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5544` n `131` status `ready` deltaP `3.106` edge `0.0145` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.611` n `131` status `ready` deltaP `-5.9046` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7462` n `131` status `ready` deltaP `4.0191` edge `0.0905` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7776` n `94` status `ready` deltaP `-0.1662` edge `-0.0114` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.0318` n `131` status `ready` deltaP `3.0603` edge `-0.0333` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.0348` n `131` status `ready` deltaP `1.1599` edge `0.005` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.0801` n `131` status `ready` deltaP `2.7323` edge `0.0696` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.176` n `128` status `ready` deltaP `-9.1463` edge `-0.0056` maxDD `-1.0693`
- `market_context_high->metal_1h` score `-1.266` n `131` status `ready` deltaP `-3.0752` edge `-0.005` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.2848` n `128` status `ready` deltaP `10.2134` edge `0.0581` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.8984` n `128` status `ready` deltaP `18.4641` edge `0.3098` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.3987` n `128` status `ready` deltaP `8.2698` edge `0.0216` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
