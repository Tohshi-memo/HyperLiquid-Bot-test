# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T14:37:31.317005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9386`

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

- `news_risk_high->crypto_major_24h` score `22.2784` n `98` status `ready` deltaP `7.9295` edge `2.4895` maxDD `-46.1999`
- `market_context_high->unknown_4h` score `22.1961` n `56` status `ready` deltaP `1.0453` edge `1.8577` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `20.1181` n `98` status `ready` deltaP `14.7463` edge `2.0663` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `5.9897` n `101` status `ready` deltaP `23.1873` edge `0.4655` maxDD `-7.675`
- `market_context_high->commodity_24h` score `4.6924` n `45` status `ready` deltaP `27.0834` edge `0.263` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.5224` n `101` status `ready` deltaP `21.9678` edge `0.3562` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3804` n `56` status `ready` deltaP `37.9137` edge `0.1256` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.1085` n `101` status `ready` deltaP `16.9799` edge `0.1924` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2703` n `101` status `ready` deltaP `18.6266` edge `0.1173` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8402` n `56` status `ready` deltaP `24.5644` edge `0.0111` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.7155` n `45` status `ready` deltaP `19.4792` edge `0.0173` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3747` n `56` status `ready` deltaP `15.6116` edge `0.038` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0635` n `98` status `ready` deltaP `22.775` edge `0.1151` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7402` n `56` status `ready` deltaP `11.5804` edge `0.0061` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.703` n `101` status `ready` deltaP `18.0134` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.6521` n `98` status `ready` deltaP `16.571` edge `0.0848` maxDD `-4.941`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.3031` n `56` status `ready` deltaP `8.1801` edge `0.0067` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2515` n `98` status `ready` deltaP `15.5046` edge `0.0133` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2352` n `101` status `ready` deltaP `5.364` edge `0.0244` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
