# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T14:07:34.884094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8386`

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

- `market_context_high->unknown_4h` score `39.949` n `149` status `ready` deltaP `-0.4634` edge `3.3555` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8277` n `52` status `ready` deltaP `-7.704` edge `1.2262` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8277` n `52` status `ready` deltaP `-7.704` edge `1.2262` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.766` n `52` status `ready` deltaP `49.3056` edge `0.4018` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.766` n `52` status `ready` deltaP `49.3056` edge `0.4018` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4669` n `149` status `ready` deltaP `42.5942` edge `0.3908` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `6.009` n `31` status `ready` deltaP `22.2838` edge `0.4901` maxDD `-9.3661`
- `news_risk_high->crypto_alt_4h` score `3.2997` n `95` status `ready` deltaP `21.6447` edge `0.4938` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7991` n `52` status `ready` deltaP `32.5399` edge `0.0513` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7991` n `52` status `ready` deltaP `32.5399` edge `0.0513` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6988` n `149` status `ready` deltaP `29.0422` edge `0.0731` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0606` n `149` status `ready` deltaP `15.7618` edge `0.021` maxDD `-0.3491`
- `news_risk_high->index_24h` score `0.8942` n `31` status `ready` deltaP `7.6165` edge `0.0418` maxDD `-0.1116`
- `risk_on_high->fx_24h` score `0.6909` n `52` status `ready` deltaP `16.3061` edge `-0.0469` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6909` n `52` status `ready` deltaP `16.3061` edge `-0.0469` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6549` n `95` status `ready` deltaP `12.2288` edge `0.0966` maxDD `-4.1995`
- `market_context_high->fx_24h` score `0.556` n `149` status `ready` deltaP `13.5312` edge `-0.0223` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.5386` n `95` status `ready` deltaP `13.7099` edge `0.3023` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4373` n `52` status `ready` deltaP `8.8439` edge `0.0127` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4373` n `52` status `ready` deltaP `8.8439` edge `0.0127` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
