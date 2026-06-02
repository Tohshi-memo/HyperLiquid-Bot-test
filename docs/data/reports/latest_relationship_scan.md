# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T05:22:19.763957+00:00`
- Price records: `672`
- Market context records: `2632`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.572` n `144` status `ready` deltaP `18.2292` edge `0.5423` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1307` n `144` status `ready` deltaP `25.254` edge `0.5271` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3592` n `144` status `ready` deltaP `14.7357` edge `0.3627` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.403` n `144` status `ready` deltaP `11.4583` edge `0.1386` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2602` n `144` status `ready` deltaP `11.003` edge `0.1504` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `1.1552` n `144` status `ready` deltaP `3.4722` edge `0.689` maxDD `-37.9373`
- `market_context_high->unknown_4h` score `1.1229` n `144` status `ready` deltaP `8.1978` edge `0.1439` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6559` n `144` status `ready` deltaP `8.3209` edge `0.1186` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3575` n `144` status `ready` deltaP `9.3666` edge `0.0515` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1108` n `144` status `ready` deltaP `4.1958` edge `0.0122` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.2548` n `144` status `ready` deltaP `6.645` edge `0.0223` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.2876` n `144` status `ready` deltaP `2.5616` edge `0.0173` maxDD `-2.0009`
- `market_context_high->metal_1h` score `-0.548` n `144` status `ready` deltaP `-0.0416` edge `0.0048` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6944` n `144` status `ready` deltaP `-1.1976` edge `0.0032` maxDD `-0.2464`
- `market_context_high->commodity_4h` score `-0.831` n `144` status `ready` deltaP `5.6741` edge `0.0499` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-0.9836` n `144` status `ready` deltaP `-1.6966` edge `0.0132` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.9857` n `144` status `ready` deltaP `2.5576` edge `0.029` maxDD `-4.5886`
- `market_context_high->fx_24h` score `-1.029` n `144` status `ready` deltaP `2.2569` edge `-0.0036` maxDD `-1.4425`
- `market_context_high->fx_4h` score `-1.0743` n `144` status `ready` deltaP `-2.1511` edge `0.0092` maxDD `-0.7507`
- `market_context_high->equity_4h` score `-1.4176` n `144` status `ready` deltaP `1.2026` edge `0.0143` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
