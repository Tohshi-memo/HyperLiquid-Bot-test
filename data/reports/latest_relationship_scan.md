# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T14:37:31.720021+00:00`
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

- `market_context_high->unknown_4h` score `39.9154` n `149` status `ready` deltaP `-0.4634` edge `3.3527` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7941` n `52` status `ready` deltaP `-7.704` edge `1.2234` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7941` n `52` status `ready` deltaP `-7.704` edge `1.2234` maxDD `-0.4694`
- `news_risk_high->crypto_alt_24h` score `9.3813` n `33` status `ready` deltaP `23.8479` edge `0.7607` maxDD `-9.3661`
- `risk_on_high->commodity_24h` score `8.7414` n `52` status `ready` deltaP `49.1319` edge `0.4009` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7414` n `52` status `ready` deltaP `49.1319` edge `0.4009` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4422` n `149` status `ready` deltaP `42.4205` edge `0.3899` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.3082` n `95` status `ready` deltaP `21.6447` edge `0.4949` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7871` n `52` status `ready` deltaP `32.5399` edge `0.0503` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7871` n `52` status `ready` deltaP `32.5399` edge `0.0503` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6868` n `149` status `ready` deltaP `29.0422` edge `0.0721` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0654` n `149` status `ready` deltaP `15.7618` edge `0.0214` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6831` n `95` status `ready` deltaP `12.3812` edge `0.0992` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6813` n `52` status `ready` deltaP `16.3061` edge `-0.0477` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6813` n `52` status `ready` deltaP `16.3061` edge `-0.0477` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.5464` n `149` status `ready` deltaP `13.5312` edge `-0.0231` maxDD `-0.0593`
- `news_risk_high->crypto_major_24h` score `0.5318` n `33` status `ready` deltaP `-13.3839` edge `0.3569` maxDD `-13.2931`
- `news_risk_high->crypto_major_4h` score `0.5121` n `95` status `ready` deltaP `13.7099` edge `0.2989` maxDD `-19.972`
- `news_risk_high->index_24h` score `0.4728` n `33` status `ready` deltaP `4.4666` edge `0.0343` maxDD `-0.3072`
- `risk_on_high->commodity_1h` score `0.4421` n `52` status `ready` deltaP `8.8439` edge `0.0131` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
