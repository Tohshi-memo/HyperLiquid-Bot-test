# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T11:07:32.574488+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `26.7883` n `93` status `ready` deltaP `9.2294` edge `2.698` maxDD `-35.1737`
- `news_risk_high->crypto_alt_24h` score `25.3592` n `93` status `ready` deltaP `17.938` edge `2.3192` maxDD `-21.3748`
- `market_context_high->unknown_4h` score `18.8857` n `61` status `ready` deltaP `1.4844` edge `1.5789` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9931` n `100` status `ready` deltaP `22.75` edge `0.4687` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.9873` n `58` status `ready` deltaP `32.0642` edge `0.3377` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.4627` n `100` status `ready` deltaP `21.8354` edge `0.3521` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.01` n `61` status `ready` deltaP `34.4837` edge `0.1176` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0402` n `101` status `ready` deltaP `16.3811` edge `0.1907` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.3017` n `61` status `ready` deltaP `29.873` edge `0.01` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2451` n `101` status `ready` deltaP `18.4769` edge `0.1162` maxDD `-2.8494`
- `news_risk_high->equity_24h` score `2.1874` n `93` status `ready` deltaP `20.8502` edge `0.1469` maxDD `-3.6227`
- `market_context_high->fx_24h` score `1.4349` n `58` status `ready` deltaP `17.5467` edge `0.0068` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3813` n `69` status `ready` deltaP `17.0203` edge `0.031` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `0.8521` n `93` status `ready` deltaP `21.3486` edge `0.0975` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.6463` n `100` status `ready` deltaP `17.3049` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.5921` n `93` status `ready` deltaP `19.3997` edge `0.031` maxDD `-2.4203`
- `market_context_high->fx_1h` score `0.3824` n `69` status `ready` deltaP `7.3787` edge `0.0043` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2771` n `101` status `ready` deltaP `5.9628` edge `0.0239` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.0823` n `69` status `ready` deltaP `4.1743` edge `0.0051` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
