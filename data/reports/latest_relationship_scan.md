# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T09:37:22.193467+00:00`
- Price records: `672`
- Market context records: `2030`
- Flow alert records: `7734`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8787` n `205` status `ready` deltaP `30.7927` edge `0.5876` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.367` n `205` status `ready` deltaP `24.5427` edge `0.6481` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8785` n `205` status `ready` deltaP `18.689` edge `0.4402` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0239` n `205` status `ready` deltaP `17.2561` edge `0.2464` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5476` n `205` status `ready` deltaP `12.6274` edge `0.1434` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4474` n `205` status `ready` deltaP `12.9269` edge `0.1028` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2785` n `205` status `ready` deltaP `10.2322` edge `0.1497` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.9145` n `199` status `ready` deltaP `16.7627` edge `0.4965` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.4177` n `199` status `ready` deltaP `15.8025` edge `0.4193` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.2569` n `199` status `ready` deltaP `4.1922` edge `0.1163` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2092` n `205` status `ready` deltaP `6.9104` edge `0.0502` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `-0.0166` n `205` status `ready` deltaP `3.5965` edge `0.0466` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3038` n `205` status `ready` deltaP `2.5537` edge `0.0167` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4461` n `199` status `ready` deltaP `11.187` edge `0.0229` maxDD `-2.439`
- `market_context_high->fx_1h` score `-0.8518` n `205` status `ready` deltaP `-1.2918` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9162` n `205` status `ready` deltaP `3.5088` edge `0.019` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1788` n `205` status `ready` deltaP `8.7195` edge `0.1059` maxDD `-11.9812`
- `market_context_high->metal_24h` score `-1.3477` n `199` status `ready` deltaP `10.212` edge `0.1415` maxDD `-19.0843`
- `market_context_high->fx_4h` score `-1.6231` n `205` status `ready` deltaP `-6.7378` edge `-0.0022` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.799` n `205` status `ready` deltaP `3.2043` edge `0.0038` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
