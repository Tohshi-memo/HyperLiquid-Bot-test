# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T07:22:24.376154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5173`

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

- `market_context_high->unknown_24h` score `6050.9275` n `33` status `ready` deltaP `1.3889` edge `504.2347` maxDD `0.0`
- `market_context_high->unknown_4h` score `614.0849` n `38` status `ready` deltaP `8.8415` edge `51.1148` maxDD `0.0`
- `market_context_high->unknown_1h` score `159.4117` n `38` status `ready` deltaP `7.6742` edge `13.2442` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.6206` n `33` status `ready` deltaP `41.5878` edge `1.3814` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `11.9436` n `99` status `ready` deltaP `30.2557` edge `0.966` maxDD `-9.7923`
- `market_context_high->commodity_24h` score `7.2851` n `33` status `ready` deltaP `42.5821` edge `0.3543` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.9042` n `33` status `ready` deltaP `49.1319` edge `0.2478` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2352` n `38` status `ready` deltaP `25.9387` edge `0.3761` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.8535` n `38` status `ready` deltaP `11.3688` edge `0.4822` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.887` n `38` status `ready` deltaP `23.8768` edge `0.2817` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.3801` n `38` status `ready` deltaP `12.5591` edge `0.238` maxDD `-1.2043`
- `market_context_high->crypto_alt_1h` score `2.7662` n `38` status `ready` deltaP `10.8257` edge `0.2025` maxDD `-1.5324`
- `news_risk_high->crypto_alt_4h` score `2.5161` n `126` status `ready` deltaP `10.2328` edge `0.2801` maxDD `-7.4246`
- `market_context_high->crypto_major_1h` score `2.4852` n `38` status `ready` deltaP `12.8585` edge `0.1604` maxDD `-1.1219`
- `market_context_high->index_4h` score `2.1426` n `38` status `ready` deltaP `21.2853` edge `0.0623` maxDD `-0.3854`
- `market_context_high->crypto_alt_24h` score `1.8383` n `33` status `ready` deltaP `-6.108` edge `0.3457` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5866` n `38` status `ready` deltaP `18.6457` edge `0.0504` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.3747` n `38` status `ready` deltaP `17.972` edge `0.0119` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `1.1777` n `38` status `ready` deltaP `22.7294` edge `0.0407` maxDD `-1.633`
- `market_context_high->metal_1h` score `0.4246` n `38` status `ready` deltaP `9.0057` edge `0.0201` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
