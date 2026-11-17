# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T12:07:31.399326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `market_context_high->unknown_24h` score `1816.9767` n `86` status `ready` deltaP `3.4542` edge `151.3917` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.3927` n `50` status `ready` deltaP `65.5475` edge `4.4997` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.5395` n `50` status `ready` deltaP `30.5389` edge `2.1594` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.455` n `50` status `ready` deltaP `44.25` edge `1.0226` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.3622` n `86` status `ready` deltaP `44.6319` edge `1.8708` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.3915` n `86` status `ready` deltaP `28.6983` edge `1.7379` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.0332` n `50` status `ready` deltaP `56.9119` edge `0.4037` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.792` n `50` status `ready` deltaP `51.2953` edge `0.3907` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.4217` n `50` status `ready` deltaP `16.8843` edge `1.4177` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0` n `50` status `ready` deltaP `44.3841` edge `0.1584` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5345` n `50` status `ready` deltaP `22.994` edge `0.2876` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.444` n `50` status `ready` deltaP `26.3841` edge `0.338` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.9292` n `50` status `ready` deltaP `20.5366` edge `0.3281` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.764` n `50` status `ready` deltaP `34.5915` edge `0.1084` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.154` n `50` status `ready` deltaP `29.5244` edge `0.101` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1395` n `50` status `ready` deltaP `24.0958` edge `0.0431` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.482` n `50` status `ready` deltaP `18.994` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8439` n `50` status `ready` deltaP `19.0017` edge `0.1988` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7266` n `50` status `ready` deltaP `16.2455` edge `0.0828` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6845` n `50` status `ready` deltaP `18.2455` edge `0.0713` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
