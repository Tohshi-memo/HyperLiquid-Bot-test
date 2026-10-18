# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T16:37:24.904955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9294`

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

- `market_context_high->commodity_24h` score `2.0936` n `124` status `ready` deltaP `19.1277` edge `0.1321` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9674` n `89` status `ready` deltaP `21.1393` edge `0.1028` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9674` n `89` status `ready` deltaP `21.1393` edge `0.1028` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.085` n `125` status `ready` deltaP `15.9073` edge `0.3735` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.8082` n `90` status `ready` deltaP `16.7073` edge `0.2403` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.8082` n `90` status `ready` deltaP `16.7073` edge `0.2403` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.49` n `125` status `ready` deltaP `4.9988` edge `0.0964` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0904` n `90` status `ready` deltaP `5.946` edge `0.0063` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0904` n `90` status `ready` deltaP `5.946` edge `0.0063` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2685` n `90` status `ready` deltaP `0.9609` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2685` n `90` status `ready` deltaP `0.9609` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.2946` n `90` status `ready` deltaP `10.8108` edge `0.033` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2946` n `90` status `ready` deltaP `10.8108` edge `0.033` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.4252` n `125` status `ready` deltaP `2.6571` edge `0.0026` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.4276` n `125` status `ready` deltaP `1.8407` edge `0.0829` maxDD `-7.3329`
- `risk_on_high->metal_1h` score `-0.4845` n `90` status `ready` deltaP `1.008` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4845` n `90` status `ready` deltaP `1.008` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.494` n `125` status `ready` deltaP `2.3413` edge `0.008` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.5355` n `125` status `ready` deltaP `-2.1502` edge `-0.0022` maxDD `-0.503`
- `risk_on_high->crypto_major_1h` score `-0.6337` n `90` status `ready` deltaP `-0.5123` edge `0.0141` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
