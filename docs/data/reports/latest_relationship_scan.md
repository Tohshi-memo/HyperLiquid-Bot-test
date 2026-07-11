# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T10:37:26.476897+00:00`
- Price records: `672`
- Market context records: `6382`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.1577` n `32` status `ready` deltaP `37.6736` edge `0.9434` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3872` n `32` status `ready` deltaP `53.125` edge `0.1781` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.295` n `32` status `ready` deltaP `17.5347` edge `0.5117` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.2339` n `32` status `ready` deltaP `36.8056` edge `0.128` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9352` n `32` status `ready` deltaP `40.625` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3847` n `32` status `ready` deltaP `28.7425` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5294` n `32` status `ready` deltaP `14.8765` edge `0.1436` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8683` n `32` status `ready` deltaP `10.872` edge `0.085` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4875` n `220` status `ready` deltaP `15.1136` edge `0.0414` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1818` n `228` status `ready` deltaP `-5.6151` edge `0.1534` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1812` n `220` status `ready` deltaP `9.1852` edge `0.0215` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2297` n `32` status `ready` deltaP `6.8301` edge `-0.0302` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2468` n `146` status `ready` deltaP `19.6205` edge `0.0944` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3892` n `228` status `ready` deltaP `3.7452` edge `0.0029` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.625` n `228` status `ready` deltaP `-1.6467` edge `0.0028` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.7091` n `32` status `ready` deltaP `-2.3952` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7101` n `228` status `ready` deltaP `-0.6435` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7346` n `32` status `ready` deltaP `0.5208` edge `-0.0105` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.8416` n `146` status `ready` deltaP `-5.7886` edge `0.1171` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.8743` n `220` status `ready` deltaP `7.0981` edge `0.0497` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
