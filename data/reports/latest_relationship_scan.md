# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T13:07:30.708995+00:00`
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

- `market_context_high->unknown_4h` score `40.0824` n `149` status `ready` deltaP `-0.311` edge `3.3656` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9611` n `52` status `ready` deltaP `-7.5516` edge `1.2363` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9611` n `52` status `ready` deltaP `-7.5516` edge `1.2363` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8202` n `52` status `ready` deltaP `49.6528` edge `0.404` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8202` n `52` status `ready` deltaP `49.6528` edge `0.404` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5211` n `149` status `ready` deltaP `42.9414` edge `0.393` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2552` n `95` status `ready` deltaP `21.6447` edge `0.4881` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8147` n `52` status `ready` deltaP `32.5399` edge `0.0526` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8147` n `52` status `ready` deltaP `32.5399` edge `0.0526` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7144` n `149` status `ready` deltaP `29.0422` edge `0.0744` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0702` n `149` status `ready` deltaP `15.7618` edge `0.0218` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.7379` n `52` status `ready` deltaP `16.6533` edge `-0.0453` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.7379` n `52` status `ready` deltaP `16.6533` edge `-0.0453` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6196` n `95` status `ready` deltaP `11.9239` edge `0.0941` maxDD `-4.1995`
- `market_context_high->fx_24h` score `0.603` n `149` status `ready` deltaP `13.8784` edge `-0.0207` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.5347` n `95` status `ready` deltaP `13.7099` edge `0.3018` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4469` n `52` status `ready` deltaP `8.8439` edge `0.0135` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4469` n `52` status `ready` deltaP `8.8439` edge `0.0135` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3551` n `95` status `ready` deltaP `10.5893` edge `0.0271` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2449` n `95` status `ready` deltaP `7.7792` edge `0.0242` maxDD `-0.2398`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
