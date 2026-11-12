# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T00:22:28.272676+00:00`
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

- `market_context_high->unknown_4h` score `94.7496` n `88` status `ready` deltaP `8.4129` edge `7.8845` maxDD `-0.9161`
- `market_context_high->unknown_24h` score `68.0184` n `88` status `ready` deltaP `4.9937` edge `5.649` maxDD `-0.4609`
- `news_risk_high->equity_24h` score `48.7647` n `37` status `ready` deltaP `36.6782` edge `3.8192` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `26.9149` n `37` status `ready` deltaP `50.4396` edge `2.1032` maxDD `-12.7247`
- `market_context_high->equity_24h` score `20.0201` n `88` status `ready` deltaP `19.6327` edge `1.7766` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `12.3684` n `37` status `ready` deltaP `26.2415` edge `1.0306` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.2309` n `53` status `ready` deltaP `34.0369` edge `0.8212` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.1449` n `37` status `ready` deltaP `33.391` edge `0.3728` maxDD `0.0`
- `news_risk_high->commodity_24h` score `7.0204` n `37` status `ready` deltaP `39.9654` edge `0.3186` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.5057` n `88` status `ready` deltaP `34.9638` edge `1.1104` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.7497` n `88` status `ready` deltaP `34.142` edge `0.2235` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.255` n `53` status `ready` deltaP `41.2826` edge `0.117` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.7541` n `88` status `ready` deltaP `19.7546` edge `0.2274` maxDD `-2.3671`
- `news_risk_high->crypto_major_4h` score `3.7235` n `53` status `ready` deltaP `20.347` edge `0.3234` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6065` n `53` status `ready` deltaP `18.6137` edge `0.2477` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6424` n `53` status `ready` deltaP `23.9023` edge `0.0862` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2146` n `53` status `ready` deltaP `20.9816` edge `0.0883` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0252` n `53` status `ready` deltaP `24.3927` edge `0.0316` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9938` n `53` status `ready` deltaP `23.816` edge `0.2607` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3688` n `53` status `ready` deltaP `17.7748` edge `0.0257` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
