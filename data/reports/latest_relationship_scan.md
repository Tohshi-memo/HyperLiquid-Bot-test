# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T07:37:29.571401+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5205`

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

- `market_context_high->unknown_24h` score `5877.3139` n `32` status `ready` deltaP `1.3889` edge `489.7669` maxDD `0.0`
- `market_context_high->unknown_4h` score `642.3293` n `37` status `ready` deltaP `8.8415` edge `53.4685` maxDD `0.0`
- `market_context_high->unknown_1h` score `169.7902` n `37` status `ready` deltaP `7.6105` edge `14.1095` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.7967` n `32` status `ready` deltaP `41.4931` edge `1.3967` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `11.3343` n `100` status `ready` deltaP `29.6111` edge `0.945` maxDD `-11.8307`
- `market_context_high->commodity_24h` score `7.3016` n `32` status `ready` deltaP `42.1875` edge `0.3583` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.9822` n `32` status `ready` deltaP `49.1319` edge `0.2543` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2279` n `37` status `ready` deltaP `25.5933` edge `0.3778` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.9333` n `37` status `ready` deltaP `10.5966` edge `0.494` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.8768` n `37` status `ready` deltaP `23.3891` edge `0.2841` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.7002` n `37` status `ready` deltaP `14.2661` edge `0.2533` maxDD `-1.2043`
- `market_context_high->crypto_alt_1h` score `3.0483` n `37` status `ready` deltaP `12.4616` edge `0.2151` maxDD `-1.5324`
- `market_context_high->crypto_major_1h` score `2.7502` n `37` status `ready` deltaP `14.5655` edge `0.1711` maxDD `-1.1219`
- `news_risk_high->crypto_alt_4h` score `2.5643` n `126` status `ready` deltaP `10.3852` edge `0.2831` maxDD `-7.4246`
- `market_context_high->index_4h` score `2.4312` n `37` status `ready` deltaP `23.3479` edge `0.0699` maxDD `-0.1695`
- `market_context_high->crypto_alt_24h` score `1.6186` n `32` status `ready` deltaP `-7.6389` edge `0.3376` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.4962` n `37` status `ready` deltaP `17.65` edge `0.0495` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.3065` n `37` status `ready` deltaP `17.1185` edge `0.0119` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `1.127` n `37` status `ready` deltaP `22.0996` edge `0.0384` maxDD `-1.633`
- `market_context_high->index_1h` score `0.5189` n `37` status `ready` deltaP `5.4095` edge `0.0313` maxDD `-0.2628`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
