# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T14:37:25.178181+00:00`
- Price records: `672`
- Market context records: `4943`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9456`

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

- `market_context_high->unknown_1h` score `19.6115` n `95` status `ready` deltaP `10.9124` edge `1.6033` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.199` n `94` status `ready` deltaP `28.2596` edge `0.8796` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2969` n `94` status `ready` deltaP `21.1339` edge `0.5896` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0535` n `94` status `ready` deltaP `21.7372` edge `0.5781` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8655` n `88` status `ready` deltaP `26.7519` edge `0.3447` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7918` n `94` status `ready` deltaP `14.8903` edge `0.1882` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6633` n `94` status `ready` deltaP `12.7854` edge `0.1196` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9859` n `94` status `ready` deltaP `12.62` edge `0.0442` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.7696` n `95` status `ready` deltaP `7.7261` edge `0.151` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.5817` n `95` status `ready` deltaP `8.6432` edge `0.1192` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.5491` n `95` status `ready` deltaP `7.5953` edge `0.0771` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.094` n `95` status `ready` deltaP `4.4138` edge `0.0364` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3597` n `95` status `ready` deltaP `1.8689` edge `0.0074` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4652` n `95` status `ready` deltaP `0.531` edge `0.0123` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9543` n `94` status `ready` deltaP `6.5613` edge `-0.0046` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1294` n `94` status `ready` deltaP `-6.5322` edge `-0.0042` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.5367` n `88` status `ready` deltaP `-1.9097` edge `-0.0143` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.605` n `95` status `ready` deltaP `-10.0189` edge `-0.0057` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-4.4001` n `88` status `ready` deltaP `17.8503` edge `0.0252` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0227` n `88` status `ready` deltaP `-9.1856` edge `0.0215` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
