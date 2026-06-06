# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T03:37:22.234661+00:00`
- Price records: `672`
- Market context records: `3034`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `23.1386` n `99` status `ready` deltaP `11.1584` edge `2.2455` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.0466` n `99` status `ready` deltaP `22.9325` edge `0.9808` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.8129` n `99` status `ready` deltaP `42.3769` edge `0.8093` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.1853` n `99` status `ready` deltaP `22.3327` edge `1.1757` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.9308` n `99` status `ready` deltaP `21.9224` edge `0.6403` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8458` n `124` status `ready` deltaP `19.4041` edge `0.1725` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0421` n `129` status `ready` deltaP `2.4405` edge `0.0295` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.2793` n `124` status `ready` deltaP `2.1391` edge `0.0678` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.3788` n `129` status `ready` deltaP `4.2369` edge `0.0246` maxDD `-4.1126`
- `market_context_high->index_4h` score `-0.3916` n `124` status `ready` deltaP `13.8376` edge `0.078` maxDD `-13.3027`
- `market_context_high->equity_1h` score `-0.4739` n `129` status `ready` deltaP `3.5685` edge `0.037` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5252` n `129` status `ready` deltaP `-4.5897` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5669` n `129` status `ready` deltaP `6.3861` edge `0.0977` maxDD `-14.7034`
- `market_context_high->crypto_alt_4h` score `-0.6896` n `124` status `ready` deltaP `19.5417` edge `0.3592` maxDD `-40.5639`
- `market_context_high->unknown_1h` score `-0.8105` n `129` status `ready` deltaP `3.9212` edge `-0.0206` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.002` n `129` status `ready` deltaP `4.2798` edge `0.0693` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0995` n `124` status `ready` deltaP `-8.4137` edge `-0.003` maxDD `-0.8833`
- `market_context_high->metal_1h` score `-1.1458` n `129` status `ready` deltaP `-1.9484` edge `-0.0021` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.4985` n `99` status `ready` deltaP `-2.6673` edge `-0.0199` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-1.6362` n `124` status `ready` deltaP `10.7248` edge `0.0878` maxDD `-26.1923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
