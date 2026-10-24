# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T23:37:33.103097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `21.4392` n `98` status `ready` deltaP `2.2244` edge `1.8053` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7573` n `60` status `ready` deltaP `23.5417` edge `0.0804` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.798` n `98` status `ready` deltaP `10.6988` edge `0.0514` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.0335` n `107` status `ready` deltaP `5.4718` edge `0.0108` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3143` n `107` status `ready` deltaP `0.957` edge `0.0029` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.8316` n `98` status `ready` deltaP `-2.0657` edge `0.0051` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0224` n `107` status `ready` deltaP `-1.9965` edge `-0.0067` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1176` n `107` status `ready` deltaP `-1.171` edge `-0.0059` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.0956` n `60` status `ready` deltaP `-6.875` edge `-0.0028` maxDD `-1.7464`
- `market_context_high->crypto_major_1h` score `-2.8052` n `107` status `ready` deltaP `-1.6649` edge `-0.0477` maxDD `-10.6638`
- `market_context_high->crypto_major_24h` score `-3.2495` n `60` status `ready` deltaP `-4.4445` edge `-0.1029` maxDD `-18.0591`
- `market_context_high->metal_4h` score `-3.5454` n `98` status `ready` deltaP `-12.1547` edge `-0.0313` maxDD `-5.9831`
- `market_context_high->metal_24h` score `-3.6683` n `60` status `ready` deltaP `-12.1875` edge `0.0139` maxDD `-7.4004`
- `market_context_high->crypto_alt_1h` score `-3.7592` n `107` status `ready` deltaP `-2.6317` edge `-0.0693` maxDD `-14.7805`
- `market_context_high->equity_1h` score `-4.0327` n `107` status `ready` deltaP `-1.1347` edge `-0.0956` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.0663` n `98` status `ready` deltaP `-25.4293` edge `-0.0527` maxDD `-5.3304`
- `market_context_high->index_24h` score `-7.9498` n `60` status `ready` deltaP `-37.8125` edge `-0.1721` maxDD `-7.0642`
- `market_context_high->unknown_1h` score `-8.2589` n `107` status `ready` deltaP `-0.9821` edge `-0.6328` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-10.253` n `60` status `ready` deltaP `-1.5972` edge `-0.4223` maxDD `-61.5234`
- `market_context_high->crypto_major_4h` score `-14.5976` n `98` status `ready` deltaP `-25.5817` edge `-0.3667` maxDD `-45.6714`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
