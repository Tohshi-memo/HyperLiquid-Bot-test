# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T09:37:27.005349+00:00`
- Price records: `672`
- Market context records: `7656`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0508` n `146` status `ready` deltaP `6.512` edge `0.011` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.2017` n `146` status `ready` deltaP `7.7065` edge `0.0188` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2996` n `146` status `ready` deltaP `1.3063` edge `0.0161` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3551` n `145` status `ready` deltaP `9.2803` edge `0.0173` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4162` n `146` status `ready` deltaP `1.2279` edge `-0.0045` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5431` n `146` status `ready` deltaP `5.0764` edge `0.0479` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6395` n `146` status `ready` deltaP `1.0889` edge `0.0153` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7104` n `146` status `ready` deltaP `1.6066` edge `0.0046` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7245` n `146` status `ready` deltaP `7.6871` edge `0.026` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.9524` n `145` status `ready` deltaP `8.187` edge `0.0244` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.1253` n `146` status `ready` deltaP `1.8251` edge `0.0425` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1939` n `146` status `ready` deltaP `9.2841` edge `0.0528` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5026` n `146` status `ready` deltaP `-0.9843` edge `-0.0563` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7045` n `146` status `ready` deltaP `-2.7376` edge `0.0454` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.7316` n `146` status `ready` deltaP `0.6849` edge `0.1878` maxDD `-20.4824`
- `market_context_high->equity_24h` score `-1.7526` n `145` status `ready` deltaP `13.8412` edge `0.1736` maxDD `-34.5784`
- `market_context_high->metal_24h` score `-2.2512` n `146` status `ready` deltaP `-3.2772` edge `0.0589` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7669` n `146` status `ready` deltaP `-8.4936` edge `-0.0055` maxDD `-2.1425`
- `market_context_high->unknown_24h` score `-3.2816` n `146` status `ready` deltaP `5.1085` edge `-0.1895` maxDD `-4.775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
