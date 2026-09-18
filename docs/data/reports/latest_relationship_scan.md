# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T13:22:29.614886+00:00`
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

- `market_context_high->unknown_4h` score `40.074` n `149` status `ready` deltaP `-0.311` edge `3.3649` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9527` n `52` status `ready` deltaP `-7.5516` edge `1.2356` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9527` n `52` status `ready` deltaP `-7.5516` edge `1.2356` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.7991` n `52` status `ready` deltaP `49.4792` edge `0.4034` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7991` n `52` status `ready` deltaP `49.4792` edge `0.4034` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5` n `149` status `ready` deltaP `42.7678` edge `0.3924` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.2841` n `95` status `ready` deltaP `21.6447` edge `0.4918` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8111` n `52` status `ready` deltaP `32.5399` edge `0.0523` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8111` n `52` status `ready` deltaP `32.5399` edge `0.0523` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7108` n `149` status `ready` deltaP `29.0422` edge `0.0741` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.069` n `149` status `ready` deltaP `15.7618` edge `0.0217` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.718` n `52` status `ready` deltaP `16.4797` edge `-0.0458` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.718` n `52` status `ready` deltaP `16.4797` edge `-0.0458` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.6384` n `95` status `ready` deltaP `12.0764` edge `0.0955` maxDD `-4.1995`
- `market_context_high->fx_24h` score `0.5831` n `149` status `ready` deltaP `13.7048` edge `-0.0212` maxDD `-0.0593`
- `news_risk_high->crypto_major_4h` score `0.5612` n `95` status `ready` deltaP `13.7099` edge `0.3052` maxDD `-19.972`
- `risk_on_high->commodity_1h` score `0.4457` n `52` status `ready` deltaP `8.8439` edge `0.0134` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4457` n `52` status `ready` deltaP `8.8439` edge `0.0134` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3613` n `95` status `ready` deltaP `10.5893` edge `0.0279` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2441` n `95` status `ready` deltaP `7.7792` edge `0.0241` maxDD `-0.2398`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
