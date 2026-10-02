# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T10:07:28.914068+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4854`

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

- `market_context_high->unknown_1h` score `340.9414` n `50` status `ready` deltaP `10.4251` edge `28.3472` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.2729` n `50` status `ready` deltaP `9.7561` edge `23.9577` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.324` n `72` status `ready` deltaP `39.7569` edge `1.0329` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.5511` n `50` status `ready` deltaP `35.4722` edge `0.7844` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.415` n `72` status `ready` deltaP `36.2848` edge `0.6745` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0201` n `50` status `ready` deltaP `16.5347` edge `0.8124` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9647` n `50` status `ready` deltaP `17.3902` edge `0.5348` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9323` n `50` status `ready` deltaP `15.4268` edge `0.4375` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4456` n `101` status `ready` deltaP `17.704` edge `0.3868` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9541` n `50` status `ready` deltaP `14.2036` edge `0.2178` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9395` n `50` status `ready` deltaP `32.8415` edge `0.0395` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.91` n `50` status `ready` deltaP `14.1497` edge `0.1932` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.6756` n `50` status `ready` deltaP `12.6181` edge `0.4451` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.5555` n `101` status `ready` deltaP `23.874` edge `0.1234` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.2745` n `72` status `ready` deltaP `9.0278` edge `0.5468` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4532` n `50` status `ready` deltaP `20.3413` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2743` n `72` status `ready` deltaP `12.3264` edge `0.2086` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `0.9618` n `112` status `ready` deltaP `6.2393` edge `0.0948` maxDD `-2.4998`
- `market_context_high->index_24h` score `0.9473` n `50` status `ready` deltaP `15.4861` edge `0.0753` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.8114` n `72` status `ready` deltaP `14.9305` edge `0.0523` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
