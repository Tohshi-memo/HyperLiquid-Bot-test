# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T09:37:26.078252+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11184`

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

- `news_risk_high->unknown_4h` score `397.1302` n `78` status `ready` deltaP `-22.303` edge `33.3322` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.8496` n `78` status `ready` deltaP `45.5128` edge `1.5565` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.661` n `78` status `ready` deltaP `18.4028` edge `1.6824` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.5494` n `78` status `ready` deltaP `35.2164` edge `1.2914` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.109` n `78` status `ready` deltaP `48.4642` edge `1.114` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7173` n `78` status `ready` deltaP `62.2863` edge `0.3288` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5897` n `78` status `ready` deltaP `39.0091` edge `0.3345` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9781` n `52` status `ready` deltaP `38.0208` edge `0.2447` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9781` n `52` status `ready` deltaP `38.0208` edge `0.2447` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6811` n `137` status `ready` deltaP `30.7215` edge `0.2378` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.7642` n `52` status `ready` deltaP `43.563` edge `0.0275` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.7642` n `52` status `ready` deltaP `43.563` edge `0.0275` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.3672` n `137` status `ready` deltaP `40.3766` edge `0.033` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9167` n `52` status `ready` deltaP `24.7655` edge `0.0296` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9167` n `52` status `ready` deltaP `24.7655` edge `0.0296` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8165` n `149` status `ready` deltaP `21.2678` edge `0.0514` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8162` n `149` status `ready` deltaP `13.2169` edge `0.0176` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7217` n `78` status `ready` deltaP `17.5735` edge `0.0382` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
