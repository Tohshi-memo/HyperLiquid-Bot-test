# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T07:07:11.682431+00:00`
- Price records: `624`
- Market context records: `730`
- Flow alert records: `2062`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.075` n `146` status `ready` deltaP `29.0914` edge `0.8457` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4206` n `146` status `ready` deltaP `7.8378` edge `0.4876` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.2176` n `146` status `ready` deltaP `0.1621` edge `0.1803` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3467` n `149` status `ready` deltaP `5.2347` edge `0.0078` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4397` n `156` status `ready` deltaP `2.8138` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5126` n `156` status `ready` deltaP `2.1353` edge `0.0405` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9175` n `156` status `ready` deltaP `0.8242` edge `0.0034` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9709` n `149` status `ready` deltaP `17.8382` edge `0.1272` maxDD `-22.648`
- `market_context_high->equity_24h` score `-0.9986` n `146` status `ready` deltaP `-1.5659` edge `0.1877` maxDD `-10.5047`
- `market_context_high->equity_1h` score `-1.0413` n `156` status `ready` deltaP `-0.6368` edge `-0.0015` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0877` n `156` status `ready` deltaP `5.4384` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4797` n `156` status `ready` deltaP `3.9537` edge `-0.0182` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.6007` n `156` status `ready` deltaP `-4.818` edge `-0.0241` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8773` n `149` status `ready` deltaP `0.8445` edge `-0.0098` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0202` n `149` status `ready` deltaP `3.0488` edge `0.0683` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8529` n `149` status `ready` deltaP `-2.1356` edge `-0.0083` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2337` n `156` status `ready` deltaP `-4.3714` edge `-0.0444` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5553` n `149` status `ready` deltaP `-4.9924` edge `0.0871` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9501` n `149` status `ready` deltaP `4.5214` edge `-0.1715` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2622` n `146` status `ready` deltaP `-14.3627` edge `-0.0617` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
