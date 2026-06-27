# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T13:37:28.904045+00:00`
- Price records: `672`
- Market context records: `4938`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9408`

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

- `market_context_high->unknown_1h` score `19.3991` n `96` status `ready` deltaP `12.1881` edge `1.5771` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.0245` n `96` status `ready` deltaP `28.6585` edge `0.8624` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3405` n `96` status `ready` deltaP `21.7988` edge `0.5888` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1739` n `96` status `ready` deltaP `22.3577` edge `0.584` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.988` n `86` status `ready` deltaP `26.5141` edge `0.3565` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8474` n `96` status `ready` deltaP `15.5996` edge `0.1881` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5941` n `96` status `ready` deltaP `12.2205` edge `0.1176` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.3486` n `96` status `ready` deltaP `8.2086` edge `0.1615` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `1.0537` n `96` status `ready` deltaP `9.0818` edge `0.1295` maxDD `-5.5126`
- `market_context_high->index_4h` score `1.0211` n `96` status `ready` deltaP `13.1351` edge `0.0437` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.9194` n `96` status `ready` deltaP `8.0339` edge `0.0804` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.1422` n `96` status `ready` deltaP `4.9401` edge `0.0369` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3996` n `96` status `ready` deltaP `1.7777` edge `0.0124` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4282` n `96` status `ready` deltaP `0.9107` edge `0.005` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.9829` n `96` status `ready` deltaP `6.1738` edge `-0.0044` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.0673` n `96` status `ready` deltaP `-5.4878` edge `-0.0032` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4849` n `96` status `ready` deltaP `-8.6078` edge `-0.0051` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.6358` n `86` status `ready` deltaP `-3.0725` edge `-0.0148` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.8733` n `86` status `ready` deltaP `14.9508` edge `0.0051` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.3085` n `86` status `ready` deltaP `-11.2282` edge `0.0113` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
