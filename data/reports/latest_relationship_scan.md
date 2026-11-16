# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T04:22:22.284070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8920`

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

- `news_risk_high->equity_24h` score `48.1338` n `50` status `ready` deltaP `50.8472` edge `3.7428` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `36.9189` n `64` status `ready` deltaP `6.1738` edge `3.044` maxDD `-0.02`
- `news_risk_high->crypto_major_24h` score `21.2543` n `50` status `ready` deltaP `41.3333` edge `2.5637` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.913` n `50` status `ready` deltaP `37.3902` edge `0.8565` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1201` n `50` status `ready` deltaP `20.9097` edge `1.4804` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.9201` n `50` status `ready` deltaP `42.5139` edge `0.3236` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2142` n `50` status `ready` deltaP `40.9722` edge `0.2447` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0048` n `50` status `ready` deltaP `44.3841` edge `0.1588` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3088` n `50` status `ready` deltaP `20.8415` edge `0.3577` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0868` n `50` status `ready` deltaP `25.7744` edge `0.3123` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9325` n `50` status `ready` deltaP `20.2994` edge `0.2554` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8693` n `50` status `ready` deltaP `35.3537` edge `0.1121` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4648` n `50` status `ready` deltaP `23.5793` edge `0.0832` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.27` n `50` status `ready` deltaP `25.5928` edge `0.044` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2891` n `50` status `ready` deltaP `17.0479` edge `0.0239` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9956` n `50` status `ready` deltaP `18.9028` edge `0.2189` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8731` n `50` status `ready` deltaP `20.0419` edge `0.0835` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8255` n `50` status `ready` deltaP `18.1916` edge `0.0825` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3761` n `50` status `ready` deltaP `4.2455` edge `0.0365` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.9738` n `74` status `ready` deltaP `-5.8667` edge `-0.0099` maxDD `-2.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
