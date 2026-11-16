# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T06:52:27.856752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8472`

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

- `news_risk_high->equity_24h` score `49.0532` n `50` status `ready` deltaP `52.4097` edge `3.809` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1449` n `50` status `ready` deltaP `40.6389` edge `2.5543` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9264` n `50` status `ready` deltaP `37.5427` edge `0.8566` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3635` n `50` status `ready` deltaP `22.4722` edge `1.5012` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.1243` n `50` status `ready` deltaP `44.0764` edge `0.3302` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1302` n `50` status `ready` deltaP `40.9722` edge `0.2377` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9734` n `50` status `ready` deltaP `44.2317` edge `0.1572` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1788` n `50` status `ready` deltaP `20.5366` edge `0.3489` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `3.9894` n `50` status `ready` deltaP `25.622` edge `0.3052` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9109` n `50` status `ready` deltaP `20.1497` edge `0.2546` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7364` n `50` status `ready` deltaP `34.5915` edge `0.1061` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4758` n `50` status `ready` deltaP `23.7317` edge `0.0831` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2545` n `50` status `ready` deltaP `25.4431` edge `0.0437` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2615` n `50` status `ready` deltaP `16.7485` edge `0.0236` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9831` n `50` status `ready` deltaP `18.9028` edge `0.2173` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8443` n `50` status `ready` deltaP `19.8922` edge `0.0808` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8076` n `50` status `ready` deltaP `18.0419` edge `0.0812` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.2706` n `50` status `ready` deltaP `3.3473` edge `0.0337` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-1.1469` n `67` status `ready` deltaP `-4.7659` edge `-0.0082` maxDD `-1.7817`
- `market_context_high->index_4h` score `-1.3903` n `64` status `ready` deltaP `-5.8308` edge `-0.0328` maxDD `-2.8591`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
