# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T03:52:28.756840+00:00`
- Price records: `672`
- Market context records: `7099`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4184` n `156` status `ready` deltaP `16.4752` edge `0.0138` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1343` n `156` status `ready` deltaP `0.2802` edge `0.0428` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1913` n `156` status `ready` deltaP `3.9114` edge `0.0031` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4592` n `156` status `ready` deltaP `0.2342` edge `0.026` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5057` n `156` status `ready` deltaP `0.4529` edge `-0.0059` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6176` n `156` status `ready` deltaP `3.0977` edge `0.0354` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8653` n `156` status `ready` deltaP `-4.4258` edge `-0.0198` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3756` n `156` status `ready` deltaP `-4.4442` edge `-0.0432` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5362` n `156` status `ready` deltaP `-6.8747` edge `-0.0054` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.6123` n `156` status `ready` deltaP `-7.1255` edge `0.001` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1249` n `156` status `ready` deltaP `1.8847` edge `-0.0427` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.4292` n `156` status `ready` deltaP `0.1759` edge `-0.0427` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0351` n `156` status `ready` deltaP `3.8149` edge `0.0139` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1651` n `156` status `ready` deltaP `-0.9811` edge `-0.0207` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.1992` n `156` status `ready` deltaP `-6.9177` edge `-0.0896` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3048` n `156` status `ready` deltaP `-8.4936` edge `-0.0194` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.3974` n `156` status `ready` deltaP `-8.5992` edge `-0.0108` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.5456` n `156` status `ready` deltaP `-0.0079` edge `-0.2085` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8937` n `156` status `ready` deltaP `-23.905` edge `-0.0671` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.994` n `156` status `ready` deltaP `-25.1202` edge `-0.1385` maxDD `-43.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
