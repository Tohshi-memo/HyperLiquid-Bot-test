# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T13:22:24.703407+00:00`
- Price records: `672`
- Market context records: `8518`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6278.1777` n `52` status `ready` deltaP `44.7383` edge `522.9253` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.505` n `64` status `ready` deltaP `21.1128` edge `0.3777` maxDD `-3.4427`
- `market_context_high->equity_4h` score `2.4387` n `34` status `ready` deltaP `25.3407` edge `0.0831` maxDD `-2.2381`
- `news_risk_high->index_4h` score `1.9855` n `64` status `ready` deltaP `16.5015` edge `0.0745` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7314` n `64` status `ready` deltaP `15.9525` edge `0.0856` maxDD `-2.4803`
- `market_context_high->crypto_major_4h` score `1.1803` n `34` status `ready` deltaP `9.4781` edge `0.1615` maxDD `-2.8692`
- `market_context_high->crypto_alt_4h` score `1.173` n `34` status `ready` deltaP `13.2891` edge `0.1366` maxDD `-3.9846`
- `news_risk_high->crypto_major_4h` score `0.8126` n `64` status `ready` deltaP `5.5259` edge `0.1449` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7466` n `64` status `ready` deltaP `14.0244` edge `0.1414` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5162` n `64` status `ready` deltaP `9.0101` edge `0.0588` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.2885` n `64` status `ready` deltaP `6.3155` edge `0.0461` maxDD `-2.0972`
- `market_context_high->fx_4h` score `0.2755` n `34` status `ready` deltaP `9.6037` edge `0.0208` maxDD `-0.2932`
- `news_risk_high->fx_1h` score `0.0854` n `64` status `ready` deltaP `5.2863` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.055` n `64` status `ready` deltaP `4.5191` edge `0.0086` maxDD `-0.5338`
- `market_context_high->metal_4h` score `-0.0035` n `34` status `ready` deltaP `11.8544` edge `-0.0153` maxDD `-1.4679`
- `news_risk_high->metal_4h` score `-0.005` n `64` status `ready` deltaP `2.0198` edge `0.0335` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0098` n `64` status `ready` deltaP `11.1662` edge `0.0205` maxDD `-0.6604`
- `market_context_high->index_4h` score `-0.0202` n `34` status `ready` deltaP `4.6449` edge `0.006` maxDD `-0.4979`
- `market_context_high->commodity_1h` score `-0.0374` n `46` status `ready` deltaP `6.743` edge `0.0128` maxDD `-2.0038`
- `news_risk_high->metal_1h` score `-0.1323` n `64` status `ready` deltaP `3.256` edge `0.0076` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
