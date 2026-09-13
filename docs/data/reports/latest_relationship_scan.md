# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T22:37:27.706936+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `6989.1216` n `56` status `ready` deltaP `10.2093` edge `582.3789` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.9436` n `82` status `ready` deltaP `-5.5499` edge `36.4078` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.8275` n `82` status `ready` deltaP `36.5475` edge `1.3741` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.298` n `82` status `ready` deltaP `38.0236` edge `1.4184` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.1002` n `82` status `ready` deltaP `30.0294` edge `0.8195` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.4594` n `82` status `ready` deltaP `53.8015` edge `0.2806` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.0402` n `56` status `ready` deltaP `39.8276` edge `0.1545` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.9562` n `31` status `ready` deltaP `39.8276` edge `0.1475` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9562` n `31` status `ready` deltaP `39.8276` edge `0.1475` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9313` n `82` status `ready` deltaP `28.2086` edge `0.2683` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `3.2013` n `31` status `ready` deltaP `57.564` edge `0.0432` maxDD `-0.3227`
- `risk_on_and_context->fx_24h` score `3.2013` n `31` status `ready` deltaP `57.564` edge `0.0432` maxDD `-0.3227`
- `risk_on_high->crypto_alt_24h` score `2.7768` n `31` status `ready` deltaP `-1.218` edge `0.3724` maxDD `-6.9638`
- `risk_on_and_context->crypto_alt_24h` score `2.7768` n `31` status `ready` deltaP `-1.218` edge `0.3724` maxDD `-6.9638`
- `market_context_high->crypto_alt_24h` score `2.2273` n `56` status `ready` deltaP `1.835` edge `0.3583` maxDD `-11.1273`
- `risk_on_high->commodity_4h` score `1.7125` n `53` status `ready` deltaP `23.7575` edge `0.0193` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7125` n `53` status `ready` deltaP `23.7575` edge `0.0193` maxDD `-0.1313`
- `market_context_high->fx_24h` score `1.3284` n `56` status `ready` deltaP `36.8843` edge `0.0172` maxDD `-2.0893`
- `market_context_high->commodity_4h` score `1.2983` n `129` status `ready` deltaP `18.9308` edge `0.0238` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4394` n `82` status `ready` deltaP `12.8049` edge `0.0338` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
