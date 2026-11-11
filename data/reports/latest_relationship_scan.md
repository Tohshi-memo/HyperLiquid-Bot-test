# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T20:07:30.053301+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_4h` score `82.7891` n `88` status `ready` deltaP `8.592` edge `6.8866` maxDD `-0.9161`
- `market_context_high->equity_24h` score `24.0702` n `88` status `ready` deltaP `22.3642` edge `2.0959` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.9947` n `53` status `ready` deltaP `33.6487` edge `0.8041` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.4541` n `88` status `ready` deltaP `36.2374` edge `1.2235` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.4829` n `88` status `ready` deltaP `22.4747` edge `0.27` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4528` n `88` status `ready` deltaP `31.3762` edge `0.2172` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.9636` n `53` status `ready` deltaP `39.0791` edge `0.1074` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.4087` n `53` status `ready` deltaP `17.7155` edge `0.2372` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.2953` n `53` status `ready` deltaP `18.6091` edge `0.2993` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.6732` n `53` status `ready` deltaP `24.2723` edge `0.0863` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1944` n `53` status `ready` deltaP `20.5937` edge `0.0892` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9534` n `53` status `ready` deltaP `23.6442` edge `0.0306` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.675` n `53` status `ready` deltaP `22.2302` edge `0.2304` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2742` n `53` status `ready` deltaP `16.7269` edge `0.0248` maxDD `-0.4103`
- `market_context_high->unknown_24h` score `0.9908` n `88` status `ready` deltaP `5.019` edge `0.0632` maxDD `-0.4609`
- `news_risk_high->crypto_major_1h` score `0.649` n `53` status `ready` deltaP `18.1928` edge `0.0671` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6307` n `53` status `ready` deltaP `16.8455` edge `0.0665` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0489` n `88` status `ready` deltaP `6.4916` edge `0.0203` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.2895` n `53` status `ready` deltaP `-2.9488` edge `0.029` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.3329` n `88` status `ready` deltaP `15.7986` edge `0.0269` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
