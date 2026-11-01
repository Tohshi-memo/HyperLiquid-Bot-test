# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T19:37:26.836807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6865`

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

- `market_context_high->unknown_24h` score `7332.5971` n `55` status `ready` deltaP `1.3889` edge `611.0405` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.9088` n `55` status `ready` deltaP `7.0233` edge `31.6999` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `52.385` n `55` status `ready` deltaP `4.2107` edge `4.3484` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1912` n `55` status `ready` deltaP `42.7999` edge `1.5042` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2384` n `94` status `ready` deltaP `30.9619` edge `1.0324` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.4647` n `55` status `ready` deltaP `52.0833` edge `0.1915` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2254` n `55` status `ready` deltaP `24.5122` edge `0.3848` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `6.1495` n `55` status `ready` deltaP `43.0114` edge `0.2568` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6925` n `55` status `ready` deltaP `31.3498` edge `0.299` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5286` n `55` status `ready` deltaP `6.3525` edge `0.3219` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3299` n `55` status `ready` deltaP `31.5244` edge `0.0924` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5475` n `126` status `ready` deltaP `10.3852` edge `0.2817` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4193` n `55` status `ready` deltaP `10.685` edge `0.3066` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9153` n `55` status `ready` deltaP `-4.2992` edge `0.426` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7358` n `55` status `ready` deltaP `20.1801` edge `0.0526` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6543` n `55` status `ready` deltaP `4.2243` edge `0.1622` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.525` n `55` status `ready` deltaP `4.5237` edge `0.164` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.5067` n `55` status `ready` deltaP `8.7806` edge `0.128` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9642` n `55` status `ready` deltaP `11.9243` edge `0.0257` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5475` n `55` status `ready` deltaP `13.337` edge `-0.0003` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
