# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T22:22:24.465139+00:00`
- Price records: `672`
- Market context records: `3012`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `20.7951` n `98` status `ready` deltaP `8.4148` edge `2.0685` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.8432` n `98` status `ready` deltaP `43.3355` edge `0.7924` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.4598` n `98` status `ready` deltaP `20.6527` edge `0.9471` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.8742` n `98` status `ready` deltaP `19.3878` edge `0.9773` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.7701` n `98` status `ready` deltaP `18.998` edge `0.5356` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4862` n `105` status `ready` deltaP `18.57` edge `0.1481` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6232` n `105` status `ready` deltaP `13.313` edge `0.1716` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.3215` n `105` status `ready` deltaP `17.8107` edge `0.1005` maxDD `-9.9084`
- `market_context_high->equity_1h` score `-0.1474` n `115` status `ready` deltaP `5.6873` edge `0.051` maxDD `-5.6254`
- `market_context_high->commodity_1h` score `-0.2446` n `115` status `ready` deltaP `-0.164` edge `0.012` maxDD `-1.7142`
- `market_context_high->crypto_alt_4h` score `-0.2678` n `105` status `ready` deltaP `22.2707` edge `0.372` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.3247` n `115` status `ready` deltaP `5.2317` edge `0.0249` maxDD `-4.1126`
- `market_context_high->fx_1h` score `-0.5351` n `115` status `ready` deltaP `-1.333` edge `0.0009` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.7078` n `115` status `ready` deltaP `7.0919` edge `0.1067` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.9212` n `115` status `ready` deltaP `3.8271` edge `-0.0292` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9799` n `115` status `ready` deltaP `4.8685` edge `0.0682` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1934` n `105` status `ready` deltaP `-10.9524` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.7155` n `105` status `ready` deltaP `-2.7628` edge `-0.0192` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.7285` n `115` status `ready` deltaP `-1.3395` edge `-0.0033` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.8012` n `98` status `ready` deltaP `-5.6122` edge `-0.0255` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
