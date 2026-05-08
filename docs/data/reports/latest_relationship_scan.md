# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T03:22:13.019213+00:00`
- Price records: `609`
- Market context records: `713`
- Flow alert records: `2015`
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

- `market_context_high->crypto_major_24h` score `11.2299` n `146` status `ready` deltaP `27.2584` edge `0.7875` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4489` n `146` status `ready` deltaP `8.087` edge `0.4883` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.265` n `149` status `ready` deltaP `6.4448` edge `0.0102` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2892` n `149` status `ready` deltaP `2.8096` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4465` n `149` status `ready` deltaP `2.5707` edge `0.0431` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.617` n `149` status `ready` deltaP `0.5025` edge `0.0029` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.7971` n `146` status `ready` deltaP `-1.9525` edge `0.1461` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.0718` n `149` status `ready` deltaP `16.8442` edge `0.1209` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1572` n `149` status `ready` deltaP `-1.4998` edge `-0.0054` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1844` n `149` status `ready` deltaP `-4.0746` edge `-0.0112` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3448` n `149` status `ready` deltaP `4.7401` edge `-0.0122` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5629` n `149` status `ready` deltaP `6.4885` edge `-0.0012` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7765` n `149` status `ready` deltaP `1.789` edge `-0.0077` maxDD `-6.5149`
- `market_context_high->equity_24h` score `-1.8075` n `146` status `ready` deltaP `-3.8324` edge `0.1354` maxDD `-10.5047`
- `market_context_high->crypto_alt_4h` score `-1.9604` n `149` status `ready` deltaP `3.8559` edge `0.0679` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7138` n `149` status `ready` deltaP `-1.2671` edge `-0.0025` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3536` n `149` status `ready` deltaP `-4.851` edge `-0.0512` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.728` n `149` status `ready` deltaP `-6.0254` edge `0.0796` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2203` n `149` status `ready` deltaP `3.3942` edge `-0.1865` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1079` n `146` status `ready` deltaP `-12.6867` edge `-0.0531` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
