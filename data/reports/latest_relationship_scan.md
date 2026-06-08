# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T07:07:26.058610+00:00`
- Price records: `672`
- Market context records: `3259`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10498`

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

- `risk_on_high->crypto_major_4h` score `16.7418` n `31` status `ready` deltaP `30.8517` edge `1.3017` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.7418` n `31` status `ready` deltaP `30.8517` edge `1.3017` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.834` n `103` status `ready` deltaP `16.22` edge `2.6496` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.9433` n `103` status `ready` deltaP `46.0845` edge `0.8142` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2186` n `103` status `ready` deltaP `30.1005` edge `0.823` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2471` n `103` status `ready` deltaP `17.6595` edge `1.5248` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.1265` n `31` status `ready` deltaP `11.9788` edge `0.7618` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1265` n `31` status `ready` deltaP `11.9788` edge `0.7618` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2467` n `31` status `ready` deltaP `18.809` edge `0.5325` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2467` n `31` status `ready` deltaP `18.809` edge `0.5325` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.3954` n `156` status `ready` deltaP `20.2705` edge `0.1603` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.2053` n `32` status `ready` deltaP `8.2148` edge `0.3349` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2053` n `32` status `ready` deltaP `8.2148` edge `0.3349` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.5795` n `31` status `ready` deltaP `5.7533` edge `0.2229` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5795` n `31` status `ready` deltaP `5.7533` edge `0.2229` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.4229` n `103` status `ready` deltaP `19.5961` edge `2.1217` maxDD `-152.2601`
- `risk_on_high->crypto_alt_1h` score `0.3319` n `32` status `ready` deltaP `1.497` edge `0.1763` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.3319` n `32` status `ready` deltaP `1.497` edge `0.1763` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.3219` n `32` status `ready` deltaP `6.3997` edge `0.0671` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3219` n `32` status `ready` deltaP `6.3997` edge `0.0671` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
