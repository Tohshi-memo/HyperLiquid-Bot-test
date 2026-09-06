# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T01:52:23.727641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10963`

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

- `risk_on_high->unknown_4h` score `20.946` n `141` status `ready` deltaP `-2.9915` edge `1.966` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.946` n `141` status `ready` deltaP `-2.9915` edge `1.966` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.2776` n `236` status `ready` deltaP `1.1136` edge `0.9292` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.1866` n `37` status `ready` deltaP `23.4422` edge `0.3029` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9151` n `37` status `ready` deltaP `20.1389` edge `0.192` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2827` n `37` status `ready` deltaP `16.2657` edge `0.2064` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.421` n `156` status `ready` deltaP `14.1426` edge `0.4613` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3881` n `37` status `ready` deltaP `24.3037` edge `0.0591` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.562` n `37` status `ready` deltaP `12.7853` edge `0.084` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5344` n `37` status `ready` deltaP `7.313` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3556` n `37` status `ready` deltaP `16.2122` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1874` n `37` status `ready` deltaP `14.873` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0983` n `37` status `ready` deltaP `5.717` edge `0.0717` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.0982` n `37` status `ready` deltaP `21.8656` edge `0.0473` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.9918` n `78` status `ready` deltaP `10.4034` edge `0.7904` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.9918` n `78` status `ready` deltaP `10.4034` edge `0.7904` maxDD `-47.9416`
- `news_risk_high->crypto_alt_1h` score `0.7714` n `37` status `ready` deltaP `8.2781` edge `0.0356` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `-0.0192` n `37` status `ready` deltaP `2.7398` edge `0.013` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0371` n `37` status `ready` deltaP `5.5754` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0998` n `145` status `ready` deltaP `5.2364` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
