# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T14:52:35.547761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8739`

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

- `market_context_high->unknown_4h` score `40.6497` n `90` status `ready` deltaP `-2.6456` edge `3.459` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.227` n `49` status `ready` deltaP `42.6829` edge `0.8177` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.023` n `49` status `ready` deltaP `43.9367` edge `0.7991` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.082` n `49` status `ready` deltaP `21.5431` edge `0.4565` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.8014` n `90` status `ready` deltaP `18.0829` edge `1.0488` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.6399` n `49` status `ready` deltaP `41.6235` edge `0.1925` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.017` n `49` status `ready` deltaP `29.6416` edge `0.241` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.4135` n `90` status `ready` deltaP `20.8175` edge `0.2719` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3003` n `49` status `ready` deltaP `43.386` edge `0.0736` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.3852` n `49` status `ready` deltaP `34.7785` edge `0.0587` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.9238` n `49` status `ready` deltaP `12.0127` edge `0.1991` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.8956` n `90` status `ready` deltaP `18.0183` edge `0.2176` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.4174` n `49` status `ready` deltaP `6.6388` edge `0.1889` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4026` n `49` status `ready` deltaP `29.8363` edge `0.0153` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.3872` n `90` status `ready` deltaP `23.0915` edge `0.1724` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1762` n `49` status `ready` deltaP `18.2958` edge `0.0704` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.8614` n `90` status `ready` deltaP `9.787` edge `0.639` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6143` n `90` status `ready` deltaP `16.7954` edge `0.0139` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5326` n `91` status `ready` deltaP `9.8408` edge `0.003` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.189` n `91` status `ready` deltaP `10.4429` edge `0.0435` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
