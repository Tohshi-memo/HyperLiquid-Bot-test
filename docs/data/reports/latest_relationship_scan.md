# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T05:52:30.088773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_24h` score `172.5055` n `88` status `ready` deltaP `5.5128` edge `14.3528` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.2186` n `88` status `ready` deltaP `7.2201` edge `7.3482` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `33.9655` n `50` status `ready` deltaP `27.564` edge `2.6833` maxDD `-1.9281`
- `news_risk_high->crypto_major_24h` score `20.9881` n `50` status `ready` deltaP `40.1799` edge `1.6777` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.1709` n `88` status `ready` deltaP `16.5185` edge `1.4766` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1927` n `53` status `ready` deltaP `33.6487` edge `0.8206` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6875` n `50` status `ready` deltaP `40.1384` edge `0.2897` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.5728` n `88` status `ready` deltaP `34.9638` edge `0.9908` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8489` n `88` status `ready` deltaP `35.0071` edge `0.226` maxDD `-1.4245`
- `news_risk_high->index_24h` score `4.7837` n `50` status `ready` deltaP `24.6228` edge `0.2504` maxDD `-0.2731`
- `news_risk_high->metal_4h` score `4.2503` n `53` status `ready` deltaP `40.9084` edge `0.1191` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9126` n `53` status `ready` deltaP `20.8957` edge `0.3355` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5789` n `53` status `ready` deltaP `18.6137` edge `0.2454` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.0466` n `88` status `ready` deltaP `16.9864` edge `0.1869` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7328` n `53` status `ready` deltaP `24.8821` edge `0.0872` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.16` n `53` status `ready` deltaP `24.8216` edge `0.2753` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.122` n `53` status `ready` deltaP `20.2888` edge `0.0852` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0959` n `53` status `ready` deltaP `24.9915` edge `0.0335` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.3695` n `50` status `ready` deltaP `10.782` edge `0.4866` maxDD `-24.6321`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
