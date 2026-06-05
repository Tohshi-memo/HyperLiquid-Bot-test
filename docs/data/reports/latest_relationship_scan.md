# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T19:22:22.827694+00:00`
- Price records: `672`
- Market context records: `2998`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `18.4756` n `98` status `ready` deltaP `6.3315` edge `1.8891` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.382` n `98` status `ready` deltaP `42.6411` edge `0.7586` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.8263` n `98` status `ready` deltaP `18.5693` edge `0.9082` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.8955` n `98` status `ready` deltaP `17.3045` edge `0.8263` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.5158` n `98` status `ready` deltaP `17.0883` edge `0.4438` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.1977` n `102` status `ready` deltaP `16.5381` edge `0.1376` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.3288` n `102` status `ready` deltaP `18.6484` edge `0.1148` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.0193` n `102` status `ready` deltaP `14.0543` edge `0.179` maxDD `-9.0276`
- `market_context_high->index_1h` score `0.0428` n `105` status `ready` deltaP `5.8369` edge `0.0268` maxDD `-2.4852`
- `market_context_high->commodity_1h` score `-0.0396` n `105` status `ready` deltaP `1.1834` edge `0.02` maxDD `-0.9706`
- `market_context_high->crypto_alt_4h` score `-0.2886` n `102` status `ready` deltaP `22.6536` edge `0.3621` maxDD `-38.3432`
- `market_context_high->equity_1h` score `-0.2947` n `105` status `ready` deltaP `3.9992` edge `0.0375` maxDD `-5.1553`
- `market_context_high->fx_1h` score `-0.3424` n `105` status `ready` deltaP `-1.8777` edge `0.0008` maxDD `-0.2412`
- `market_context_high->crypto_alt_1h` score `-1.0008` n `105` status `ready` deltaP `6.6396` edge `0.0303` maxDD `-13.8964`
- `market_context_high->fx_4h` score `-1.1149` n `102` status `ready` deltaP `-9.8039` edge `0.0003` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.1803` n `105` status `ready` deltaP `-2.448` edge `-0.0101` maxDD `-6.3255`
- `market_context_high->unknown_4h` score `-1.3547` n `102` status `ready` deltaP `-0.8489` edge `-0.0019` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.4668` n `105` status `ready` deltaP `4.2187` edge `0.0005` maxDD `-14.6674`
- `market_context_high->unknown_1h` score `-1.8352` n `105` status `ready` deltaP `1.3872` edge `-0.0891` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.928` n `98` status `ready` deltaP `-7.0011` edge `-0.0268` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
