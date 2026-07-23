# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T19:52:28.271136+00:00`
- Price records: `672`
- Market context records: `7701`
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

- `market_context_high->equity_24h` score `3.6399` n `132` status `ready` deltaP `19.396` edge `0.3082` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.3488` n `133` status `ready` deltaP `15.8708` edge `0.1784` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1353` n `133` status `ready` deltaP `13.4573` edge `0.049` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8605` n `133` status `ready` deltaP `8.8093` edge `0.1247` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.8489` n `133` status `ready` deltaP `3.4984` edge `0.2768` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6951` n `133` status `ready` deltaP `8.7968` edge `0.0852` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3902` n `133` status `ready` deltaP `8.9447` edge `0.0159` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1677` n `133` status `ready` deltaP `3.6795` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0813` n `132` status `ready` deltaP `11.4217` edge `0.0222` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1042` n `133` status `ready` deltaP `12.6992` edge `0.0478` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.2181` n `133` status `ready` deltaP `3.2446` edge `0.0061` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.3383` n `133` status `ready` deltaP `2.7994` edge `0.0125` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4939` n `133` status `ready` deltaP `-0.2269` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.6389` n `133` status `ready` deltaP `2.8548` edge `0.1368` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8123` n `133` status `ready` deltaP `1.8662` edge `0.0202` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2542` n `133` status `ready` deltaP `-0.2262` edge `-0.044` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4223` n `133` status `ready` deltaP `1.5954` edge `0.0763` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5536` n `133` status `ready` deltaP `-4.9263` edge `-0.0035` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7225` n `132` status `ready` deltaP `5.6858` edge `-0.0231` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2495` n `133` status `ready` deltaP `15.3023` edge `-0.1638` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
