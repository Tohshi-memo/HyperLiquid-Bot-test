# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T19:07:31.420725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6735`

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

- `market_context_high->unknown_24h` score `7300.3291` n `55` status `ready` deltaP `1.3889` edge `608.3515` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.7922` n `55` status `ready` deltaP `6.8708` edge `31.6912` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `52.7738` n `55` status `ready` deltaP `4.2107` edge `4.3808` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.172` n `55` status `ready` deltaP `42.7999` edge `1.5026` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2156` n `94` status `ready` deltaP `30.9619` edge `1.0305` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.4984` n `55` status `ready` deltaP `52.4306` edge `0.192` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1966` n `55` status `ready` deltaP `24.5122` edge `0.3824` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `6.1844` n `55` status `ready` deltaP `43.3586` edge `0.2574` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6793` n `55` status `ready` deltaP `31.3498` edge `0.2979` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5225` n `55` status `ready` deltaP `6.3525` edge `0.3214` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3347` n `55` status `ready` deltaP `31.5244` edge `0.0928` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5187` n `126` status `ready` deltaP `10.3852` edge `0.2793` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4092` n `55` status `ready` deltaP `10.685` edge `0.3053` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9005` n `55` status `ready` deltaP `-4.2992` edge `0.4241` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7078` n `55` status `ready` deltaP `19.8752` edge `0.0523` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6507` n `55` status `ready` deltaP `4.2243` edge `0.1619` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.5058` n `55` status `ready` deltaP `4.5237` edge `0.1624` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4815` n `55` status `ready` deltaP `8.6309` edge `0.1269` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.951` n `55` status `ready` deltaP `11.7746` edge `0.0256` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5389` n `55` status `ready` deltaP `13.1873` edge `-0.0004` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
