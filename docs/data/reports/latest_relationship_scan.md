# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T18:07:28.729488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `0.6612` n `133` status `ready` deltaP `8.2381` edge `0.0229` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1732` n `133` status `ready` deltaP `10.6062` edge `0.0046` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1335` n `129` status `ready` deltaP `8.7103` edge `0.0093` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1401` n `133` status `ready` deltaP `2.0294` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2295` n `133` status `ready` deltaP `6.4146` edge `0.0348` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3604` n `133` status `ready` deltaP `0.233` edge `-0.0059` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5294` n `129` status `ready` deltaP `2.7037` edge `-0.0243` maxDD `-1.5942`
- `market_context_high->unknown_4h` score `-0.6049` n `129` status `ready` deltaP `20.7766` edge `-0.145` maxDD `-0.5133`
- `market_context_high->crypto_alt_1h` score `-0.65` n `133` status `ready` deltaP `0.7193` edge `0.0212` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6791` n `133` status `ready` deltaP `-4.5709` edge `0.0` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6847` n `129` status `ready` deltaP `-1.5516` edge `0.0076` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6962` n `129` status `ready` deltaP `0.8709` edge `0.0085` maxDD `-2.618`
- `market_context_high->commodity_24h` score `-0.7939` n `105` status `ready` deltaP `1.8105` edge `0.1051` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1913` n `133` status `ready` deltaP `-1.1008` edge `-0.0429` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.2273` n `129` status `ready` deltaP `3.6479` edge `0.0004` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.9539` n `129` status `ready` deltaP `-3.3584` edge `0.0524` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.7086` n `105` status `ready` deltaP `-9.3502` edge `-0.0024` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.7899` n `129` status `ready` deltaP `0.1903` edge `-0.215` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2527` n `105` status `ready` deltaP `-6.4633` edge `-0.0519` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7303` n `105` status `ready` deltaP `-18.4574` edge `-0.1526` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
