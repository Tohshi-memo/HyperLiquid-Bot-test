# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T10:22:29.656151+00:00`
- Price records: `672`
- Market context records: `7766`
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

- `market_context_high->equity_24h` score `6.2327` n `132` status `ready` deltaP `24.9709` edge `0.4871` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.0795` n `133` status `ready` deltaP `11.0145` edge `0.2256` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9063` n `133` status `ready` deltaP `12.4094` edge `0.0369` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5635` n `132` status `ready` deltaP `21.5263` edge `0.0375` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4479` n `133` status `ready` deltaP `12.3647` edge `0.1267` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.3998` n `133` status `ready` deltaP `7.4454` edge `0.0696` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3894` n `133` status `ready` deltaP `1.8165` edge `0.2291` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3086` n `133` status `ready` deltaP `8.194` edge `0.0141` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.21` n `133` status `ready` deltaP `6.8276` edge `0.0837` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0789` n `133` status `ready` deltaP `3.9789` edge `0.0233` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.0592` n `133` status `ready` deltaP `5.3988` edge `0.0283` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0379` n `133` status `ready` deltaP `4.8963` edge `0.0101` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2718` n `133` status `ready` deltaP `10.4056` edge `0.0416` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8926` n `133` status `ready` deltaP `1.1177` edge `0.0185` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.2111` n `132` status `ready` deltaP `7.428` edge `0.0079` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4761` n `133` status `ready` deltaP `-3.8559` edge `-0.0007` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6296` n `133` status `ready` deltaP `-0.0814` edge `0.0702` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.0482` n `132` status `ready` deltaP `-13.9241` edge `0.0405` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3279` n `133` status `ready` deltaP `-2.0226` edge `-0.1215` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
