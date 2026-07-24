# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T07:37:27.465774+00:00`
- Price records: `672`
- Market context records: `7754`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `5.345` n `132` status `ready` deltaP `23.0546` edge `0.4259` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8044` n `133` status `ready` deltaP `11.8106` edge `0.0324` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.7767` n `133` status `ready` deltaP `9.1048` edge `0.2131` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `0.4673` n `133` status `ready` deltaP `12.5172` edge `0.1273` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.4526` n `133` status `ready` deltaP `8.046` edge `0.07` maxDD `-4.2072`
- `market_context_high->fx_24h` score `0.4389` n `132` status `ready` deltaP `19.6099` edge `0.0343` maxDD `-3.0343`
- `market_context_high->equity_4h` score `0.3887` n `133` status `ready` deltaP `1.9694` edge `0.228` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3614` n `133` status `ready` deltaP `8.7946` edge `0.0145` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2148` n `133` status `ready` deltaP `6.8276` edge `0.0841` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0242` n `133` status `ready` deltaP `3.2304` edge `0.0197` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1436` n `133` status `ready` deltaP `3.9954` edge `0.0073` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2169` n `133` status `ready` deltaP `3.7168` edge `0.0165` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2584` n `133` status `ready` deltaP `10.5585` edge `0.0423` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4891` n `133` status `ready` deltaP `-0.2269` edge `-0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8399` n `133` status `ready` deltaP `1.7165` edge `0.0189` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4515` n `133` status `ready` deltaP `1.2905` edge `0.0759` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4848` n `133` status `ready` deltaP `-4.0088` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.561` n `132` status `ready` deltaP `5.86` edge `-0.0108` maxDD `-7.0012`
- `market_context_high->index_24h` score `-2.2461` n `132` status `ready` deltaP `-15.8405` edge `0.0279` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2968` n `133` status `ready` deltaP `-1.7232` edge `-0.1209` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
