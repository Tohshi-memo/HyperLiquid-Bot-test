# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T04:37:27.268017+00:00`
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

- `news_risk_high->equity_24h` score `48.1878` n `50` status `ready` deltaP `50.8472` edge `3.7473` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `36.8457` n `64` status `ready` deltaP `6.1738` edge `3.0379` maxDD `-0.02`
- `news_risk_high->crypto_major_24h` score `21.232` n `50` status `ready` deltaP `41.1597` edge `2.562` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8998` n `50` status `ready` deltaP `37.3902` edge `0.8554` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1232` n `50` status `ready` deltaP `20.9097` edge `1.4808` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.9249` n `50` status `ready` deltaP `42.5139` edge `0.324` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2058` n `50` status `ready` deltaP `40.9722` edge `0.244` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0048` n `50` status `ready` deltaP `44.3841` edge `0.1588` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.2848` n `50` status `ready` deltaP `20.8415` edge `0.3557` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0434` n `50` status `ready` deltaP `25.622` edge `0.3097` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9289` n `50` status `ready` deltaP `20.2994` edge `0.2551` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8609` n `50` status `ready` deltaP `35.3537` edge `0.1114` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4636` n `50` status `ready` deltaP `23.5793` edge `0.0831` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.27` n `50` status `ready` deltaP `25.5928` edge `0.044` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2759` n `50` status `ready` deltaP `16.8982` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9932` n `50` status `ready` deltaP `18.9028` edge `0.2186` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8731` n `50` status `ready` deltaP `20.0419` edge `0.0835` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8255` n `50` status `ready` deltaP `18.1916` edge `0.0825` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3761` n `50` status `ready` deltaP `4.2455` edge `0.0365` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-1.0279` n `73` status `ready` deltaP `-6.6812` edge `-0.0114` maxDD `-2.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
