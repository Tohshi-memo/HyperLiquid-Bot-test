# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T19:07:26.348864+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10313`

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

- `risk_on_high->unknown_24h` score `233.0889` n `103` status `ready` deltaP `25.2124` edge `19.2659` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `233.0889` n `103` status `ready` deltaP `25.2124` edge `19.2659` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `19.5286` n `103` status `ready` deltaP `32.376` edge `1.4851` maxDD `-4.2182`
- `risk_on_and_context->crypto_major_24h` score `19.5286` n `103` status `ready` deltaP `32.376` edge `1.4851` maxDD `-4.2182`
- `risk_on_high->crypto_alt_24h` score `10.9393` n `103` status `ready` deltaP `23.3802` edge `0.8577` maxDD `-5.4903`
- `risk_on_and_context->crypto_alt_24h` score `10.9393` n `103` status `ready` deltaP `23.3802` edge `0.8577` maxDD `-5.4903`
- `market_context_high->crypto_alt_24h` score `6.6048` n `196` status `ready` deltaP `19.8732` edge `0.5452` maxDD `-6.8498`
- `market_context_high->equity_24h` score `6.0822` n `196` status `ready` deltaP `21.4073` edge `0.3984` maxDD `-1.0747`
- `risk_on_high->equity_24h` score `5.0507` n `103` status `ready` deltaP `19.1039` edge `0.3278` maxDD `-1.0747`
- `risk_on_and_context->equity_24h` score `5.0507` n `103` status `ready` deltaP `19.1039` edge `0.3278` maxDD `-1.0747`
- `risk_on_high->index_24h` score `1.6001` n `103` status `ready` deltaP `17.8955` edge `0.0736` maxDD `-1.4313`
- `risk_on_and_context->index_24h` score `1.6001` n `103` status `ready` deltaP `17.8955` edge `0.0736` maxDD `-1.4313`
- `market_context_high->index_24h` score `1.4913` n `196` status `ready` deltaP `18.9307` edge `0.089` maxDD `-1.9408`
- `risk_on_high->metal_24h` score `0.5382` n `103` status `ready` deltaP `14.7013` edge `0.0842` maxDD `-4.9889`
- `risk_on_and_context->metal_24h` score `0.5382` n `103` status `ready` deltaP `14.7013` edge `0.0842` maxDD `-4.9889`
- `risk_on_high->crypto_alt_4h` score `0.2892` n `118` status `ready` deltaP `23.8916` edge `0.1851` maxDD `-22.2889`
- `risk_on_and_context->crypto_alt_4h` score `0.2892` n `118` status `ready` deltaP `23.8916` edge `0.1851` maxDD `-22.2889`
- `risk_on_high->crypto_alt_1h` score `0.233` n `129` status `ready` deltaP `3.8516` edge `0.0678` maxDD `-4.2582`
- `risk_on_and_context->crypto_alt_1h` score `0.233` n `129` status `ready` deltaP `3.8516` edge `0.0678` maxDD `-4.2582`
- `risk_on_high->index_1h` score `0.1071` n `129` status `ready` deltaP `9.1712` edge `-0.0027` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
