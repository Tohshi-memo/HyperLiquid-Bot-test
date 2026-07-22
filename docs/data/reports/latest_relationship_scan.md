# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T01:22:23.608375+00:00`
- Price records: `672`
- Market context records: `7516`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14782`

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

- `risk_on_high->crypto_major_4h` score `7.4659` n `36` status `ready` deltaP `40.1423` edge `0.3738` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.4659` n `36` status `ready` deltaP `40.1423` edge `0.3738` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.3047` n `32` status `ready` deltaP `16.7732` edge `0.5157` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.3047` n `32` status `ready` deltaP `16.7732` edge `0.5157` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.1023` n `36` status `ready` deltaP `31.0129` edge `0.2428` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.1023` n `36` status `ready` deltaP `31.0129` edge `0.2428` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.332` n `36` status `ready` deltaP `14.5833` edge `0.3066` maxDD `-0.4256`
- `risk_on_and_context->unknown_4h` score `4.332` n `36` status `ready` deltaP `14.5833` edge `0.3066` maxDD `-0.4256`
- `risk_on_high->crypto_alt_24h` score `2.0814` n `32` status `ready` deltaP `16.5728` edge `0.2492` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0814` n `32` status `ready` deltaP `16.5728` edge `0.2492` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.6046` n `36` status `ready` deltaP `23.8024` edge `0.0715` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6046` n `36` status `ready` deltaP `23.8024` edge `0.0715` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.5377` n `31` status `ready` deltaP `16.2527` edge `0.0095` maxDD `-1.5794`
- `risk_on_and_context->fx_24h` score `0.5377` n `31` status `ready` deltaP `16.2527` edge `0.0095` maxDD `-1.5794`
- `risk_on_high->commodity_1h` score `0.5371` n `36` status `ready` deltaP `6.2312` edge `0.0316` maxDD `-0.2704`
- `risk_on_and_context->commodity_1h` score `0.5371` n `36` status `ready` deltaP `6.2312` edge `0.0316` maxDD `-0.2704`
- `risk_on_high->metal_4h` score `0.5058` n `36` status `ready` deltaP `4.1159` edge `0.0989` maxDD `-0.7352`
- `risk_on_and_context->metal_4h` score `0.5058` n `36` status `ready` deltaP `4.1159` edge `0.0989` maxDD `-0.7352`
- `risk_on_high->equity_1h` score `0.4346` n `36` status `ready` deltaP `7.8079` edge `0.0435` maxDD `-1.5203`
- `risk_on_and_context->equity_1h` score `0.4346` n `36` status `ready` deltaP `7.8079` edge `0.0435` maxDD `-1.5203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
