# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T10:52:25.880390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0233` n `54` status `ready` deltaP `38.5017` edge `0.3286` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0233` n `54` status `ready` deltaP `38.5017` edge `0.3286` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `5.8709` n `143` status `ready` deltaP `14.1833` edge `0.5369` maxDD `-6.3769`
- `market_context_high->crypto_major_4h` score `5.7249` n `143` status `ready` deltaP `22.2796` edge `0.4607` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `5.648` n `69` status `ready` deltaP `31.3097` edge `0.3472` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.648` n `69` status `ready` deltaP `31.3097` edge `0.3472` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `1.9653` n `69` status `ready` deltaP `7.8186` edge `0.253` maxDD `-6.3077`
- `risk_on_and_context->crypto_alt_4h` score `1.9653` n `69` status `ready` deltaP `7.8186` edge `0.253` maxDD `-6.3077`
- `market_context_high->crypto_major_1h` score `0.8399` n `155` status `ready` deltaP `6.5781` edge `0.1067` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5642` n `155` status `ready` deltaP `8.0182` edge `0.125` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.3518` n `143` status `ready` deltaP `12.758` edge `0.0488` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.2157` n `81` status `ready` deltaP `7.5576` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2157` n `81` status `ready` deltaP `7.5576` edge `0.006` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1321` n `155` status `ready` deltaP `7.9638` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.3176` n `81` status `ready` deltaP `11.3781` edge `0.0273` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3176` n `81` status `ready` deltaP `11.3781` edge `0.0273` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.328` n `155` status `ready` deltaP `7.6366` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3664` n `155` status `ready` deltaP `9.9603` edge `0.0376` maxDD `-7.0778`
- `risk_on_high->fx_1h` score `-0.3707` n `81` status `ready` deltaP `-0.8842` edge `-0.0036` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3707` n `81` status `ready` deltaP `-0.8842` edge `-0.0036` maxDD `-0.376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
