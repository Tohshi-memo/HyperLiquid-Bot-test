# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T14:27:32.005641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8424`

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

- `market_context_high->unknown_4h` score `39.931` n `149` status `ready` deltaP `-0.4634` edge `3.354` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8097` n `52` status `ready` deltaP `-7.704` edge `1.2247` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8097` n `52` status `ready` deltaP `-7.704` edge `1.2247` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.7462` n `52` status `ready` deltaP `49.1319` edge `0.4013` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7462` n `52` status `ready` deltaP `49.1319` edge `0.4013` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.7499` n `32` status `ready` deltaP `23.0903` edge `0.6298` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.447` n `149` status `ready` deltaP `42.4205` edge `0.3903` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2989` n `95` status `ready` deltaP `21.6447` edge `0.4937` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7931` n `52` status `ready` deltaP `32.5399` edge `0.0508` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7931` n `52` status `ready` deltaP `32.5399` edge `0.0508` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6928` n `149` status `ready` deltaP `29.0422` edge `0.0726` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0618` n `149` status `ready` deltaP `15.7618` edge `0.0211` maxDD `-0.3491`
- `news_risk_high->index_24h` score `0.7018` n `32` status `ready` deltaP `5.9028` edge `0.0383` maxDD `-0.2001`
- `risk_on_high->fx_24h` score `0.6861` n `52` status `ready` deltaP `16.3061` edge `-0.0473` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6861` n `52` status `ready` deltaP `16.3061` edge `-0.0473` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6612` n `95` status `ready` deltaP `12.2288` edge `0.0974` maxDD `-4.1995`
- `market_context_high->fx_24h` score `0.5512` n `149` status `ready` deltaP `13.5312` edge `-0.0227` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.5214` n `95` status `ready` deltaP `13.7099` edge `0.3001` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4385` n `52` status `ready` deltaP `8.8439` edge `0.0128` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4385` n `52` status `ready` deltaP `8.8439` edge `0.0128` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
