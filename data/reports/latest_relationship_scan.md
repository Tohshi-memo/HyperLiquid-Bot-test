# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T03:37:37.038170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `365.3914` n `50` status `ready` deltaP `11.024` edge `30.3807` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.2273` n `50` status `ready` deltaP `10.3659` edge `24.3665` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9712` n `70` status `ready` deltaP `24.1518` edge `0.9459` maxDD `-6.0784`
- `market_context_high->crypto_alt_24h` score `11.1713` n `50` status `ready` deltaP `22.4375` edge `0.9517` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.385` n `70` status `ready` deltaP `33.7351` edge `0.689` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9254` n `50` status `ready` deltaP `31.3056` edge `0.6767` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.8115` n `95` status `ready` deltaP `32.1999` edge `0.5707` maxDD `-6.4195`
- `news_risk_high->crypto_major_4h` score `7.3171` n `95` status `ready` deltaP `27.7279` edge `0.465` maxDD `-1.2076`
- `market_context_high->crypto_major_4h` score `7.2723` n `50` status `ready` deltaP `16.7805` edge `0.5645` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.6747` n `70` status `ready` deltaP `12.1627` edge `0.5842` maxDD `-6.0583`
- `market_context_high->crypto_alt_4h` score `5.785` n `50` status `ready` deltaP `15.8841` edge `0.5051` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.3901` n `95` status `ready` deltaP `27.6412` edge `0.1595` maxDD `-2.9013`
- `news_risk_high->index_24h` score `3.1924` n `70` status `ready` deltaP `28.0208` edge `0.0951` maxDD `-0.2696`
- `market_context_high->crypto_alt_1h` score `3.1642` n `50` status `ready` deltaP `14.2036` edge `0.2353` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9869` n `50` status `ready` deltaP `13.4012` edge `0.2046` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7665` n `50` status `ready` deltaP `30.8598` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `1.7719` n `95` status `ready` deltaP `9.4012` edge `0.1382` maxDD `-1.5904`
- `news_risk_high->crypto_alt_1h` score `1.6977` n `95` status `ready` deltaP `7.151` edge `0.1457` maxDD `-2.4854`
- `news_risk_high->metal_24h` score `1.6866` n `70` status `ready` deltaP `9.6329` edge `0.1867` maxDD `-2.8298`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
