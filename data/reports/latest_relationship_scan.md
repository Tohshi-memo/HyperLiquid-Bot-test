# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T18:07:35.880976+00:00`
- Price records: `672`
- Market context records: `4541`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `55.41` n `173` status `ready` deltaP `7.492` edge `4.6176` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.1729` n `171` status `ready` deltaP `8.3851` edge `2.6151` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4903` n `171` status `ready` deltaP `6.4925` edge `0.0021` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5979` n `173` status `ready` deltaP `0.1765` edge `0.0141` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.6971` n `173` status `ready` deltaP `0.135` edge `-0.0031` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-1.0007` n `171` status `ready` deltaP `3.934` edge `0.0673` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0414` n `173` status `ready` deltaP `-3.2623` edge `-0.0109` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0656` n `173` status `ready` deltaP `-1.5904` edge `0.0205` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.1576` n `171` status `ready` deltaP `-0.0347` edge `-0.0109` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.4732` n `171` status `ready` deltaP `1.5066` edge `0.0197` maxDD `-9.8229`
- `market_context_high->unknown_24h` score `-2.7194` n `171` status `ready` deltaP `2.3574` edge `-0.15` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4404` n `173` status `ready` deltaP `-4.2937` edge `-0.0735` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.281` n `173` status `ready` deltaP `-2.6635` edge `-0.0936` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4801` n `171` status `ready` deltaP `-13.4321` edge `-0.0159` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6921` n `171` status `ready` deltaP `-8.6805` edge `-0.1344` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2472` n `173` status `ready` deltaP `-4.2479` edge `-0.117` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.4249` n `171` status `ready` deltaP `3.9748` edge `0.0122` maxDD `-46.5954`
- `market_context_high->crypto_alt_4h` score `-13.2806` n `171` status `ready` deltaP `-1.6644` edge `-0.2299` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4912` n `171` status `ready` deltaP `-0.8223` edge `-0.2562` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5612` n `171` status `ready` deltaP `-7.2849` edge `-0.3133` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
