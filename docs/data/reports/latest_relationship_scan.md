# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T21:52:29.281586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4838`

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

- `market_context_high->unknown_1h` score `364.0079` n `50` status `ready` deltaP `10.4251` edge `30.2694` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.3563` n `50` status `ready` deltaP `10.2134` edge `24.2116` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6849` n `73` status `ready` deltaP `42.2256` edge `1.1298` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.3596` n `50` status `ready` deltaP `18.9653` edge `0.9072` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0738` n `50` status `ready` deltaP `31.8264` edge `0.6856` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.6038` n `73` status `ready` deltaP `30.6697` edge `0.561` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.8759` n `50` status `ready` deltaP `19.5244` edge `0.5965` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3489` n `50` status `ready` deltaP `17.7134` edge `0.5399` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `6.1699` n `116` status `ready` deltaP `23.5755` edge `0.4914` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3765` n `50` status `ready` deltaP `15.4012` edge `0.245` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1691` n `50` status `ready` deltaP `14.5988` edge `0.2118` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4695` n `116` status `ready` deltaP `21.7935` edge `0.1301` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.6887` n `116` status `ready` deltaP `16.1796` edge `0.3396` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5628` n `73` status `ready` deltaP `5.9908` edge `0.4758` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4191` n `50` status `ready` deltaP `6.8889` edge `0.3222` maxDD `-11.8957`
- `news_risk_high->metal_24h` score `1.3785` n `73` status `ready` deltaP `13.009` edge `0.2174` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.229` n `116` status `ready` deltaP `6.2978` edge `0.1165` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9358` n `50` status `ready` deltaP `19.4653` edge `0.092` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
