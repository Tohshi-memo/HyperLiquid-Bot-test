# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T01:22:26.822502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_1h` score `371.4277` n `51` status `ready` deltaP `13.3087` edge `30.8685` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.703` n `50` status `ready` deltaP `12.9573` edge `26.7222` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2636` n `50` status `ready` deltaP `29.286` edge `1.0804` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.1473` n `50` status `ready` deltaP `35.3795` edge `0.8347` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.5449` n `62` status `ready` deltaP `28.3977` edge `0.7379` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4459` n `68` status `ready` deltaP `37.8766` edge `0.6383` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1395` n `68` status `ready` deltaP `25.0897` edge `0.5621` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.046` n `50` status `ready` deltaP `16.1707` edge `0.5497` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4228` n `50` status `ready` deltaP `14.2073` edge `0.4861` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4239` n `62` status `ready` deltaP `31.7298` edge `0.173` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `news_risk_high->index_4h` score `2.9729` n `68` status `ready` deltaP `32.5413` edge `0.057` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9335` n `50` status `ready` deltaP `32.8415` edge `0.039` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.8875` n `68` status `ready` deltaP `12.7598` edge `0.1911` maxDD `-1.5096`
- `market_context_high->crypto_alt_1h` score `2.8101` n `51` status `ready` deltaP `11.5622` edge `0.2234` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.6467` n `51` status `ready` deltaP `10.799` edge `0.1936` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3613` n `68` status `ready` deltaP `19.9875` edge `0.1051` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0078` n `68` status `ready` deltaP `24.7975` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.4502` n `51` status `ready` deltaP `20.3945` edge `0.0113` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4263` n `50` status `ready` deltaP `7.688` edge `0.3178` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
