# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T08:37:32.760151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_major_24h` score `38.5888` n `83` status `ready` deltaP `16.3027` edge `3.3353` maxDD `-14.5934`
- `news_risk_high->crypto_alt_24h` score `35.6489` n `83` status `ready` deltaP `26.483` edge `2.9321` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `7.3479` n `71` status `ready` deltaP `2.177` edge `0.6128` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.7049` n `68` status `ready` deltaP `34.5997` edge `0.3806` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.211` n `98` status `ready` deltaP `23.4476` edge `0.4822` maxDD `-7.675`
- `news_risk_high->equity_24h` score `5.3678` n `83` status `ready` deltaP `30.9551` edge `0.2691` maxDD `-0.9186`
- `news_risk_high->crypto_major_4h` score `4.6916` n `98` status `ready` deltaP `22.8378` edge `0.3645` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1521` n `71` status `ready` deltaP `36.4093` edge `0.1166` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0653` n `101` status `ready` deltaP `16.6805` edge `0.1908` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.3099` n `101` status `ready` deltaP `18.7763` edge `0.1196` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3092` n `71` status `ready` deltaP `30.3117` edge `0.0077` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `2.234` n `72` status `ready` deltaP `24.4844` edge `0.0398` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.1891` n `68` status `ready` deltaP `16.0641` edge `-0.0038` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8503` n `83` status `ready` deltaP `21.3792` edge `0.0509` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.8126` n `98` status `ready` deltaP `19.1295` edge `0.0456` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.7591` n `72` status `ready` deltaP `12.6664` edge `0.0046` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6796` n `101` status `ready` deltaP `15.1968` edge `0.0155` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.4585` n `83` status `ready` deltaP `17.9803` edge `0.0695` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3395` n `101` status `ready` deltaP `6.2622` edge `0.0271` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
