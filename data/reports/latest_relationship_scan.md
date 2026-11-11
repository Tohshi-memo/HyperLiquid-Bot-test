# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T04:07:26.507847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `79.6042` n `88` status `ready` deltaP `7.525` edge `6.6283` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.5182` n `88` status `ready` deltaP `32.2601` edge `2.9006` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1217` n `37` status `ready` deltaP `33.6314` edge `0.8148` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.73` n `88` status `ready` deltaP `32.2443` edge `1.2855` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1533` n `88` status `ready` deltaP `31.8497` edge `0.3467` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8845` n `47` status `ready` deltaP `20.6937` edge `0.257` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.3054` n `88` status `ready` deltaP `28.5985` edge `0.1401` maxDD `-1.4245`
- `news_risk_high->commodity_4h` score `3.2463` n `37` status `ready` deltaP `23.8464` edge `0.1369` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4275` n `37` status `ready` deltaP `24.8723` edge `0.0801` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2095` n `37` status `ready` deltaP `28.6544` edge `0.2561` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.8407` n `37` status `ready` deltaP `20.2415` edge `0.2498` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.6744` n `37` status `ready` deltaP `30.9287` edge `0.0461` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.5805` n `47` status `ready` deltaP `20.544` edge `0.0202` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4477` n `47` status `ready` deltaP `18.8655` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0915` n `47` status `ready` deltaP `22.7577` edge `0.082` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7469` n `47` status `ready` deltaP `20.9294` edge `0.0614` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2084` n `47` status `ready` deltaP `-4.2075` edge `0.0348` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.416` n `88` status `ready` deltaP `2.5381` edge `-0.002` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4767` n `88` status `ready` deltaP `2.7491` edge `0.0096` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6776` n `88` status `ready` deltaP `1.5798` edge `0.0132` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
