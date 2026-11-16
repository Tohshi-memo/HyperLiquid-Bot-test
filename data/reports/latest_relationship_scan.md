# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T12:07:36.352803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `101.1693` n `30` status `ready` deltaP `3.9861` edge `8.4042` maxDD `0.0`
- `news_risk_high->equity_24h` score `51.5639` n `50` status `ready` deltaP `55.9376` edge `3.9947` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.4363` n `50` status `ready` deltaP `42.4021` edge `2.5799` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.3096` n `30` status `ready` deltaP `14.2692` edge `1.5851` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `12.6593` n `50` status `ready` deltaP `40.3592` edge `0.8989` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5718` n `30` status `ready` deltaP `44.4021` edge `1.6428` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.1258` n `50` status `ready` deltaP `24.9359` edge `1.5825` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.5863` n `50` status `ready` deltaP `46.9255` edge `0.3497` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0244` n `50` status `ready` deltaP `41.0745` edge `0.2282` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0913` n `50` status `ready` deltaP `45.3607` edge `0.1595` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.8664` n `50` status `ready` deltaP `28.274` edge `0.3606` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5204` n `50` status `ready` deltaP `22.1218` edge `0.3668` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9649` n `50` status `ready` deltaP `20.3737` edge `0.2576` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.9063` n `30` status `ready` deltaP `47.9492` edge `0.2703` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.6564` n `50` status `ready` deltaP `34.207` edge `0.102` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6388` n `50` status `ready` deltaP `25.1842` edge `0.087` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1739` n `50` status `ready` deltaP `24.6158` edge `0.0425` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3057` n `50` status `ready` deltaP `17.2706` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0278` n `50` status `ready` deltaP `19.2825` edge `0.2205` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8486` n `50` status `ready` deltaP `18.1106` edge `0.086` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
