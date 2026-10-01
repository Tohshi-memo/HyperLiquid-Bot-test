# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T19:52:36.192838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6822`

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

- `market_context_high->unknown_1h` score `339.6997` n `50` status `ready` deltaP `8.479` edge `28.2567` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.132` n `50` status `ready` deltaP `6.8598` edge `23.7986` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3432` n `103` status `ready` deltaP `35.7319` edge `1.478` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.2235` n `50` status `ready` deltaP `33.0417` edge `0.7733` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2933` n `50` status `ready` deltaP `19.0671` edge `0.551` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.5076` n `50` status `ready` deltaP `11.6736` edge `0.5521` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0654` n `50` status `ready` deltaP `16.3415` edge `0.4425` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.8201` n `103` status `ready` deltaP `19.9737` edge `0.5839` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8809` n `50` status `ready` deltaP `19.0417` edge `0.5568` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3971` n `116` status `ready` deltaP `28.1382` edge `0.1651` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1562` n `50` status `ready` deltaP `35.2805` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0203` n `50` status `ready` deltaP `14.4491` edge `0.2004` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9386` n `50` status `ready` deltaP `13.4551` edge `0.2215` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.8723` n `103` status `ready` deltaP `20.9446` edge `0.4635` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.3209` n `103` status `ready` deltaP `23.4325` edge `0.085` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1588` n `103` status `ready` deltaP `25.0607` edge `0.2371` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5394` n `50` status `ready` deltaP `21.3892` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.905` n `50` status `ready` deltaP `14.7917` edge `0.0745` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5839` n `116` status `ready` deltaP `8.1768` edge `0.0478` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.4993` n `50` status `ready` deltaP `14.4306` edge `0.0696` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
