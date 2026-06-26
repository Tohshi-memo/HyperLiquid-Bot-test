# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T01:52:31.282385+00:00`
- Price records: `672`
- Market context records: `4781`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `8.268` n `122` status `ready` deltaP `12.8792` edge `0.6449` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.4571` n `122` status `ready` deltaP `17.5005` edge `0.6258` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8896` n `107` status `ready` deltaP `11.52` edge `0.173` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1096` n `122` status `ready` deltaP `11.8153` edge `0.0525` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0842` n `122` status `ready` deltaP `5.0824` edge `0.0319` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4535` n `122` status `ready` deltaP `2.6689` edge `0.0017` maxDD `-1.5439`
- `market_context_high->equity_4h` score `-0.509` n `122` status `ready` deltaP `6.7098` edge `0.0586` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.5109` n `122` status `ready` deltaP `5.6228` edge `0.0039` maxDD `-5.5505`
- `market_context_high->fx_1h` score `-0.8873` n `122` status `ready` deltaP `-0.8835` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.895` n `122` status `ready` deltaP `0.8197` edge `-0.0033` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.477` n `122` status `ready` deltaP `-2.2455` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1513` n `107` status `ready` deltaP `20.0967` edge `0.1011` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2914` n `122` status `ready` deltaP `-1.097` edge `-0.0689` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.2898` n `122` status `ready` deltaP `0.1497` edge `-0.0512` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.3469` n `107` status `ready` deltaP `-15.247` edge `-0.0223` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.6098` n `122` status `ready` deltaP `-0.0638` edge `-0.0747` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.1484` n `122` status `ready` deltaP `3.3736` edge `-0.0401` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6834` n `107` status `ready` deltaP `-5.1029` edge `-0.1062` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.4565` n `122` status `ready` deltaP `2.1341` edge `-0.1753` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.5768` n `122` status `ready` deltaP `4.8581` edge `-0.3079` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
