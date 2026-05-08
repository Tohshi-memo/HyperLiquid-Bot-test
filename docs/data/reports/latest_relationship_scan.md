# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T09:52:15.672351+00:00`
- Price records: `635`
- Market context records: `742`
- Flow alert records: `2096`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.7485` n `146` status `ready` deltaP `30.3708` edge `0.8933` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6059` n `146` status `ready` deltaP `7.6639` edge `0.5042` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.1801` n `146` status `ready` deltaP `1.6374` edge `0.2036` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3428` n `161` status `ready` deltaP `3.9654` edge `0.0028` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4291` n `156` status `ready` deltaP `6.2821` edge `0.0095` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-0.4905` n `146` status `ready` deltaP `0.0154` edge `0.2195` maxDD `-10.5047`
- `market_context_high->commodity_1h` score `-0.5827` n `161` status `ready` deltaP `1.5741` edge `0.0384` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8613` n `161` status `ready` deltaP `1.3462` edge `0.0046` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0022` n `161` status `ready` deltaP `-0.5676` edge `0.0013` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0718` n `161` status `ready` deltaP `5.6245` edge `-0.0026` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4468` n `161` status `ready` deltaP `4.0958` edge `-0.0164` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5406` n `161` status `ready` deltaP `-4.4718` edge `-0.0214` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5585` n `156` status `ready` deltaP `17.5241` edge `0.1239` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.757` n `156` status `ready` deltaP `1.8074` edge `-0.0062` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1685` n `156` status `ready` deltaP `2.4999` edge `0.0596` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5496` n `156` status `ready` deltaP `-1.1195` edge `0.0102` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1332` n `161` status `ready` deltaP `-3.9403` edge `-0.0389` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6671` n `156` status `ready` deltaP `-5.3846` edge `0.0804` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7481` n `156` status `ready` deltaP `5.1416` edge `-0.1588` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3752` n `146` status `ready` deltaP `-15.532` edge `-0.0684` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
