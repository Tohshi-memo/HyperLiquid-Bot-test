# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T00:07:29.909789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `7.3057` n `117` status `ready` deltaP `17.6092` edge `0.6363` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.5819` n `117` status `ready` deltaP `22.4096` edge `0.555` maxDD `-7.4722`
- `risk_on_high->commodity_24h` score `6.394` n `52` status `ready` deltaP `32.0` edge `0.3195` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.394` n `52` status `ready` deltaP `32.0` edge `0.3195` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.8946` n `54` status `ready` deltaP `19.8884` edge `0.4034` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.8946` n `54` status `ready` deltaP `19.8884` edge `0.4034` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.818` n `54` status `ready` deltaP `35.515` edge `0.4662` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.818` n `54` status `ready` deltaP `35.515` edge `0.4662` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2333` n `117` status `ready` deltaP `-3.7934` edge `0.4427` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0349` n `117` status `ready` deltaP `14.9138` edge `0.1769` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5151` n `117` status `ready` deltaP `7.7576` edge `0.1551` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3842` n `117` status `ready` deltaP `14.7524` edge `0.0382` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1716` n `54` status `ready` deltaP `3.1992` edge `0.0289` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1716` n `54` status `ready` deltaP `3.1992` edge `0.0289` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.2823` n `117` status `ready` deltaP `8.3129` edge `0.008` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3167` n `117` status `ready` deltaP `1.3976` edge `0.0023` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.3979` n `54` status `ready` deltaP `2.8998` edge `0.0028` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3979` n `54` status `ready` deltaP `2.8998` edge `0.0028` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4106` n `54` status `ready` deltaP `4.6574` edge `0.0189` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4106` n `54` status `ready` deltaP `4.6574` edge `0.0189` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
