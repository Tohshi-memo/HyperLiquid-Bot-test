# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T19:37:37.945144+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6952`

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

- `market_context_high->unknown_1h` score `319.0179` n `50` status `ready` deltaP `7.5808` edge `26.5392` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.895` n `50` status `ready` deltaP `7.622` edge `23.3571` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8038` n `135` status `ready` deltaP `27.6852` edge `1.2367` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8123` n `50` status `ready` deltaP `18.3049` edge `0.516` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.304` n `135` status `ready` deltaP `24.213` edge `0.5988` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.2275` n `135` status `ready` deltaP `23.6459` edge `0.6767` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4221` n `50` status `ready` deltaP `13.1402` edge `0.3269` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.013` n `50` status `ready` deltaP `15.6467` edge `0.1918` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9081` n `50` status `ready` deltaP `32.689` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8541` n `135` status `ready` deltaP `26.9329` edge `0.1061` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7215` n `135` status `ready` deltaP `21.5393` edge `0.2106` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.665` n `50` status `ready` deltaP `13.6048` edge `0.1977` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2896` n `135` status `ready` deltaP `25.8175` edge `0.1788` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7437` n `135` status `ready` deltaP `8.503` edge `0.0676` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5668` n `135` status `ready` deltaP `7.6048` edge `0.0876` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4262` n `135` status `ready` deltaP `8.2191` edge `0.0095` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0044` n `50` status `ready` deltaP `9.3473` edge `-0.0071` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0312` n `50` status `ready` deltaP `0.503` edge `0.0577` maxDD `-1.2043`
- `market_context_high->metal_1h` score `-0.203` n `50` status `ready` deltaP `2.3952` edge `0.0094` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
