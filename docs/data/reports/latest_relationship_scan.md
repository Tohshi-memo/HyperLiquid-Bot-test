# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T20:52:30.365130+00:00`
- Price records: `672`
- Market context records: `7706`
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

- `market_context_high->equity_24h` score `3.6219` n `132` status `ready` deltaP `19.396` edge `0.3067` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.262` n `133` status `ready` deltaP `15.5659` edge `0.1732` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0718` n `133` status `ready` deltaP `13.0082` edge `0.0467` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8137` n `133` status `ready` deltaP `8.8093` edge `0.1208` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.7923` n `133` status `ready` deltaP `3.0397` edge `0.2726` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6374` n `133` status `ready` deltaP `8.6466` edge `0.0814` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3842` n `133` status `ready` deltaP `8.9447` edge `0.0154` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1198` n `133` status `ready` deltaP `3.3801` edge `0.0307` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0357` n `132` status `ready` deltaP `12.1186` edge `0.0234` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1232` n `133` status `ready` deltaP `12.3934` edge `0.0474` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.1916` n `133` status `ready` deltaP `3.5449` edge `0.0063` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.275` n `133` status `ready` deltaP `3.411` edge `0.0137` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5432` n `133` status `ready` deltaP `-0.8275` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.5638` n `133` status `ready` deltaP `3.0284` edge `0.1419` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8531` n `133` status `ready` deltaP `1.4171` edge `0.0198` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.3261` n `133` status `ready` deltaP `-0.6753` edge `-0.047` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4113` n `133` status `ready` deltaP `1.7479` edge `0.0762` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5782` n `133` status `ready` deltaP `-5.385` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7417` n `132` status `ready` deltaP `5.6858` edge `-0.0247` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2531` n `133` status `ready` deltaP `15.3023` edge `-0.1641` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
