# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T15:52:35.639317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4210`

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

- `market_context_high->unknown_1h` score `368.0457` n `50` status `ready` deltaP `11.4731` edge `30.5989` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `296.6784` n `50` status `ready` deltaP `12.1951` edge `24.6419` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2863` n `50` status `ready` deltaP `29.9792` edge `1.161` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8159` n `50` status `ready` deltaP `37.6326` edge `0.8754` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.9439` n `63` status `ready` deltaP `38.4316` edge `0.6761` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6251` n `62` status `ready` deltaP `29.6109` edge `0.7365` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.619` n `63` status `ready` deltaP `27.0785` edge `0.5888` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3201` n `50` status `ready` deltaP `17.5427` edge `0.5634` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2697` n `50` status `ready` deltaP `17.7134` edge `0.5333` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6179` n `62` status `ready` deltaP `33.8095` edge `0.1753` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0153` n `63` status `ready` deltaP `27.3568` edge `0.2135` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3585` n `50` status `ready` deltaP `15.1018` edge `0.2455` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1408` n `63` status `ready` deltaP `34.0109` edge `0.0612` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0858` n `50` status `ready` deltaP `34.6707` edge `0.0395` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0302` n `68` status `ready` deltaP `13.9574` edge `0.195` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9653` n `50` status `ready` deltaP `13.2515` edge `0.2038` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3017` n `63` status `ready` deltaP `18.4331` edge `0.1105` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0593` n `68` status `ready` deltaP `25.3963` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.7032` n `68` status `ready` deltaP `6.4547` edge `0.1508` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
