# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T03:52:27.387988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `71.9694` n `47` status `ready` deltaP `10.5651` edge `5.9341` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `37.4527` n `46` status `ready` deltaP `24.8189` edge `2.9712` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `22.0241` n `46` status `ready` deltaP `19.7917` edge `1.7034` maxDD `0.0`
- `market_context_high->equity_24h` score `21.6868` n `46` status `ready` deltaP `22.2147` edge `1.6692` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.2693` n `46` status `ready` deltaP `31.2425` edge `0.4062` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9791` n `103` status `ready` deltaP `14.6889` edge `0.4168` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7012` n `103` status `ready` deltaP `18.195` edge `0.3282` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `3.7115` n `103` status `ready` deltaP `-2.8721` edge `1.2327` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.5821` n `103` status `ready` deltaP `13.7565` edge `0.1725` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5574` n `47` status `ready` deltaP `30.0629` edge `0.0281` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.376` n `103` status `ready` deltaP `23.0532` edge `0.1622` maxDD `-2.431`
- `market_context_high->metal_24h` score `2.3393` n `46` status `ready` deltaP `25.2189` edge `0.0502` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.0888` n `103` status `ready` deltaP `16.1517` edge `0.1099` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.6034` n `47` status `ready` deltaP `12.7237` edge `0.0906` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5722` n `103` status `ready` deltaP `23.0716` edge `0.0408` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.221` n `103` status `ready` deltaP `29.6639` edge `0.1219` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8565` n `47` status `ready` deltaP `13.5622` edge `0.0088` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6925` n `103` status `ready` deltaP `15.8014` edge `0.0117` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6837` n `47` status `ready` deltaP `9.67` edge `0.0328` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3937` n `103` status `ready` deltaP `15.1847` edge `0.045` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
