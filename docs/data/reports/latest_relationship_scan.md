# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T21:22:24.616525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1490.9478` n `98` status `ready` deltaP `3.4722` edge `124.2225` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.3808` n `32` status `ready` deltaP `65.1042` edge `3.835` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.5156` n `32` status `ready` deltaP `55.6402` edge `1.3387` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.4956` n `98` status `ready` deltaP `46.5384` edge `2.0034` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6377` n `98` status `ready` deltaP `32.7735` edge `1.8705` maxDD `-13.3222`
- `news_risk_high->crypto_major_24h` score `14.5648` n `32` status `ready` deltaP `25.1736` edge `1.8138` maxDD `-6.8139`
- `news_risk_high->index_24h` score `8.4001` n `32` status `ready` deltaP `56.4236` edge `0.3542` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.5089` n `32` status `ready` deltaP `54.8611` edge `0.26` maxDD `0.0`
- `news_risk_high->metal_4h` score `7.0246` n `32` status `ready` deltaP `55.8689` edge `0.2174` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.9641` n `32` status `ready` deltaP `27.6946` edge `0.3342` maxDD `-0.4122`
- `news_risk_high->crypto_major_4h` score `4.8574` n `32` status `ready` deltaP `20.4268` edge `0.3113` maxDD `-1.7491`
- `news_risk_high->crypto_alt_4h` score `4.7399` n `32` status `ready` deltaP `29.9543` edge `0.4847` maxDD `-4.137`
- `news_risk_high->index_4h` score `4.272` n `32` status `ready` deltaP `35.4421` edge `0.1422` maxDD `-0.1319`
- `news_risk_high->crypto_alt_24h` score `3.8797` n `32` status `ready` deltaP `3.8194` edge `0.9225` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.624` n `32` status `ready` deltaP `27.6946` edge `0.0558` maxDD `-0.0743`
- `news_risk_high->crypto_major_1h` score `2.4949` n `32` status `ready` deltaP `17.2717` edge `0.1279` maxDD `-1.4777`
- `news_risk_high->index_1h` score `1.8862` n `32` status `ready` deltaP `21.8937` edge `0.033` maxDD `-0.0751`
- `news_risk_high->crypto_alt_1h` score `1.8618` n `32` status `ready` deltaP `21.4446` edge `0.1484` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `1.4749` n `32` status `ready` deltaP `24.7713` edge `0.0493` maxDD `-0.3611`
- `market_context_high->metal_1h` score `-0.4758` n `98` status `ready` deltaP `-0.3666` edge `0.0016` maxDD `-2.1461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
