# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T08:37:31.474712+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7468`

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

- `news_risk_high->unknown_24h` score `817.6636` n `135` status `ready` deltaP `1.9097` edge `68.1259` maxDD `0.0`
- `market_context_high->unknown_1h` score `568.0808` n `40` status `ready` deltaP `9.7305` edge `47.2752` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.8489` n `135` status `ready` deltaP `28.5532` edge `1.318` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.8217` n `135` status `ready` deltaP `27.1644` edge `0.7056` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.4853` n `135` status `ready` deltaP `23.9931` edge `0.7792` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.6932` n `135` status `ready` deltaP `33.3565` edge `0.1332` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.3122` n `135` status `ready` deltaP `25.5324` edge `0.2332` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.8396` n `135` status `ready` deltaP `29.0187` edge `0.2033` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.7529` n `135` status `ready` deltaP `10.6549` edge `0.341` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.5619` n `40` status `ready` deltaP `9.2515` edge `0.1348` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `1.3775` n `40` status `ready` deltaP `8.5928` edge `0.1185` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0754` n `135` status `ready` deltaP `9.2515` edge `0.119` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.9686` n `40` status `ready` deltaP `14.1018` edge `0.0727` maxDD `-2.4027`
- `news_risk_high->equity_1h` score `0.8744` n `135` status `ready` deltaP `9.1018` edge `0.0745` maxDD `-1.6514`
- `market_context_high->fx_1h` score `0.7227` n `40` status `ready` deltaP `12.1407` edge `0.0057` maxDD `-0.113`
- `news_risk_high->index_1h` score `0.479` n `135` status `ready` deltaP `8.6682` edge `0.0109` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.4399` n `40` status `ready` deltaP `8.1437` edge `0.0242` maxDD `-0.4338`
- `market_context_high->index_1h` score `0.2044` n `40` status `ready` deltaP `5.1497` edge `0.0164` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.2026` n `135` status `ready` deltaP `6.1868` edge `0.0272` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.6192` n `135` status `ready` deltaP `-0.1896` edge `0.0126` maxDD `-0.7016`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
