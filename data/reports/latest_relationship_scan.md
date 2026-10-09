# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T01:22:31.712734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.82` n `91` status `ready` deltaP `-3.5965` edge `3.3962` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.1556` n `49` status `ready` deltaP `43.4451` edge `0.89` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6716` n `49` status `ready` deltaP `44.394` edge `0.8501` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.0216` n `49` status `ready` deltaP `28.5785` edge `0.7379` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.4123` n `90` status `ready` deltaP `21.9122` edge `1.358` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.3532` n `90` status `ready` deltaP `27.8529` edge `0.5533` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8324` n `49` status `ready` deltaP `48.7002` edge `0.2447` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8603` n `49` status `ready` deltaP `32.233` edge `0.294` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5429` n `49` status `ready` deltaP `45.3677` edge `0.0806` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.2093` n `90` status `ready` deltaP `13.6145` edge `0.9145` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.0678` n `49` status `ready` deltaP `12.0127` edge `0.2111` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.5771` n `49` status `ready` deltaP `6.04` edge `0.2062` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4146` n `49` status `ready` deltaP `29.8363` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1429` n `49` status `ready` deltaP `29.194` edge `-0.0076` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.6872` n `91` status `ready` deltaP `17.7064` edge `0.2313` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.2317` n `90` status `ready` deltaP `21.3922` edge `0.1638` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1321` n `49` status `ready` deltaP `17.8385` edge `0.0678` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5003` n `91` status `ready` deltaP `15.6862` edge `0.0118` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.3877` n `91` status `ready` deltaP `8.1941` edge `0.0019` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2826` n `91` status `ready` deltaP `10.4429` edge `0.0555` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
