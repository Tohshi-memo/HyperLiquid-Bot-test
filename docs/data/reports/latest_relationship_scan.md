# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T23:22:29.223820+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `risk_on_high->crypto_alt_4h` score `7.6853` n `48` status `ready` deltaP `26.9309` edge `0.4874` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `7.6853` n `48` status `ready` deltaP `26.9309` edge `0.4874` maxDD `-0.4529`
- `risk_on_high->crypto_major_4h` score `6.2446` n `48` status `ready` deltaP `32.3679` edge `0.3322` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.2446` n `48` status `ready` deltaP `32.3679` edge `0.3322` maxDD `-1.208`
- `news_risk_high->crypto_alt_24h` score `6.1135` n `43` status `ready` deltaP `20.3933` edge `0.9854` maxDD `-22.3391`
- `news_risk_high->unknown_4h` score `5.6148` n `52` status `ready` deltaP `-0.8091` edge `0.5323` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6814` n `104` status `ready` deltaP `34.415` edge `0.2626` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.2413` n `52` status `ready` deltaP `-5.0092` edge `0.3392` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.117` n `48` status `ready` deltaP `35.061` edge `0.0346` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.117` n `48` status `ready` deltaP `35.061` edge `0.0346` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.3157` n `48` status `ready` deltaP `18.496` edge `0.0946` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.3157` n `48` status `ready` deltaP `18.496` edge `0.0946` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8506` n `150` status `ready` deltaP `18.3191` edge `0.0791` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.4246` n `162` status `ready` deltaP `8.3574` edge `0.1111` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.4087` n `48` status `ready` deltaP `20.7317` edge `0.0101` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.4087` n `48` status `ready` deltaP `20.7317` edge `0.0101` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1828` n `60` status `ready` deltaP `16.8563` edge `0.0076` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1828` n `60` status `ready` deltaP `16.8563` edge `0.0076` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.145` n `52` status `ready` deltaP `28.1895` edge `0.0138` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.7402` n `60` status `ready` deltaP `0.8883` edge `0.0997` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
