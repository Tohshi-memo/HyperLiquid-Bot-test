# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T16:22:29.579876+00:00`
- Price records: `672`
- Market context records: `4950`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9472`

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

- `market_context_high->unknown_1h` score `19.5237` n `95` status `ready` deltaP `10.0095` edge `1.602` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.4214` n `92` status `ready` deltaP `28.6254` edge `0.8957` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3576` n `92` status `ready` deltaP `21.5469` edge `0.5919` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1394` n `92` status `ready` deltaP `22.1964` edge `0.5822` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.793` n `92` status `ready` deltaP `27.1966` edge `0.3357` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8512` n `92` status `ready` deltaP `15.2572` edge `0.1907` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.7206` n `92` status `ready` deltaP `13.0965` edge `0.1223` maxDD `-1.9651`
- `market_context_high->index_4h` score `1.0376` n `92` status `ready` deltaP `13.176` edge `0.0448` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.9325` n `95` status `ready` deltaP `8.4983` edge `0.0784` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9135` n `95` status `ready` deltaP `9.2326` edge `0.1594` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.7053` n `95` status `ready` deltaP `10.0` edge `0.126` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1364` n `95` status `ready` deltaP `4.8676` edge `0.0369` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3825` n `95` status `ready` deltaP `1.4151` edge `0.0075` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.383` n `95` status `ready` deltaP `2.0375` edge `0.0128` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.904` n `92` status `ready` deltaP `7.1447` edge `-0.0043` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1488` n `92` status `ready` deltaP `-6.8465` edge `-0.0046` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3227` n `92` status `ready` deltaP `0.0906` edge `-0.0098` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5918` n `95` status `ready` deltaP `-9.8692` edge `-0.0056` maxDD `-0.5673`
- `market_context_high->commodity_24h` score `-3.8996` n `92` status `ready` deltaP `20.2219` edge `0.0511` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8884` n `92` status `ready` deltaP `-9.2618` edge `0.0332` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
