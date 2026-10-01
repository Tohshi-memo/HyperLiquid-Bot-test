# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T03:52:33.934330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6730`

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

- `market_context_high->unknown_1h` score `318.4588` n `50` status `ready` deltaP `6.6826` edge `26.4986` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.5806` n `50` status `ready` deltaP `6.7073` edge `23.337` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.042` n `135` status `ready` deltaP `29.2477` edge `1.4128` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0343` n `50` status `ready` deltaP `19.2195` edge `0.5284` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4783` n `135` status `ready` deltaP `23.6459` edge `0.6976` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4291` n `135` status `ready` deltaP `24.9074` edge `0.6046` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `4.0169` n `50` status `ready` deltaP `14.6646` edge `0.3663` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.983` n `50` status `ready` deltaP `15.3473` edge `0.1913` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8297` n `135` status `ready` deltaP `21.8866` edge `0.2173` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.7987` n `50` status `ready` deltaP `31.622` edge `0.0359` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7108` n `135` status `ready` deltaP `25.8912` edge `0.1011` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6243` n `50` status `ready` deltaP `13.1557` edge `0.1973` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.8966` n `135` status `ready` deltaP `23.5309` edge `0.1613` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4052` n `50` status `ready` deltaP `19.8922` edge `0.0109` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.5352` n `135` status `ready` deltaP `6.7066` edge `0.0622` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5261` n `135` status `ready` deltaP `7.1557` edge `0.0872` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3891` n `135` status `ready` deltaP `8.3683` edge `0.2426` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.2909` n `135` status `ready` deltaP `6.7221` edge `0.0082` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0417` n `50` status `ready` deltaP `9.3473` edge `-0.0046` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1667` n `50` status `ready` deltaP `-1.2934` edge `0.0523` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
