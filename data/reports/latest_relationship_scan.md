# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T02:52:21.225907+00:00`
- Price records: `672`
- Market context records: `2001`
- Flow alert records: `7652`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7593`

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

- `market_context_high->crypto_major_4h` score `8.7125` n `218` status `ready` deltaP `30.6053` edge `0.575` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.0938` n `218` status `ready` deltaP `24.0224` edge `0.6288` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.3206` n `218` status `ready` deltaP `17.9095` edge `0.3989` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.6166` n `218` status `ready` deltaP `15.6453` edge `0.2232` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.1319` n `185` status `ready` deltaP `15.6599` edge `0.6053` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.4852` n `185` status `ready` deltaP `16.3754` edge `0.2572` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.362` n `218` status `ready` deltaP `11.4775` edge `0.1356` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.1136` n `218` status `ready` deltaP `9.5506` edge `0.1405` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.036` n `185` status `ready` deltaP `14.4715` edge `0.4797` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.933` n `218` status `ready` deltaP `9.3771` edge `0.0836` maxDD `-1.8022`
- `market_context_high->fx_24h` score `0.6999` n `185` status `ready` deltaP `16.2643` edge `0.0295` maxDD `-1.3685`
- `market_context_high->crypto_major_24h` score `0.1516` n `185` status `ready` deltaP `19.6825` edge `0.74` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.0705` n `185` status `ready` deltaP `2.7472` edge `0.1104` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0374` n `218` status `ready` deltaP `5.1173` edge `0.0416` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.5848` n `218` status `ready` deltaP `-1.8156` edge `-0.0001` maxDD `-0.3548`
- `market_context_high->index_1h` score `-0.5875` n `218` status `ready` deltaP `0.0426` edge `0.0098` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.7881` n `218` status `ready` deltaP `2.9981` edge `-0.0137` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.9494` n `218` status `ready` deltaP `1.7044` edge `0.0005` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.0876` n `218` status `ready` deltaP `-7.3198` edge `-0.0025` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.8454` n `218` status `ready` deltaP `5.9674` edge `0.0687` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
