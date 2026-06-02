# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T05:37:19.290317+00:00`
- Price records: `672`
- Market context records: `2633`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5105` n `143` status `ready` deltaP `18.1952` edge `0.5374` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0892` n `143` status `ready` deltaP `25.0501` edge `0.525` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.342` n `143` status `ready` deltaP `14.6406` edge `0.3619` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.3712` n `143` status `ready` deltaP `11.4814` edge `0.1358` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `1.2751` n `143` status `ready` deltaP `3.8365` edge `0.6921` maxDD `-37.9133`
- `market_context_high->crypto_alt_1h` score `1.2656` n `143` status `ready` deltaP `10.8905` edge `0.1516` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0956` n `143` status `ready` deltaP `7.9162` edge `0.1435` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6529` n `143` status `ready` deltaP `8.1938` edge `0.1192` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3374` n `143` status `ready` deltaP `9.0995` edge `0.0516` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1405` n `143` status `ready` deltaP `3.8996` edge `0.0117` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.2681` n `143` status `ready` deltaP `6.4937` edge `0.0222` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.3461` n `143` status `ready` deltaP `2.2508` edge `0.0145` maxDD `-2.0009`
- `market_context_high->metal_1h` score `-0.5776` n `143` status `ready` deltaP `-0.401` edge `0.0034` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6646` n `143` status `ready` deltaP `-0.8479` edge `0.0033` maxDD `-0.2422`
- `market_context_high->commodity_4h` score `-0.845` n `143` status `ready` deltaP `5.5401` edge `0.049` maxDD `-10.2078`
- `market_context_high->metal_4h` score `-0.9171` n `143` status `ready` deltaP `2.7353` edge `0.0283` maxDD `-4.5037`
- `market_context_high->fx_24h` score `-0.994` n `143` status `ready` deltaP `2.4913` edge `-0.0032` maxDD `-1.3662`
- `market_context_high->equity_1h` score `-1.0165` n `143` status `ready` deltaP `-1.9879` edge `0.0124` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.0453` n `143` status `ready` deltaP `-1.9636` edge `0.0096` maxDD `-0.6894`
- `market_context_high->equity_24h` score `-1.4441` n `143` status `ready` deltaP `10.112` edge `-0.09` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
