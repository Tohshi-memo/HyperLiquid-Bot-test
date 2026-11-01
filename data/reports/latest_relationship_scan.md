# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T23:07:28.614088+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7053`

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

- `market_context_high->unknown_24h` score `7542.8335` n `55` status `ready` deltaP `1.3889` edge `628.5602` maxDD `0.0`
- `market_context_high->unknown_4h` score `343.121` n `55` status `ready` deltaP `7.1757` edge `28.5499` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `45.6122` n `55` status `ready` deltaP `4.3604` edge `3.783` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2764` n `55` status `ready` deltaP `42.7999` edge `1.5113` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.3014` n `94` status `ready` deltaP `31.1355` edge `1.0365` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.2234` n `55` status `ready` deltaP `49.6528` edge `0.1876` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2074` n `55` status `ready` deltaP `24.5122` edge `0.3833` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8933` n `55` status `ready` deltaP `40.7545` edge `0.2505` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6397` n `55` status `ready` deltaP `31.3498` edge `0.2946` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.3714` n `55` status `ready` deltaP `6.3525` edge `0.3088` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0886` n `55` status `ready` deltaP `29.5427` edge `0.0855` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5295` n `126` status `ready` deltaP `10.3852` edge `0.2802` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4209` n `55` status `ready` deltaP `10.685` edge `0.3068` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9563` n `55` status `ready` deltaP `-4.1256` edge `0.4301` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7627` n `55` status `ready` deltaP `20.6374` edge `0.0518` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6076` n `55` status `ready` deltaP `3.7752` edge `0.1613` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.4567` n `55` status `ready` deltaP `4.0746` edge `0.1613` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4527` n `55` status `ready` deltaP `8.3315` edge `0.1265` maxDD `-2.2118`
- `market_context_high->metal_1h` score `1.0169` n `55` status `ready` deltaP `12.5231` edge `0.0261` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5638` n `55` status `ready` deltaP `13.6364` edge `-0.0002` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
