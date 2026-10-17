# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T13:52:30.880957+00:00`
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

- `risk_on_high->commodity_24h` score `7.0101` n `54` status `ready` deltaP `38.5017` edge `0.3275` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0101` n `54` status `ready` deltaP `38.5017` edge `0.3275` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `4.7236` n `155` status `ready` deltaP `18.749` edge `0.4124` maxDD `-6.1675`
- `risk_on_high->crypto_major_4h` score `3.0573` n `81` status `ready` deltaP `21.5447` edge `0.2549` maxDD `-6.1675`
- `risk_on_and_context->crypto_major_4h` score `3.0573` n `81` status `ready` deltaP `21.5447` edge `0.2549` maxDD `-6.1675`
- `market_context_high->crypto_alt_4h` score `2.776` n `155` status `ready` deltaP `11.0316` edge `0.472` maxDD `-16.1368`
- `market_context_high->crypto_major_1h` score `0.4313` n `167` status `ready` deltaP `4.9401` edge `0.0919` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1842` n `155` status `ready` deltaP `11.0671` edge `0.0461` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0882` n `167` status `ready` deltaP `6.4371` edge `0.0995` maxDD `-7.3143`
- `market_context_high->metal_1h` score `-0.2483` n `167` status `ready` deltaP `7.0359` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2834` n `90` status `ready` deltaP `0.7207` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2834` n `90` status `ready` deltaP `0.7207` edge `-0.0031` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3025` n `167` status `ready` deltaP `6.7523` edge `0.0046` maxDD `-1.3195`
- `market_context_high->equity_1h` score `-0.4101` n `167` status `ready` deltaP `9.3066` edge `0.0368` maxDD `-7.1141`
- `market_context_high->equity_4h` score `-0.428` n `155` status `ready` deltaP `12.9949` edge `0.2011` maxDD `-17.4086`
- `market_context_high->fx_1h` score `-0.4504` n `167` status `ready` deltaP `-0.6033` edge `-0.0016` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.4843` n `90` status `ready` deltaP `9.5195` edge `0.0258` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4843` n `90` status `ready` deltaP `9.5195` edge `0.0258` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
