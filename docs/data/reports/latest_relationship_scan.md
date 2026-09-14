# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T06:07:34.016448+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11520`

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

- `news_risk_high->unknown_1h` score `443.5709` n `82` status `ready` deltaP `-5.999` edge `37.0464` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.9067` n `82` status `ready` deltaP `39.8234` edge `1.4422` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0172` n `82` status `ready` deltaP `36.9891` edge `1.4019` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.8088` n `82` status `ready` deltaP `35.2019` edge `0.9274` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.1612` n `82` status `ready` deltaP `58.9739` edge `0.3046` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7598` n `75` status `ready` deltaP `39.8276` edge `0.2978` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.245` n `41` status `ready` deltaP `39.8276` edge `0.2549` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.245` n `41` status `ready` deltaP `39.8276` edge `0.2549` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.5683` n `82` status `ready` deltaP `33.381` edge `0.2869` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.3688` n `41` status `ready` deltaP `59.63` edge `0.0541` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.3688` n `41` status `ready` deltaP `59.63` edge `0.0541` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7362` n `75` status `ready` deltaP `54.069` edge `0.0558` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9987` n `52` status `ready` deltaP `26.8996` edge `0.0222` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9987` n `52` status `ready` deltaP `26.8996` edge `0.0222` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.799` n `137` status `ready` deltaP `22.3095` edge `0.043` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.779` n `137` status `ready` deltaP `12.9617` edge `0.0162` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6109` n `82` status `ready` deltaP `15.5488` edge `0.0375` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3309` n `137` status `ready` deltaP `11.9881` edge `0.0101` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2635` n `52` status `ready` deltaP `7.3469` edge `0.0082` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2635` n `52` status `ready` deltaP `7.3469` edge `0.0082` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
