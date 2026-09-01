# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T20:52:26.960373+00:00`
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

- `risk_on_high->unknown_4h` score `7.2643` n `107` status `ready` deltaP `19.763` edge `0.5354` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2643` n `107` status `ready` deltaP `19.763` edge `0.5354` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8109` n `151` status `ready` deltaP `16.0556` edge `0.4467` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.9008` n `107` status `ready` deltaP `3.3718` edge `0.1936` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.9008` n `107` status `ready` deltaP `3.3718` edge `0.1936` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.77` n `151` status `ready` deltaP `2.7343` edge `0.1923` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.1905` n `59` status `ready` deltaP `0.8373` edge `0.1283` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1257` n `59` status `ready` deltaP `10.3349` edge `0.0009` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1232` n `107` status `ready` deltaP `12.5441` edge `0.0034` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1232` n `107` status `ready` deltaP `12.5441` edge `0.0034` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.108` n `107` status `ready` deltaP `8.2433` edge `0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.108` n `107` status `ready` deltaP `8.2433` edge `0.0034` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0348` n `107` status `ready` deltaP `19.5635` edge `0.0071` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0348` n `107` status `ready` deltaP `19.5635` edge `0.0071` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.0002` n `107` status `ready` deltaP `6.5226` edge `0.0553` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.0002` n `107` status `ready` deltaP `6.5226` edge `0.0553` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.159` n `107` status `ready` deltaP `7.7173` edge `0.0111` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.159` n `107` status `ready` deltaP `7.7173` edge `0.0111` maxDD `-2.3009`
- `news_risk_high->index_1h` score `-0.1833` n `59` status `ready` deltaP `2.8418` edge `-0.0071` maxDD `-0.8275`
- `risk_on_high->commodity_1h` score `-0.2105` n `107` status `ready` deltaP `3.0766` edge `0.0047` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
