# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T18:52:32.447452+00:00`
- Price records: `672`
- Market context records: `4961`
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

- `market_context_high->unknown_1h` score `19.0868` n `96` status `ready` deltaP `8.7637` edge `1.5739` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1105` n `94` status `ready` deltaP `28.7137` edge `0.8692` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2757` n `94` status `ready` deltaP `21.5879` edge `0.5848` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0152` n `94` status `ready` deltaP `22.0388` edge `0.5729` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7624` n `91` status `ready` deltaP `26.7991` edge `0.3358` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7009` n `94` status `ready` deltaP `13.979` edge `0.1867` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5241` n `94` status `ready` deltaP `12.1757` edge `0.1204` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.4067` n `96` status `ready` deltaP `9.1005` edge `0.1604` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0609` n `96` status `ready` deltaP `9.9676` edge `0.0793` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.924` n `94` status `ready` deltaP `11.8611` edge `0.0441` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.6993` n `96` status `ready` deltaP `9.6744` edge `0.1274` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.2633` n `96` status `ready` deltaP `6.4246` edge `0.0371` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3244` n `96` status `ready` deltaP `3.1188` edge `0.0131` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.3924` n `96` status `ready` deltaP `1.2101` edge `0.0076` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0403` n `94` status `ready` deltaP `6.5613` edge `-0.0059` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1239` n `94` status `ready` deltaP `-6.383` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.5083` n `91` status `ready` deltaP `-1.8238` edge `-0.0125` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5469` n `96` status `ready` deltaP `-9.6495` edge `-0.0046` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9995` n `91` status `ready` deltaP `19.6485` edge `0.0466` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9458` n `91` status `ready` deltaP `-9.5143` edge `0.0301` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
