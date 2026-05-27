# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T21:07:21.105776+00:00`
- Price records: `672`
- Market context records: `2076`
- Flow alert records: `7870`
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

- `market_context_high->crypto_major_4h` score `9.9133` n `203` status `ready` deltaP `35.281` edge `0.6439` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.3404` n `203` status `ready` deltaP `28.0555` edge `0.7058` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.9269` n `203` status `ready` deltaP `22.778` edge `0.5003` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.0563` n `202` status `ready` deltaP `20.7647` edge `0.8983` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.577` n `203` status `ready` deltaP `19.3553` edge `0.2785` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0476` n `203` status `ready` deltaP `15.4497` edge `0.136` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.9485` n `203` status `ready` deltaP `14.6382` edge `0.1634` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8108` n `202` status `ready` deltaP `21.0816` edge `0.5002` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.6268` n `202` status `ready` deltaP `10.0808` edge `0.1912` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.6039` n `203` status `ready` deltaP `11.6442` edge `0.1674` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5026` n `202` status `ready` deltaP `21.085` edge `0.7599` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.463` n `203` status `ready` deltaP `8.3125` edge `0.062` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4281` n `203` status `ready` deltaP `4.9409` edge `0.0747` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.082` n `203` status `ready` deltaP `4.1105` edge `0.0248` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2105` n `202` status `ready` deltaP `14.1697` edge `0.0273` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.4588` n `203` status `ready` deltaP `11.8685` edge `0.14` maxDD `-11.5886`
- `market_context_high->fx_1h` score `-0.5786` n `203` status `ready` deltaP `-1.7868` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7573` n `203` status `ready` deltaP `4.1002` edge `0.0283` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4348` n `203` status `ready` deltaP `-4.7136` edge `0.0` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.6635` n `202` status `ready` deltaP `11.1892` edge `0.1769` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
