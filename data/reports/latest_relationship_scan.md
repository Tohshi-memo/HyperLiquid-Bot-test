# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T06:07:31.143862+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11816`

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

- `news_risk_high->unknown_24h` score `3370.0128` n `100` status `ready` deltaP `-0.6528` edge `280.8432` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8961` n `47` status `ready` deltaP `8.4693` edge `5.7753` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.5009` n `47` status `ready` deltaP `24.6934` edge `3.9164` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.8985` n `47` status `ready` deltaP `22.6987` edge `2.3782` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3179` n `47` status `ready` deltaP `33.3739` edge `1.9229` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.2942` n `47` status `ready` deltaP `31.6378` edge `0.4099` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4437` n `47` status `ready` deltaP `28.982` edge `0.1176` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.6875` n `47` status `ready` deltaP `16.8396` edge `0.1535` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.492` n `47` status `ready` deltaP `28.691` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.2551` n `47` status `ready` deltaP `11.3648` edge `0.0956` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1897` n `100` status `ready` deltaP `27.5139` edge `0.1352` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7571` n `47` status `ready` deltaP `12.2149` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5332` n `47` status `ready` deltaP `10.858` edge `0.0077` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4133` n `100` status `ready` deltaP `14.0208` edge `0.0411` maxDD `-2.344`
- `market_context_high->crypto_major_4h` score `0.396` n `47` status `ready` deltaP `4.5375` edge `0.0932` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.3362` n `47` status `ready` deltaP `5.2013` edge `0.0751` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1121` n `129` status `ready` deltaP `5.1722` edge `0.0041` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0481` n `47` status `ready` deltaP `9.4739` edge `0.0076` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
