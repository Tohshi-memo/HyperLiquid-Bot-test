# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T07:52:29.061899+00:00`
- Price records: `672`
- Market context records: `4912`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_1h` score `14.8598` n `109` status `ready` deltaP `9.6715` edge `1.2156` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.8818` n `109` status `ready` deltaP `24.0154` edge `0.7148` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.6606` n `109` status `ready` deltaP `22.0169` edge `0.5435` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4938` n `109` status `ready` deltaP `18.9542` edge `0.5372` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.3614` n `91` status `ready` deltaP `23.676` edge `0.3232` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1949` n `109` status `ready` deltaP `8.8512` edge `0.1068` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8424` n `109` status `ready` deltaP `11.6176` edge `0.1687` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5648` n `109` status `ready` deltaP `7.2529` edge `0.1279` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.4859` n `109` status `ready` deltaP `10.2372` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4291` n `109` status `ready` deltaP `7.7789` edge `0.1054` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2764` n `109` status `ready` deltaP `5.0266` edge `0.0607` maxDD `-2.7019`
- `market_context_high->commodity_1h` score `-0.1856` n `109` status `ready` deltaP `3.8826` edge `0.0163` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2817` n `109` status `ready` deltaP `0.5123` edge `0.0311` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5085` n `109` status `ready` deltaP `-0.1209` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7511` n `109` status `ready` deltaP `-0.4587` edge `0.0038` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7832` n `109` status `ready` deltaP `7.1549` edge `0.0057` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.432` n `109` status `ready` deltaP `-8.0248` edge `-0.0045` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.6031` n `91` status `ready` deltaP `-3.789` edge `-0.0073` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.4854` n `91` status `ready` deltaP `17.2199` edge `0.0223` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.6361` n `91` status `ready` deltaP `-6.7976` edge `-0.1405` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
