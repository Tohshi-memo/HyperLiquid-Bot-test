# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T14:37:22.214705+00:00`
- Price records: `672`
- Market context records: `2466`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `news_risk_high->crypto_alt_24h` score `22.5776` n `31` status `ready` deltaP `45.5589` edge `1.6366` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `22.1996` n `31` status `ready` deltaP `56.1492` edge `1.5196` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `20.2711` n `31` status `ready` deltaP `28.8923` edge `1.5281` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `14.3279` n `31` status `ready` deltaP `29.1835` edge `1.0575` maxDD `-3.3119`
- `news_risk_high->index_24h` score `9.6505` n `31` status `ready` deltaP `27.5034` edge `0.6419` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.3249` n `31` status `ready` deltaP `24.0311` edge `0.4728` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6965` n `115` status `ready` deltaP `22.0395` edge `0.3606` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9427` n `136` status `ready` deltaP `20.5882` edge `0.4592` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8803` n `136` status `ready` deltaP `18.0236` edge `0.3842` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6269` n `31` status `ready` deltaP `35.5063` edge `0.084` maxDD `-0.1442`
- `news_risk_high->metal_4h` score `3.4919` n `31` status `ready` deltaP `16.4732` edge `0.4086` maxDD `-2.9923`
- `news_risk_high->commodity_4h` score `3.0345` n `31` status `ready` deltaP `21.4496` edge `0.177` maxDD `-3.0367`
- `news_risk_high->equity_4h` score `2.609` n `31` status `ready` deltaP `-5.6059` edge `0.4367` maxDD `-2.5203`
- `market_context_high->crypto_major_24h` score `2.3964` n `115` status `ready` deltaP `12.269` edge `0.6147` maxDD `-25.1408`
- `news_risk_high->crypto_alt_4h` score `2.0783` n `31` status `ready` deltaP `8.0645` edge `0.1788` maxDD `-2.4167`
- `news_risk_high->fx_4h` score `1.7116` n `31` status `ready` deltaP `21.7545` edge `0.016` maxDD `-0.1382`
- `market_context_high->unknown_4h` score `1.5721` n `136` status `ready` deltaP `9.9983` edge `0.1664` maxDD `-3.4972`
- `news_risk_high->unknown_1h` score `1.3994` n `31` status `ready` deltaP `17.2928` edge `0.0445` maxDD `-1.4536`
- `news_risk_high->index_4h` score `1.1349` n `31` status `ready` deltaP `-4.0273` edge `0.2507` maxDD `-2.6011`
- `news_risk_high->crypto_major_4h` score `1.0662` n `31` status `ready` deltaP `9.461` edge `0.1622` maxDD `-4.42`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
