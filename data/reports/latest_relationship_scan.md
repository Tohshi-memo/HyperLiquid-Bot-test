# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T15:37:27.014544+00:00`
- Price records: `672`
- Market context records: `7154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.3091` n `154` status `ready` deltaP `12.3991` edge `0.0131` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.231` n `162` status `ready` deltaP `3.5355` edge `0.0023` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.5072` n `162` status `ready` deltaP `-1.3455` edge `0.0309` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5946` n `162` status `ready` deltaP `0.1127` edge `0.0269` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6145` n `162` status `ready` deltaP `3.8349` edge `0.0367` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.687` n `162` status `ready` deltaP `-1.4231` edge `-0.0165` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7156` n `162` status `ready` deltaP `1.6855` edge `-0.0044` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.594` n `162` status `ready` deltaP `-6.5074` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.898` n `154` status `ready` deltaP `-6.2183` edge `0.0139` maxDD `-5.9286`
- `market_context_high->commodity_4h` score `-2.0633` n `154` status `ready` deltaP `-4.5613` edge `-0.038` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9335` n `154` status `ready` deltaP `-10.3857` edge `-0.012` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.509` n `162` status `ready` deltaP `-0.353` edge `-0.0408` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.9339` n `154` status `ready` deltaP `-2.1183` edge `-0.0438` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5036` n `133` status `ready` deltaP `-13.4581` edge `-0.1547` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9446` n `133` status `ready` deltaP `-15.531` edge `-0.0258` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.948` n `154` status `ready` deltaP `2.2806` edge `0.0078` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5471` n `154` status `ready` deltaP `-3.4962` edge `-0.0324` maxDD `-24.5243`
- `market_context_high->unknown_24h` score `-10.1004` n `133` status `ready` deltaP `-32.7029` edge `-0.109` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.6899` n `154` status `ready` deltaP `-4.3772` edge `-0.2221` maxDD `-66.1638`
- `market_context_high->metal_24h` score `-14.7339` n `133` status `ready` deltaP `-31.9496` edge `-0.1967` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
