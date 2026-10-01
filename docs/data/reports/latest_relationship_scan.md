# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T09:37:33.678717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6886`

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

- `market_context_high->unknown_1h` score `324.3616` n `50` status `ready` deltaP `7.1317` edge `26.9875` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9708` n `50` status `ready` deltaP `6.8598` edge `23.3685` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.0392` n `124` status `ready` deltaP `29.6371` edge `1.4933` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.9498` n `47` status `ready` deltaP `32.6758` edge `0.6696` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.5671` n `50` status `ready` deltaP `18.0` edge `0.4976` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.9904` n `124` status `ready` deltaP `22.9782` edge `0.5809` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.3333` n `124` status `ready` deltaP `28.993` edge `0.2167` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.2089` n `124` status `ready` deltaP `21.7629` edge `0.7099` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.5039` n `50` status `ready` deltaP `13.2927` edge `0.3327` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.2213` n `47` status `ready` deltaP `14.7421` edge `0.5009` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.0331` n `124` status `ready` deltaP `12.6475` edge `0.3691` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.957` n `50` status `ready` deltaP `33.4512` edge `0.0369` maxDD `-0.0791`
- `market_context_high->crypto_alt_24h` score `2.8864` n `47` status `ready` deltaP `9.9734` edge `0.345` maxDD `-11.6768`
- `market_context_high->crypto_major_1h` score `2.826` n `50` status `ready` deltaP `14.2994` edge `0.1852` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.6217` n `124` status `ready` deltaP `24.7928` edge `0.101` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.4828` n `50` status `ready` deltaP `11.9581` edge `0.1935` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.2761` n `124` status `ready` deltaP `26.7305` edge `0.241` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6575` n `130` status `ready` deltaP `6.7273` edge `0.0636` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.6531` n `47` status `ready` deltaP `15.3037` edge `0.0835` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
