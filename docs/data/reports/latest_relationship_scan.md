# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T10:52:30.030190+00:00`
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

- `news_risk_high->crypto_major_24h` score `27.9172` n `92` status `ready` deltaP `9.8505` edge `2.7561` maxDD `-32.9603`
- `news_risk_high->crypto_alt_24h` score `26.4865` n `92` status `ready` deltaP `18.6292` edge `2.378` maxDD `-19.2655`
- `market_context_high->unknown_4h` score `17.7592` n `62` status `ready` deltaP `1.5637` edge `1.4845` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.1768` n `99` status `ready` deltaP `23.3956` edge `0.4797` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.0539` n `59` status `ready` deltaP `32.3564` edge `0.3413` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.5887` n `99` status `ready` deltaP `22.4809` edge `0.3583` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0231` n `62` status `ready` deltaP `34.7217` edge `0.1171` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0582` n `101` status `ready` deltaP `16.5308` edge `0.1912` maxDD `-2.058`
- `news_risk_high->equity_24h` score `2.4811` n `92` status `ready` deltaP `21.7618` edge `0.1577` maxDD `-3.3484`
- `news_risk_high->crypto_major_1h` score `2.2451` n `101` status `ready` deltaP `18.4769` edge `0.1162` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.1982` n `62` status `ready` deltaP `28.6241` edge `0.0097` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.4256` n `70` status `ready` deltaP `17.4551` edge `0.0318` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.409` n `59` status `ready` deltaP `17.4023` edge `0.0056` maxDD `-0.0027`
- `news_risk_high->commodity_24h` score `0.8168` n `92` status `ready` deltaP `21.0447` edge `0.095` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.6954` n `99` status `ready` deltaP `17.8292` edge `0.0445` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.6516` n `92` status `ready` deltaP `20.2295` edge `0.0331` maxDD `-2.4203`
- `news_risk_high->metal_1h` score `0.6161` n `101` status `ready` deltaP `14.4483` edge `0.0152` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.2903` n `101` status `ready` deltaP `6.1125` edge `0.024` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.272` n `70` status `ready` deltaP `6.6382` edge `0.0042` maxDD `-0.063`
- `market_context_high->metal_1h` score `0.0066` n `70` status `ready` deltaP `3.3875` edge `0.0048` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
