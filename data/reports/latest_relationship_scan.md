# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T17:52:30.917861+00:00`
- Price records: `672`
- Market context records: `3505`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13152`

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

- `risk_on_high->crypto_major_24h` score `54.0984` n `32` status `ready` deltaP `57.8802` edge `4.1266` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.0984` n `32` status `ready` deltaP `57.8802` edge `4.1266` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `50.6894` n `32` status `ready` deltaP `57.5336` edge `3.8557` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `50.6894` n `32` status `ready` deltaP `57.5336` edge `3.8557` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.2861` n `32` status `ready` deltaP `54.766` edge `3.3254` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.2861` n `32` status `ready` deltaP `54.766` edge `3.3254` maxDD `0.0`
- `risk_on_high->index_24h` score `24.3207` n `32` status `ready` deltaP `50.4333` edge `1.6905` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.3207` n `32` status `ready` deltaP `50.4333` edge `1.6905` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `18.9028` n `155` status `ready` deltaP `23.5858` edge `2.1911` maxDD `-54.8486`
- `market_context_high->equity_24h` score `18.6986` n `155` status `ready` deltaP `31.5402` edge `1.9892` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `16.7825` n `155` status `ready` deltaP `18.078` edge `2.0781` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.3933` n `32` status `ready` deltaP `32.1815` edge `1.1777` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.3933` n `32` status `ready` deltaP `32.1815` edge `1.1777` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.7928` n `32` status `ready` deltaP `27.6541` edge `1.1606` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.7928` n `32` status `ready` deltaP `27.6541` edge `1.1606` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.9472` n `155` status `ready` deltaP `34.9494` edge `1.0676` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.1312` n `32` status `ready` deltaP `8.8328` edge `0.7198` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1312` n `32` status `ready` deltaP `8.8328` edge `0.7198` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.2291` n `155` status `ready` deltaP `26.6573` edge `1.0749` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8648` n `32` status `ready` deltaP `16.3099` edge `0.5002` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
