# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T04:52:24.860525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8938`

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

- `news_risk_high->equity_24h` score `48.2617` n `50` status `ready` deltaP `51.0208` edge `3.7523` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `36.7161` n `64` status `ready` deltaP `6.1738` edge `3.0271` maxDD `-0.02`
- `news_risk_high->crypto_major_24h` score `21.225` n `50` status `ready` deltaP `41.1597` edge `2.5611` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.889` n `50` status `ready` deltaP `37.3902` edge `0.8545` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1408` n `50` status `ready` deltaP `21.0833` edge `1.4819` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.9436` n `50` status `ready` deltaP `42.6875` edge `0.3244` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1974` n `50` status `ready` deltaP `40.9722` edge `0.2433` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.006` n `50` status `ready` deltaP `44.3841` edge `0.1589` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.2608` n `50` status `ready` deltaP `20.8415` edge `0.3537` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0134` n `50` status `ready` deltaP `25.622` edge `0.3072` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9277` n `50` status `ready` deltaP `20.2994` edge `0.255` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8549` n `50` status `ready` deltaP `35.3537` edge `0.1109` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4624` n `50` status `ready` deltaP `23.5793` edge `0.083` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2844` n `50` status `ready` deltaP `25.7425` edge `0.0442` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2759` n `50` status `ready` deltaP `16.8982` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9917` n `50` status `ready` deltaP `18.9028` edge `0.2184` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8739` n `50` status `ready` deltaP `20.0419` edge `0.0836` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8247` n `50` status `ready` deltaP `18.1916` edge `0.0824` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3749` n `50` status `ready` deltaP `4.2455` edge `0.0364` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-1.0667` n `72` status `ready` deltaP `-7.3686` edge `-0.0118` maxDD `-2.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
