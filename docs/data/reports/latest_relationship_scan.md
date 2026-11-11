# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T19:52:27.472426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11774`

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

- `market_context_high->unknown_4h` score `79.6451` n `88` status `ready` deltaP `8.592` edge `6.6246` maxDD `-0.9161`
- `market_context_high->equity_24h` score `24.3625` n `88` status `ready` deltaP `22.5378` edge `2.1191` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.9753` n `53` status `ready` deltaP `33.4963` edge `0.8035` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.5333` n `88` status `ready` deltaP `36.411` edge `1.2325` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.5304` n `88` status `ready` deltaP `22.6483` edge `0.2728` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.448` n `88` status `ready` deltaP `31.3762` edge `0.2168` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.9588` n `53` status `ready` deltaP `39.0791` edge `0.107` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.4039` n `53` status `ready` deltaP `17.7155` edge `0.2368` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.2795` n `53` status `ready` deltaP `18.4567` edge `0.299` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.6502` n `53` status `ready` deltaP `24.1199` edge `0.0854` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1944` n `53` status `ready` deltaP `20.5937` edge `0.0892` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9414` n `53` status `ready` deltaP `23.4945` edge `0.0306` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6538` n `53` status `ready` deltaP `22.0777` edge `0.2287` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.273` n `53` status `ready` deltaP `16.7269` edge `0.0247` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6592` n `53` status `ready` deltaP `18.3425` edge `0.0674` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6408` n `53` status `ready` deltaP `16.9952` edge `0.0668` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0609` n `88` status `ready` deltaP `6.3419` edge `0.0203` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3099` n `53` status `ready` deltaP `-3.0985` edge `0.0283` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.3516` n `88` status `ready` deltaP `15.625` edge `0.0265` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5391` n `88` status `ready` deltaP `1.6399` edge `-0.0118` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
