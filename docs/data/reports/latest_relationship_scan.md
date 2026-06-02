# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T11:22:26.960452+00:00`
- Price records: `672`
- Market context records: `2657`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->unknown_24h` score `8.0619` n `120` status `ready` deltaP `17.257` edge `0.5896` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.5076` n `120` status `ready` deltaP `12.6736` edge `0.8905` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `5.1536` n `121` status `ready` deltaP `25.1499` edge `0.5297` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7627` n `121` status `ready` deltaP `15.2489` edge `0.3929` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8696` n `121` status `ready` deltaP `9.416` edge `0.198` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1237` n `133` status `ready` deltaP `9.7013` edge `0.1477` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6307` n `133` status `ready` deltaP `8.0512` edge `0.1183` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.4953` n `120` status `ready` deltaP `9.757` edge `0.0743` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `0.0913` n `133` status `ready` deltaP `3.5467` edge `0.0419` maxDD `-1.9684`
- `market_context_high->metal_4h` score `-0.0394` n `121` status `ready` deltaP `6.2463` edge `0.0367` maxDD `-2.5301`
- `market_context_high->index_4h` score `-0.0439` n `121` status `ready` deltaP `7.4985` edge `0.0305` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.2405` n `133` status `ready` deltaP `2.6485` edge `0.0117` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4061` n `133` status `ready` deltaP `3.5298` edge `0.0039` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.418` n `120` status `ready` deltaP `7.7778` edge `0.0005` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.5532` n `133` status `ready` deltaP `-0.6787` edge `0.003` maxDD `-1.8854`
- `market_context_high->fx_1h` score `-0.6144` n `133` status `ready` deltaP `-1.4205` edge `0.0029` maxDD `-0.2373`
- `market_context_high->fx_4h` score `-0.6998` n `121` status `ready` deltaP `-0.6778` edge `0.0117` maxDD `-0.573`
- `market_context_high->commodity_4h` score `-1.0901` n `121` status `ready` deltaP `4.6739` edge `0.0211` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2243` n `133` status `ready` deltaP `-4.3908` edge `0.0111` maxDD `-2.7085`
- `market_context_high->equity_24h` score `-1.4742` n `120` status `ready` deltaP `6.8403` edge `-0.0707` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
