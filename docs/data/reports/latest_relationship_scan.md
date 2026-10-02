# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T17:37:31.474037+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4888`

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

- `market_context_high->unknown_1h` score `359.0206` n `50` status `ready` deltaP `11.024` edge `29.8498` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.6793` n `50` status `ready` deltaP `10.6707` edge `24.3188` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5281` n `73` status `ready` deltaP `39.795` edge `1.0496` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.2027` n `50` status `ready` deltaP `16.5347` edge `0.827` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.0278` n `73` status `ready` deltaP `32.5794` edge `0.5836` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9857` n `50` status `ready` deltaP `32.0` edge `0.6771` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.0521` n `50` status `ready` deltaP `17.2378` edge `0.5431` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.0234` n `50` status `ready` deltaP `15.2744` edge `0.4457` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.8444` n `116` status `ready` deltaP `21.1365` edge `0.3972` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.0298` n `50` status `ready` deltaP `14.2036` edge `0.2241` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9892` n `50` status `ready` deltaP `14.0` edge `0.2008` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7775` n `50` status `ready` deltaP `31.0122` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4399` n `116` status `ready` deltaP `22.0984` edge `0.1256` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.6946` n `50` status `ready` deltaP `8.7986` edge `0.3448` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5055` n `73` status `ready` deltaP `6.1644` edge `0.4673` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3301` n `73` status `ready` deltaP `13.009` edge `0.2112` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.1533` n `116` status `ready` deltaP `13.893` edge `0.2862` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8824` n `116` status `ready` deltaP `5.1002` edge `0.0956` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.7488` n `50` status `ready` deltaP `16.5139` edge `0.0877` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
