# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T19:07:26.764398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.3223` n `107` status `ready` deltaP `20.0678` edge `0.5382` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3223` n `107` status `ready` deltaP `20.0678` edge `0.5382` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8689` n `151` status `ready` deltaP `16.3604` edge `0.4495` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0615` n `107` status `ready` deltaP `4.27` edge `0.201` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0615` n `107` status `ready` deltaP `4.27` edge `0.201` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9307` n `151` status `ready` deltaP `3.6325` edge `0.1997` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3512` n `59` status `ready` deltaP `1.7355` edge `0.1357` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1769` n `59` status `ready` deltaP `10.9446` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->commodity_24h` score `0.1162` n `107` status `ready` deltaP `6.5226` edge `0.065` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.1162` n `107` status `ready` deltaP `6.5226` edge `0.065` maxDD `-0.5706`
- `risk_on_high->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.078` n `107` status `ready` deltaP `11.7956` edge `0.0026` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.078` n `107` status `ready` deltaP `11.7956` edge `0.0026` maxDD `-1.699`
- `risk_on_high->index_4h` score `-0.026` n `107` status `ready` deltaP `18.6489` edge `0.0054` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.026` n `107` status `ready` deltaP `18.6489` edge `0.0054` maxDD `-3.6448`
- `market_context_high->commodity_1h` score `-0.1081` n `151` status `ready` deltaP `7.0756` edge `0.0088` maxDD `-1.5315`
- `risk_on_high->equity_1h` score `-0.1301` n `107` status `ready` deltaP `8.1664` edge `0.0118` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1301` n `107` status `ready` deltaP `8.1664` edge `0.0118` maxDD `-2.3009`
- `news_risk_high->commodity_24h` score `-0.132` n `59` status `ready` deltaP `3.3545` edge `-0.0141` maxDD `-0.2074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
