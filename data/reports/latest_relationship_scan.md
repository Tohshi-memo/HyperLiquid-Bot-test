# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T01:37:25.644414+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8622`

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

- `market_context_high->commodity_24h` score `1.7245` n `89` status `ready` deltaP `15.5486` edge `0.1252` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.2656` n `89` status `ready` deltaP `12.3167` edge `0.4206` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.9263` n `56` status `ready` deltaP `14.6056` edge `0.0596` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.9263` n `56` status `ready` deltaP `14.6056` edge `0.0596` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.4768` n `89` status `ready` deltaP `4.4574` edge `0.1203` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.1718` n `56` status `ready` deltaP `8.3841` edge `0.2142` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1718` n `56` status `ready` deltaP `8.3841` edge `0.2142` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.098` n `56` status `ready` deltaP `6.4565` edge `0.0015` maxDD `-0.5766`
- `risk_on_and_context->index_1h` score `0.098` n `56` status `ready` deltaP `6.4565` edge `0.0015` maxDD `-0.5766`
- `risk_on_high->fx_1h` score `-0.2219` n `56` status `ready` deltaP `1.1851` edge `-0.0012` maxDD `-0.1456`
- `risk_on_and_context->fx_1h` score `-0.2219` n `56` status `ready` deltaP `1.1851` edge `-0.0012` maxDD `-0.1456`
- `risk_on_high->equity_1h` score `-0.2834` n `56` status `ready` deltaP `10.0601` edge `-0.0035` maxDD `-4.3078`
- `risk_on_and_context->equity_1h` score `-0.2834` n `56` status `ready` deltaP `10.0601` edge `-0.0035` maxDD `-4.3078`
- `market_context_high->crypto_alt_1h` score `-0.4319` n `89` status `ready` deltaP `0.259` edge `0.0929` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.5191` n `89` status `ready` deltaP `1.4003` edge `-0.0031` maxDD `-1.1567`
- `market_context_high->fx_4h` score `-0.6642` n `89` status `ready` deltaP `-3.7333` edge `0.0028` maxDD `-0.7115`
- `risk_on_high->fx_4h` score `-0.6784` n `56` status `ready` deltaP `-4.6964` edge `0.002` maxDD `-0.1781`
- `risk_on_and_context->fx_4h` score `-0.6784` n `56` status `ready` deltaP `-4.6964` edge `0.002` maxDD `-0.1781`
- `risk_on_high->commodity_4h` score `-0.8389` n `56` status `ready` deltaP `4.3906` edge `-0.0313` maxDD `-3.4415`
- `risk_on_and_context->commodity_4h` score `-0.8389` n `56` status `ready` deltaP `4.3906` edge `-0.0313` maxDD `-3.4415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
