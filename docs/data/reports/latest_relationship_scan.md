# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T23:37:24.515377+00:00`
- Price records: `672`
- Market context records: `3327`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `63.5829` n `30` status `ready` deltaP `67.3611` edge `4.8495` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `63.5829` n `30` status `ready` deltaP `67.3611` edge `4.8495` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `58.651` n `30` status `ready` deltaP `61.6319` edge `4.4767` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `58.651` n `30` status `ready` deltaP `61.6319` edge `4.4767` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.9257` n `30` status `ready` deltaP `56.7708` edge `3.532` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.9257` n `30` status `ready` deltaP `56.7708` edge `3.532` maxDD `0.0`
- `risk_on_high->index_24h` score `23.0228` n `30` status `ready` deltaP `50.6944` edge `1.5806` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.0228` n `30` status `ready` deltaP `50.6944` edge `1.5806` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.3993` n `30` status `ready` deltaP `37.0139` edge `1.1415` maxDD `-0.3988`
- `risk_on_and_context->metal_24h` score `16.3993` n `30` status `ready` deltaP `37.0139` edge `1.1415` maxDD `-0.3988`
- `risk_on_high->crypto_major_4h` score `15.8363` n `32` status `ready` deltaP `30.1829` edge `1.2307` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8363` n `32` status `ready` deltaP `30.1829` edge `1.2307` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.1727` n `142` status `ready` deltaP `22.8995` edge `2.7767` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.3776` n `142` status `ready` deltaP `34.4972` edge `0.9736` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.0407` n `142` status `ready` deltaP `27.8976` edge `1.9429` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2776` n `32` status `ready` deltaP `9.2226` edge `0.7294` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2776` n `32` status `ready` deltaP `9.2226` edge `0.7294` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4998` n `32` status `ready` deltaP `13.4909` edge `0.4722` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.4998` n `32` status `ready` deltaP `13.4909` edge `0.4722` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.399` n `142` status `ready` deltaP `24.4034` edge `2.343` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
