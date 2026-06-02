# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T08:22:27.283083+00:00`
- Price records: `672`
- Market context records: `2645`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.6135` n `132` status `ready` deltaP `17.7873` edge `0.5487` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5938` n `132` status `ready` deltaP `25.9423` edge `0.5611` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `4.8979` n `132` status `ready` deltaP `7.6863` edge `0.7893` maxDD `-26.5909`
- `market_context_high->crypto_major_4h` score `4.1503` n `132` status `ready` deltaP `16.8237` edge `0.4147` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.2764` n `132` status `ready` deltaP `7.5665` edge `0.1609` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1262` n `133` status `ready` deltaP `10.3035` edge `0.1439` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.098` n `132` status `ready` deltaP `11.411` edge `0.1135` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.514` n `133` status `ready` deltaP `6.8468` edge `0.1166` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4538` n `132` status `ready` deltaP `10.7354` edge `0.0504` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0274` n `133` status `ready` deltaP `2.9445` edge `0.0368` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.1924` n `133` status `ready` deltaP `3.2507` edge `0.0117` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.2322` n `132` status `ready` deltaP `5.0213` edge `0.0288` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.2704` n `133` status `ready` deltaP `6.5407` edge `0.0217` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4085` n `133` status `ready` deltaP `0.9883` edge `0.004` maxDD `-0.2373`
- `market_context_high->metal_1h` score `-0.4613` n `133` status `ready` deltaP `-0.0765` edge `0.0053` maxDD `-2.114`
- `market_context_high->fx_24h` score `-0.6186` n `132` status `ready` deltaP `5.4767` edge `-0.0002` maxDD `-0.6957`
- `market_context_high->fx_4h` score `-0.9788` n `132` status `ready` deltaP `-1.3765` edge `0.0107` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0294` n `133` status `ready` deltaP `-2.5843` edge `0.0153` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2019` n `132` status `ready` deltaP `3.6262` edge `0.016` maxDD `-10.2078`
- `market_context_high->equity_24h` score `-1.3298` n `132` status `ready` deltaP `8.8858` edge `-0.0723` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
