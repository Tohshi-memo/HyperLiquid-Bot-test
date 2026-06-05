# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T07:22:28.381516+00:00`
- Price records: `672`
- Market context records: `2948`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.9778` n `134` status `ready` deltaP `14.8943` edge `1.7072` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.0948` n `134` status `ready` deltaP `18.4105` edge `0.7522` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.5104` n `134` status `ready` deltaP `16.7755` edge `0.5605` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `3.4078` n `134` status `ready` deltaP `19.5403` edge `0.4033` maxDD `-10.3004`
- `market_context_high->index_24h` score `3.0285` n `134` status `ready` deltaP `14.332` edge `0.2549` maxDD `-2.5127`
- `market_context_high->equity_4h` score `1.7904` n `135` status `ready` deltaP `11.1145` edge `0.1712` maxDD `-4.3541`
- `market_context_high->index_4h` score `0.776` n `135` status `ready` deltaP `15.1852` edge `0.0824` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.7343` n `135` status `ready` deltaP `17.6434` edge `0.3997` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.291` n `135` status `ready` deltaP `3.7477` edge `0.1046` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1167` n `135` status `ready` deltaP `6.4305` edge `0.0215` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.1517` n `135` status `ready` deltaP `1.8131` edge `0.0518` maxDD `-2.1226`
- `market_context_high->crypto_alt_1h` score `-0.2199` n `135` status `ready` deltaP `6.8873` edge `0.1019` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.3366` n `135` status `ready` deltaP `-0.0942` edge `0.0033` maxDD `-0.1244`
- `market_context_high->crypto_major_1h` score `-0.5163` n `135` status `ready` deltaP `5.5866` edge `0.0835` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6315` n `135` status `ready` deltaP `0.4014` edge `0.0051` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.7667` n `135` status `ready` deltaP `-1.7332` edge `-0.0114` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.7893` n `135` status `ready` deltaP `0.4799` edge `0.0089` maxDD `-0.5631`
- `market_context_high->unknown_1h` score `-0.8554` n `135` status `ready` deltaP `1.2453` edge `-0.0065` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-1.1238` n `135` status `ready` deltaP `3.2712` edge `0.0228` maxDD `-9.7612`
- `market_context_high->crypto_major_4h` score `-1.298` n `135` status `ready` deltaP `8.645` edge `0.2885` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
