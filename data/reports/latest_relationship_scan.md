# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T05:52:12.148551+00:00`
- Price records: `619`
- Market context records: `724`
- Flow alert records: `2046`
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

- `market_context_high->crypto_major_24h` score `11.7486` n `146` status `ready` deltaP `28.4921` edge `0.8225` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3419` n `146` status `ready` deltaP `7.9193` edge `0.4805` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.319` n `149` status `ready` deltaP `5.6313` edge `0.0087` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.4085` n `146` status `ready` deltaP `-0.5292` edge `0.169` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.4539` n `154` status `ready` deltaP `2.6367` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4795` n `154` status `ready` deltaP `2.3838` edge `0.0416` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9353` n `154` status `ready` deltaP `0.6462` edge `0.0031` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9944` n `149` status `ready` deltaP `17.5676` edge `0.126` maxDD `-22.648`
- `market_context_high->crypto_major_1h` score `-1.0671` n `154` status `ready` deltaP `5.7597` edge `-0.0029` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.0673` n `154` status `ready` deltaP `-0.8268` edge `-0.0024` maxDD `-4.4826`
- `market_context_high->equity_24h` score `-1.2666` n `146` status `ready` deltaP `-2.3068` edge `0.1703` maxDD `-10.5047`
- `market_context_high->crypto_alt_1h` score `-1.4266` n `154` status `ready` deltaP `4.2878` edge `-0.016` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5823` n `154` status `ready` deltaP `-4.7915` edge `-0.0229` maxDD `-3.4946`
- `market_context_high->index_4h` score `-1.8441` n `149` status `ready` deltaP `1.1541` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9966` n `149` status `ready` deltaP `3.3134` edge `0.0685` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7953` n `149` status `ready` deltaP `-1.8509` edge `-0.0054` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3135` n `154` status `ready` deltaP `-4.7999` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6136` n `149` status `ready` deltaP `-5.331` edge `0.0845` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9836` n `149` status `ready` deltaP `4.373` edge `-0.1733` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2079` n `146` status `ready` deltaP `-13.8148` edge `-0.0584` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
