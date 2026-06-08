# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T03:37:22.899947+00:00`
- Price records: `672`
- Market context records: `3244`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `risk_on_high->crypto_major_4h` score `16.9656` n `30` status `ready` deltaP `29.9289` edge `1.3265` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.9656` n `30` status `ready` deltaP `29.9289` edge `1.3265` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.1099` n `103` status `ready` deltaP `17.9561` edge `2.6734` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.5553` n `103` status `ready` deltaP `48.5151` edge `0.849` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.4911` n `103` status `ready` deltaP `31.3157` edge `0.8376` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.4183` n `103` status `ready` deltaP `18.7011` edge `1.5398` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.4204` n `30` status `ready` deltaP `13.8516` edge `0.787` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.4204` n `30` status `ready` deltaP `13.8516` edge `0.787` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.0631` n `30` status `ready` deltaP `18.0387` edge `0.5141` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.0631` n `30` status `ready` deltaP `18.0387` edge `0.5141` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.5798` n `31` status `ready` deltaP `10.3776` edge `0.3685` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5798` n `31` status `ready` deltaP `10.3776` edge `0.3685` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.2349` n `103` status `ready` deltaP `22.0267` edge `2.2096` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.9525` n `142` status `ready` deltaP `17.7946` edge `0.1399` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.4577` n `30` status `ready` deltaP `4.4004` edge `0.2163` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.4577` n `30` status `ready` deltaP `4.4004` edge `0.2163` maxDD `-1.7001`
- `risk_on_high->crypto_alt_1h` score `0.7137` n `31` status `ready` deltaP `3.7087` edge `0.2105` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7137` n `31` status `ready` deltaP `3.7087` edge `0.2105` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4631` n `31` status `ready` deltaP `7.9148` edge `0.0751` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4631` n `31` status `ready` deltaP `7.9148` edge `0.0751` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
