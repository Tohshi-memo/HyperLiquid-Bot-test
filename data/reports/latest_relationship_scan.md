# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T06:22:14.425613+00:00`
- Price records: `672`
- Market context records: `1193`
- Flow alert records: `5341`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5215` n `136` status `ready` deltaP `44.3321` edge `1.3611` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.602` n `136` status `ready` deltaP `22.0997` edge `0.6878` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `4.9981` n `136` status `ready` deltaP `4.1338` edge `0.5106` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.1418` n `136` status `ready` deltaP `-4.085` edge `0.5391` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8143` n `136` status `ready` deltaP `15.0377` edge `0.2006` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `2.3142` n `136` status `ready` deltaP `-3.2578` edge `0.5659` maxDD `-23.1066`
- `market_context_high->index_24h` score `1.9513` n `136` status `ready` deltaP `15.9212` edge `0.1651` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.4518` n `136` status `ready` deltaP `16.1867` edge `0.3109` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.949` n `136` status `ready` deltaP `10.5272` edge `0.0772` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5202` n `136` status `ready` deltaP `8.5857` edge `0.0178` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4078` n `136` status `ready` deltaP `4.1475` edge `0.0441` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.2602` n `136` status `ready` deltaP `8.7112` edge `0.0529` maxDD `-3.8101`
- `market_context_high->crypto_major_4h` score `-0.0545` n `136` status `ready` deltaP `7.1288` edge `0.1376` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1896` n `136` status `ready` deltaP `4.4954` edge `-0.0002` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2403` n `136` status `ready` deltaP `7.9826` edge `-0.0122` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3014` n `136` status `ready` deltaP `3.9495` edge `0.0116` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.3706` n `136` status `ready` deltaP `2.0527` edge `0.2284` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.3829` n `136` status `ready` deltaP `0.6429` edge `0.0309` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8302` n `136` status `ready` deltaP `-2.655` edge `0.01` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.0353` n `136` status `ready` deltaP `5.5596` edge `0.1267` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
