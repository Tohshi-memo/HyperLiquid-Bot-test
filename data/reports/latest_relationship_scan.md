# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T10:07:52.213859+00:00`
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

- `market_context_high->unknown_24h` score `105.4094` n `30` status `ready` deltaP `3.9931` edge `8.7575` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.6738` n `50` status `ready` deltaP `54.6667` edge `3.929` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.2879` n `50` status `ready` deltaP `41.3333` edge `2.568` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9049` n `30` status `ready` deltaP `13.0208` edge `1.5597` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.4234` n `30` status `ready` deltaP `43.3333` edge `1.6309` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.3811` n `50` status `ready` deltaP `39.372` edge `0.8823` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.8628` n `50` status `ready` deltaP `23.6875` edge `1.5571` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.4029` n `50` status `ready` deltaP `45.6389` edge `0.343` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0762` n `50` status `ready` deltaP `40.9722` edge `0.2332` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0827` n `50` status `ready` deltaP `45.2988` edge `0.1592` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6196` n `50` status `ready` deltaP `27.6037` edge `0.3445` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.4106` n `50` status `ready` deltaP `21.6037` edge `0.3611` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.9207` n `30` status `ready` deltaP `48.0903` edge `0.2712` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.9193` n `50` status `ready` deltaP `20.1497` edge `0.2553` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6638` n `50` status `ready` deltaP `34.1341` edge `0.1031` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5753` n `50` status `ready` deltaP `24.6463` edge `0.0853` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2245` n `50` status `ready` deltaP `25.1437` edge `0.0432` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.246` n `50` status `ready` deltaP `16.5988` edge `0.0233` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0422` n `50` status `ready` deltaP `19.4236` edge `0.2214` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8606` n `50` status `ready` deltaP `18.3413` edge `0.086` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
