# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T21:52:29.963294+00:00`
- Price records: `672`
- Market context records: `4976`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `18.5357` n `96` status `ready` deltaP `5.3456` edge `1.5591` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.6179` n `88` status `ready` deltaP `28.4645` edge `0.9143` maxDD `-1.8723`
- `market_context_high->crypto_major_4h` score `7.0479` n `88` status `ready` deltaP `19.041` edge `0.5828` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.5494` n `88` status `ready` deltaP `19.637` edge `0.5501` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8702` n `83` status `ready` deltaP `27.8614` edge `0.3377` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.5314` n `88` status `ready` deltaP `12.5416` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_4h` score `1.0316` n `88` status `ready` deltaP `11.8209` edge `0.1916` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.7392` n `88` status `ready` deltaP `9.3403` edge `0.0455` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.4736` n `96` status `ready` deltaP `6.5494` edge `0.0744` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.2991` n `96` status `ready` deltaP `3.8984` edge `0.1162` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.2408` n `96` status `ready` deltaP `6.1065` edge `0.0924` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.1306` n `96` status `ready` deltaP `1.8151` edge `0.035` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3624` n `96` status `ready` deltaP `1.8026` edge `0.0075` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.469` n `96` status `ready` deltaP `0.4429` edge `0.0124` maxDD `-0.7054`
- `market_context_high->fx_24h` score `-0.8284` n `83` status `ready` deltaP `1.7654` edge `-0.0046` maxDD `-1.7626`
- `market_context_high->fx_4h` score `-1.1269` n `88` status `ready` deltaP `-6.6658` edge `-0.003` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2946` n `88` status `ready` deltaP `4.2267` edge `-0.0108` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7003` n `96` status `ready` deltaP `-11.5831` edge `-0.0045` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.1884` n `83` status `ready` deltaP `14.9118` edge `0.0027` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9499` n `83` status `ready` deltaP `-7.3314` edge `0.0152` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
