# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T08:07:38.712863+00:00`
- Price records: `672`
- Market context records: `8496`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6272.5277` n `52` status `ready` deltaP `44.0438` edge `522.4591` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0692` n `64` status `ready` deltaP `22.1799` edge `0.4176` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0363` n `64` status `ready` deltaP `16.8064` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7506` n `64` status `ready` deltaP `15.9525` edge `0.0872` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `0.9813` n `64` status `ready` deltaP `14.939` edge `0.1654` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9657` n `64` status `ready` deltaP `5.8308` edge `0.1625` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.63` n `64` status `ready` deltaP `10.2077` edge `0.0654` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.4038` n `64` status `ready` deltaP `7.5131` edge `0.0529` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1687` n `64` status `ready` deltaP `6.7833` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0706` n `64` status `ready` deltaP `12.0808` edge `0.0211` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0138` n `64` status `ready` deltaP `3.7706` edge `0.0083` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1368` n `64` status `ready` deltaP `0.1905` edge `0.0288` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2066` n `64` status `ready` deltaP `2.5075` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.6327` n `64` status `ready` deltaP `-3.7051` edge `-0.0328` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5309` n `52` status `ready` deltaP `-27.7244` edge `-0.0439` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.6197` n `64` status `ready` deltaP `-20.3125` edge `-0.1668` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.4599` n `52` status `ready` deltaP `-36.7922` edge `-0.266` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9234` n `52` status `ready` deltaP `-13.3013` edge `-0.3943` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.1829` n `52` status `ready` deltaP `-38.141` edge `-0.4607` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.4275` n `52` status `ready` deltaP `-33.4802` edge `-1.7766` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
