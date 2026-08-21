# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T21:52:27.616018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.2755` n `133` status `ready` deltaP `8.9866` edge `0.0691` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3756` n `133` status `ready` deltaP `22.1575` edge `-0.0725` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.2145` n `133` status `ready` deltaP `11.3547` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1407` n `133` status `ready` deltaP `8.8197` edge `0.0095` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1089` n `133` status `ready` deltaP `2.6282` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2069` n `133` status `ready` deltaP `6.714` edge `0.0357` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3254` n `133` status `ready` deltaP `0.8318` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4179` n `133` status `ready` deltaP `4.337` edge `-0.0209` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5594` n `133` status `ready` deltaP `3.2311` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.5987` n `133` status `ready` deltaP `-0.094` edge `0.0089` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6604` n `133` status `ready` deltaP `-4.2715` edge `0.0004` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7412` n `133` status `ready` deltaP `0.5696` edge `0.0146` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.0121` n `105` status `ready` deltaP `-0.2728` edge `0.1008` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2911` n `133` status `ready` deltaP `-1.5499` edge `-0.0527` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.356` n `133` status `ready` deltaP `3.8981` edge `-0.012` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8043` n `133` status `ready` deltaP `-1.5152` edge `0.0593` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4655` n `105` status `ready` deltaP `-6.7461` edge `0.0005` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.0311` n `133` status `ready` deltaP `-0.1249` edge `-0.233` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.3083` n `105` status `ready` deltaP `-7.1578` edge `-0.0544` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8348` n `105` status `ready` deltaP `-18.4574` edge `-0.166` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
