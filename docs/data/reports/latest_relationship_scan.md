# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T13:52:24.969561+00:00`
- Price records: `672`
- Market context records: `5668`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `2.1623` n `194` status `ready` deltaP `15.8075` edge `0.5827` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9021` n `244` status `ready` deltaP `11.4854` edge `0.2266` maxDD `-13.9064`
- `market_context_high->crypto_alt_4h` score `0.3926` n `244` status `ready` deltaP `8.5315` edge `0.1601` maxDD `-9.4072`
- `market_context_high->equity_4h` score `0.3848` n `244` status `ready` deltaP `6.9497` edge `0.1496` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2566` n `256` status `ready` deltaP `2.0444` edge `0.0011` maxDD `-0.4764`
- `market_context_high->fx_24h` score `-0.2567` n `194` status `ready` deltaP `16.6953` edge `0.0514` maxDD `-2.7278`
- `market_context_high->equity_1h` score `-0.4742` n `256` status `ready` deltaP `4.5261` edge `0.031` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5039` n `256` status `ready` deltaP `0.4818` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5504` n `256` status `ready` deltaP `1.9929` edge `0.037` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.5888` n `256` status `ready` deltaP `0.938` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7501` n `256` status `ready` deltaP `3.5156` edge `0.0386` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8781` n `256` status `ready` deltaP `0.9567` edge `-0.003` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.208` n `244` status `ready` deltaP `3.2787` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2684` n `244` status `ready` deltaP `-0.6372` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.447` n `194` status `ready` deltaP `7.3149` edge `0.0362` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.946` n `244` status `ready` deltaP `-12.9049` edge `-0.0541` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.6686` n `244` status `ready` deltaP `-0.9846` edge `-0.0316` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.607` n `194` status `ready` deltaP `4.0771` edge `0.0346` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3779` n `194` status `ready` deltaP `-13.2553` edge `-0.2507` maxDD `-32.8014`
- `market_context_high->commodity_24h` score `-12.3662` n `194` status `ready` deltaP `-11.8235` edge `-0.0908` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
