# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T06:37:14.498596+00:00`
- Price records: `672`
- Market context records: `1092`
- Flow alert records: `5049`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.5571` n `152` status `ready` deltaP `35.8814` edge `1.1869` maxDD `-3.3749`
- `market_context_high->equity_24h` score `5.7934` n `152` status `ready` deltaP `14.9472` edge `0.4328` maxDD `-3.6396`
- `market_context_high->crypto_alt_24h` score `5.7506` n `152` status `ready` deltaP `12.3179` edge `0.5205` maxDD `-9.5387`
- `market_context_high->metal_24h` score `4.9714` n `152` status `ready` deltaP `-3.0595` edge `0.6014` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.7061` n `152` status `ready` deltaP `15.086` edge `0.3224` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0021` n `164` status `ready` deltaP `10.9756` edge `0.16` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0361` n `164` status `ready` deltaP `8.8415` edge `0.0957` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.7354` n `164` status `ready` deltaP `10.2134` edge `0.1618` maxDD `-6.4882`
- `market_context_high->index_1h` score `0.6284` n `170` status `ready` deltaP `8.5593` edge `0.027` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4651` n `170` status `ready` deltaP `3.5435` edge `0.0529` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1728` n `170` status `ready` deltaP `7.4657` edge `0.0412` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0787` n `170` status `ready` deltaP `7.5942` edge `0.0015` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1267` n `170` status `ready` deltaP `7.242` edge `0.0022` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2517` n `170` status `ready` deltaP `2.8355` edge `0.0444` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6182` n `164` status `ready` deltaP `2.7439` edge `0.0021` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7068` n `170` status `ready` deltaP `-1.2945` edge `-0.0012` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.7084` n `164` status `ready` deltaP `6.5549` edge `0.1477` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-1.5997` n `164` status `ready` deltaP `6.7073` edge `-0.0544` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.4091` n `164` status `ready` deltaP `9.2988` edge `-0.1411` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.029` n `164` status `ready` deltaP `-10.0609` edge `-0.0045` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
