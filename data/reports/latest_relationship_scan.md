# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T01:37:20.570691+00:00`
- Price records: `672`
- Market context records: `2923`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.0556` n `142` status `ready` deltaP `13.4659` edge `1.4732` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.9283` n `142` status `ready` deltaP `15.6788` edge `0.6732` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.1098` n `142` status `ready` deltaP `13.7128` edge `0.4642` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.3806` n `142` status `ready` deltaP `11.4535` edge `0.2201` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8396` n `142` status `ready` deltaP `15.5516` edge `0.359` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.6219` n `142` status `ready` deltaP `7.6026` edge `0.1391` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6044` n `142` status `ready` deltaP `13.9106` edge `0.0689` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0475` n `142` status `ready` deltaP `3.899` edge `0.0833` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `-0.0251` n `142` status `ready` deltaP `15.2525` edge `0.3303` maxDD `-28.7261`
- `market_context_high->index_1h` score `-0.0326` n `143` status `ready` deltaP `4.0985` edge `0.0179` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3852` n `143` status `ready` deltaP `3.7478` edge `0.016` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4184` n `143` status `ready` deltaP `0.4544` edge `0.0454` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5187` n `143` status `ready` deltaP `5.7452` edge `0.0712` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5458` n `143` status `ready` deltaP `-0.6469` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.645` n `143` status `ready` deltaP `0.3967` edge `0.0034` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6547` n `143` status `ready` deltaP `-1.2457` edge `-0.0003` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6944` n `143` status `ready` deltaP `5.4929` edge `0.0613` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0056` n `142` status `ready` deltaP `-1.9237` edge `0.0069` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2599` n `142` status `ready` deltaP `2.1427` edge `0.0162` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2816` n `142` status `ready` deltaP `-1.7116` edge `-0.0082` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
