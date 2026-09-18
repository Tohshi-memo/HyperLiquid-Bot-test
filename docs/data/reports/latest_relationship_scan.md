# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T13:37:35.067848+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8420`

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

- `market_context_high->unknown_4h` score `39.979` n `149` status `ready` deltaP `-0.4634` edge `3.358` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8577` n `52` status `ready` deltaP `-7.704` edge `1.2287` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8577` n `52` status `ready` deltaP `-7.704` edge `1.2287` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.7931` n `52` status `ready` deltaP `49.4792` edge `0.4029` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7931` n `52` status `ready` deltaP `49.4792` edge `0.4029` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.494` n `149` status `ready` deltaP `42.7678` edge `0.3919` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2887` n `95` status `ready` deltaP `21.6447` edge `0.4924` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8075` n `52` status `ready` deltaP `32.5399` edge `0.052` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8075` n `52` status `ready` deltaP `32.5399` edge `0.052` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7072` n `149` status `ready` deltaP `29.0422` edge `0.0738` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0666` n `149` status `ready` deltaP `15.7618` edge `0.0215` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.6993` n `52` status `ready` deltaP `16.3061` edge `-0.0462` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6993` n `52` status `ready` deltaP `16.3061` edge `-0.0462` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6495` n `95` status `ready` deltaP `12.2288` edge `0.0959` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `0.5651` n `95` status `ready` deltaP `13.7099` edge `0.3057` maxDD `-19.972`
- `market_context_high->fx_24h` score `0.5644` n `149` status `ready` deltaP `13.5312` edge `-0.0216` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4433` n `52` status `ready` deltaP `8.8439` edge `0.0132` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4433` n `52` status `ready` deltaP `8.8439` edge `0.0132` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3481` n `95` status `ready` deltaP `10.4396` edge `0.0272` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2449` n `95` status `ready` deltaP `7.7792` edge `0.0242` maxDD `-0.2398`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
