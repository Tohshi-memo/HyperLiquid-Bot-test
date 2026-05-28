# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T03:07:17.609321+00:00`
- Price records: `672`
- Market context records: `2102`
- Flow alert records: `7945`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.6423` n `179` status `ready` deltaP `31.1589` edge `0.7936` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4631` n `179` status `ready` deltaP `37.6081` edge `0.6742` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.751` n `179` status `ready` deltaP `23.5897` edge `0.3969` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1226` n `179` status `ready` deltaP `22.6206` edge `0.3022` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5263` n `179` status `ready` deltaP `18.9127` edge `0.1528` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.4824` n `178` status `ready` deltaP `22.9813` edge `0.5857` maxDD `-35.8966`
- `market_context_high->index_24h` score `2.2961` n `178` status `ready` deltaP `11.6967` edge `0.2362` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.1817` n `179` status `ready` deltaP `15.6333` edge `0.1762` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.9787` n `179` status `ready` deltaP `12.6393` edge `0.192` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.5829` n `178` status `ready` deltaP `22.8977` edge `0.4691` maxDD `-33.1875`
- `market_context_high->metal_4h` score `0.8659` n `179` status `ready` deltaP `15.3146` edge `0.1758` maxDD `-9.7923`
- `market_context_high->equity_1h` score `0.8376` n `179` status `ready` deltaP `10.9708` edge `0.0755` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2385` n `179` status `ready` deltaP `5.406` edge `0.0558` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1749` n `179` status `ready` deltaP `6.3627` edge `0.0312` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.049` n `178` status `ready` deltaP `20.9653` edge `0.7229` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0751` n `178` status `ready` deltaP `14.9061` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.1762` n `179` status `ready` deltaP `6.9138` edge `0.0413` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8562` n `179` status `ready` deltaP `-1.4368` edge `0.001` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.0105` n `178` status `ready` deltaP `10.2018` edge `0.2379` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0404` n `179` status `ready` deltaP `-6.4271` edge `-0.0024` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
