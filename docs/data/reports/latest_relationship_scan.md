# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T18:52:32.829473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6942`

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

- `market_context_high->unknown_1h` score `309.3351` n `50` status `ready` deltaP `7.5808` edge `25.7323` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.3779` n `50` status `ready` deltaP `8.0793` edge `23.3943` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.5125` n `135` status `ready` deltaP `27.1643` edge `1.2159` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8171` n `50` status `ready` deltaP `18.3049` edge `0.5164` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.3184` n `135` status `ready` deltaP `24.213` edge `0.6` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1591` n `135` status `ready` deltaP `23.6459` edge `0.671` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3993` n `50` status `ready` deltaP `13.1402` edge `0.325` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0357` n `50` status `ready` deltaP `15.7964` edge `0.1927` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9081` n `50` status `ready` deltaP `32.689` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.9042` n `135` status `ready` deltaP `27.4537` edge `0.1068` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7155` n `135` status `ready` deltaP `21.5393` edge `0.2101` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6782` n `50` status `ready` deltaP `13.7545` edge `0.1978` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3053` n `135` status `ready` deltaP `25.9699` edge `0.1791` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7989` n `135` status `ready` deltaP `8.9521` edge `0.0692` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.58` n `135` status `ready` deltaP `7.7545` edge `0.0877` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4382` n `135` status `ready` deltaP `8.3688` edge `0.0095` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0046` n `50` status `ready` deltaP `0.9521` edge `0.0593` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0236` n `50` status `ready` deltaP `8.8982` edge `-0.0077` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.1874` n `50` status `ready` deltaP `2.5449` edge `0.0097` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
