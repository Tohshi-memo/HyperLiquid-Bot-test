# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T18:52:33.729507+00:00`
- Price records: `672`
- Market context records: `5585`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.9655` n `174` status `ready` deltaP `15.0084` edge `0.7383` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1952` n `200` status `ready` deltaP `11.7378` edge `0.2506` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.9663` n `174` status `ready` deltaP `18.6602` edge `0.0535` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.5945` n `200` status `ready` deltaP `6.2256` edge `0.1719` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5833` n `200` status `ready` deltaP `7.0793` edge `0.1655` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `0.4253` n `174` status `ready` deltaP `13.1047` edge `0.4021` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.1693` n `212` status `ready` deltaP `6.2987` edge `0.037` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2372` n `212` status `ready` deltaP `3.3104` edge `0.0075` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3064` n `212` status `ready` deltaP `1.0112` edge `0.0008` maxDD `-0.4122`
- `market_context_high->crypto_major_1h` score `-0.4383` n `212` status `ready` deltaP `3.2793` edge `0.0465` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5558` n `212` status `ready` deltaP `-0.6214` edge `0.0004` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.5641` n `200` status `ready` deltaP `4.5122` edge `0.0088` maxDD `-0.8712`
- `market_context_high->crypto_alt_1h` score `-0.6516` n `212` status `ready` deltaP `0.4576` edge `0.0388` maxDD `-5.0257`
- `market_context_high->commodity_1h` score `-1.2314` n `212` status `ready` deltaP `-2.6353` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5315` n `200` status `ready` deltaP `2.7744` edge `0.0148` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.1689` n `174` status `ready` deltaP `11.8235` edge `0.0418` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.007` n `200` status `ready` deltaP `-13.0427` edge `-0.0602` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2558` n `200` status `ready` deltaP `-5.7744` edge `-0.0486` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9748` n `174` status `ready` deltaP `-8.3273` edge `-0.2308` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.6724` n `174` status `ready` deltaP `2.8915` edge `0.0444` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
