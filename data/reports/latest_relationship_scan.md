# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T12:52:36.553099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `40.0848` n `149` status `ready` deltaP `-0.311` edge `3.3658` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9635` n `52` status `ready` deltaP `-7.5516` edge `1.2365` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9635` n `52` status `ready` deltaP `-7.5516` edge `1.2365` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8425` n `52` status `ready` deltaP `49.8264` edge `0.4047` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8425` n `52` status `ready` deltaP `49.8264` edge `0.4047` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5434` n `149` status `ready` deltaP `43.115` edge `0.3937` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2114` n `95` status `ready` deltaP `21.4923` edge `0.4835` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7192` n `149` status `ready` deltaP `29.0422` edge `0.0748` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.087` n `149` status `ready` deltaP `15.9115` edge `0.0222` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.7577` n `52` status `ready` deltaP `16.8269` edge `-0.0448` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.7577` n `52` status `ready` deltaP `16.8269` edge `-0.0448` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.6229` n `149` status `ready` deltaP `14.052` edge `-0.0202` maxDD `-0.0593`
- `news_risk_high->equity_4h` score `0.5953` n `95` status `ready` deltaP `11.7715` edge `0.092` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `0.4909` n `95` status `ready` deltaP `13.5574` edge `0.2972` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4637` n `52` status `ready` deltaP `8.9936` edge `0.0139` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4637` n `52` status `ready` deltaP `8.9936` edge `0.0139` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3364` n `95` status `ready` deltaP `10.4396` edge `0.0257` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2449` n `95` status `ready` deltaP `7.7792` edge `0.0242` maxDD `-0.2398`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
