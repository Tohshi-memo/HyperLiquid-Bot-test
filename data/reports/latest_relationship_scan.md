# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T03:22:27.178588+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3779` n `46` status `ready` deltaP `26.2983` edge `2.9438` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.9898` n `46` status `ready` deltaP `46.7769` edge `0.538` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.3683` n `46` status `ready` deltaP `39.4776` edge `0.4521` maxDD `-0.434`
- `market_context_high->unknown_4h` score `7.7134` n `82` status `ready` deltaP `4.5732` edge `0.6793` maxDD `-2.3601`
- `market_context_high->commodity_4h` score `1.1678` n `82` status `ready` deltaP `14.4817` edge `0.0854` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.7302` n `30` status `ready` deltaP `17.2655` edge `-0.0003` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.706` n `30` status `ready` deltaP `12.6389` edge `0.0715` maxDD `-1.5526`
- `market_context_high->fx_4h` score `0.3522` n `82` status `ready` deltaP `18.2927` edge `0.0092` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2984` n `88` status `ready` deltaP `6.2806` edge `0.0246` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2862` n `88` status `ready` deltaP `9.1794` edge `-0.0025` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.2329` n `30` status `ready` deltaP `4.3089` edge `0.0362` maxDD `-0.3082`
- `news_risk_high->commodity_4h` score `-0.1351` n `30` status `ready` deltaP `9.8476` edge `-0.0312` maxDD `-1.6568`
- `news_risk_high->unknown_4h` score `-0.1756` n `30` status `ready` deltaP `0.8333` edge `0.0208` maxDD `-1.5766`
- `news_risk_high->index_1h` score `-0.2919` n `30` status `ready` deltaP `-1.008` edge `-0.0109` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.335` n `30` status `ready` deltaP `8.503` edge `-0.0356` maxDD `-3.1233`
- `news_risk_high->index_4h` score `-0.4022` n `30` status `ready` deltaP `-5.1829` edge `0.0391` maxDD `-0.3783`
- `market_context_high->index_1h` score `-0.4102` n `88` status `ready` deltaP `2.4769` edge `-0.0157` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.4568` n `30` status `ready` deltaP `-4.3812` edge `0.0018` maxDD `-0.1588`
- `market_context_high->metal_1h` score `-0.4996` n `88` status `ready` deltaP `-1.0207` edge `-0.0078` maxDD `-1.6224`
- `news_risk_high->equity_4h` score `-0.5887` n `30` status `ready` deltaP `-15.6402` edge `0.1247` maxDD `-2.8924`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
