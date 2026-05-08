# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T00:07:12.569390+00:00`
- Price records: `596`
- Market context records: `699`
- Flow alert records: `1975`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.5041` n `146` status `ready` deltaP `25.5808` edge `0.7382` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6016` n `146` status `ready` deltaP `8.3151` edge `0.4995` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1891` n `149` status `ready` deltaP `7.5445` edge `0.0126` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2576` n `149` status `ready` deltaP `3.2963` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5018` n `149` status `ready` deltaP `2.2246` edge `0.0408` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5969` n `149` status `ready` deltaP `0.7088` edge `0.0041` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1398` n `149` status `ready` deltaP `-1.493` edge `-0.004` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1768` n `149` status `ready` deltaP `15.8146` edge `0.1143` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2125` n `149` status `ready` deltaP `-4.3806` edge `-0.0115` maxDD `-2.1602`
- `market_context_high->index_24h` score `-1.318` n `146` status `ready` deltaP `-3.8887` edge `0.1156` maxDD `-5.9609`
- `market_context_high->crypto_alt_1h` score `-1.4194` n `149` status `ready` deltaP `4.3034` edge `-0.0155` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6335` n `149` status `ready` deltaP `2.6473` edge `-0.0015` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.652` n `149` status `ready` deltaP `5.8555` edge `-0.0044` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9642` n `149` status `ready` deltaP `4.2443` edge `0.065` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.4979` n `146` status `ready` deltaP `-5.9075` edge `0.0917` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5554` n `149` status `ready` deltaP `-0.6513` edge `0.0066` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3271` n `149` status `ready` deltaP `-4.9099` edge `-0.0486` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.849` n `149` status `ready` deltaP `-6.4434` edge `0.0723` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.3819` n `149` status `ready` deltaP `2.5885` edge `-0.1946` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9743` n `146` status `ready` deltaP `-11.1523` edge `-0.0462` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
