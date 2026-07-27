# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T06:07:29.758809+00:00`
- Price records: `672`
- Market context records: `8064`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0368` n `78` status `ready` deltaP `35.8441` edge `1.5218` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3686` n `87` status `ready` deltaP `32.4205` edge `0.5292` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2856` n `78` status `ready` deltaP `35.8752` edge `0.4513` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.7349` n `33` status `ready` deltaP `6.9407` edge `0.376` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `4.2472` n `78` status `ready` deltaP `32.5534` edge `0.2971` maxDD `-8.4816`
- `news_risk_high->equity_1h` score `3.6347` n `33` status `ready` deltaP `30.0581` edge `0.1341` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2797` n `87` status `ready` deltaP `31.5881` edge `0.0815` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7208` n `78` status `ready` deltaP `16.1645` edge `0.186` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.4101` n `87` status `ready` deltaP `15.3245` edge `0.142` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.3874` n `87` status `ready` deltaP `22.0633` edge `0.1141` maxDD `-0.979`
- `news_risk_high->crypto_alt_1h` score `1.6012` n `33` status `ready` deltaP `10.6061` edge `0.0822` maxDD `-0.2249`
- `news_risk_high->crypto_major_1h` score `1.5333` n `33` status `ready` deltaP `6.8273` edge `0.1056` maxDD `-0.5338`
- `market_context_high->fx_24h` score `1.442` n `78` status `ready` deltaP `30.1693` edge `0.0541` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1027` n `87` status `ready` deltaP `14.6724` edge `0.0208` maxDD `-0.4716`
- `news_risk_high->index_1h` score `0.8739` n `33` status `ready` deltaP `10.4927` edge `0.0234` maxDD `-0.3089`
- `market_context_high->metal_1h` score `0.8039` n `87` status `ready` deltaP `11.3738` edge `0.029` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4812` n `87` status `ready` deltaP `9.0216` edge `0.021` maxDD `-1.6171`
- `news_risk_high->fx_1h` score `0.2858` n `33` status `ready` deltaP `6.4916` edge `0.0063` maxDD `-0.0611`
- `market_context_high->crypto_alt_4h` score `0.228` n `87` status `ready` deltaP `3.4378` edge `0.1078` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.206` n `87` status `ready` deltaP `6.5812` edge `0.1451` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
