# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T03:52:30.470617+00:00`
- Price records: `672`
- Market context records: `7841`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `10.1166` n `132` status `ready` deltaP `28.5507` edge `0.7869` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3291` n `133` status `ready` deltaP `5.6391` edge `0.3241` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.135` n `133` status `ready` deltaP `10.4182` edge `0.2342` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0765` n `133` status `ready` deltaP `13.1579` edge `0.0461` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0737` n `133` status `ready` deltaP `13.7367` edge `0.1697` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `0.9556` n `132` status `ready` deltaP `19.5573` edge `0.1076` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8304` n `132` status `ready` deltaP `25.2187` edge `0.0471` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.755` n `133` status `ready` deltaP `8.1961` edge `0.0942` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7032` n `133` status `ready` deltaP `7.7423` edge `0.1187` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4673` n `133` status `ready` deltaP `8.6098` edge `0.0409` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3626` n `133` status `ready` deltaP `8.4943` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2503` n `133` status `ready` deltaP `4.8771` edge `0.0316` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1134` n `133` status `ready` deltaP `6.2476` edge `0.0137` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0666` n `133` status `ready` deltaP `12.8521` edge `0.0516` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3846` n `133` status `ready` deltaP `0.9743` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8123` n `133` status `ready` deltaP `1.8662` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2331` n `132` status `ready` deltaP `-5.3136` edge `0.0876` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3737` n `133` status `ready` deltaP `2.0527` edge `0.0773` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.431` n `133` status `ready` deltaP `-3.2443` edge `0.001` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.9842` n `133` status `ready` deltaP `14.9164` edge `0.1757` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
