# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T12:07:30.462449+00:00`
- Price records: `672`
- Market context records: `6601`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.3188` n `167` status `ready` deltaP `3.3597` edge `0.5842` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0352` n `210` status `ready` deltaP `-5.1297` edge `0.2939` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.5122` n `167` status `ready` deltaP `9.0007` edge `0.1695` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3012` n `210` status `ready` deltaP `1.7565` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4836` n `210` status `ready` deltaP `6.2988` edge `0.0226` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.558` n `210` status `ready` deltaP `0.0399` edge `-0.0035` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5615` n `210` status `ready` deltaP `-0.5304` edge `0.0035` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6801` n `210` status `ready` deltaP `4.0947` edge `0.0168` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9301` n `210` status `ready` deltaP `8.9896` edge `0.0088` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.2105` n `210` status `ready` deltaP `-0.2119` edge `-0.0043` maxDD `-5.6246`
- `market_context_high->equity_1h` score `-1.234` n `210` status `ready` deltaP `1.4828` edge `-0.0017` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.353` n `210` status `ready` deltaP `-4.3256` edge `-0.0032` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6262` n `210` status `ready` deltaP `2.0586` edge `-0.001` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7507` n `210` status `ready` deltaP `-17.5232` edge `0.2115` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9363` n `210` status `ready` deltaP `6.3618` edge `0.0408` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.2193` n `210` status `ready` deltaP `-2.1109` edge `0.0156` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2406` n `210` status `ready` deltaP `3.4088` edge `0.0302` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.8475` n `167` status `ready` deltaP `-5.8606` edge `-0.0007` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.6886` n `167` status `ready` deltaP `0.1947` edge `0.0576` maxDD `-10.6357`
- `market_context_high->equity_4h` score `-4.944` n `210` status `ready` deltaP `6.2863` edge `-0.027` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
