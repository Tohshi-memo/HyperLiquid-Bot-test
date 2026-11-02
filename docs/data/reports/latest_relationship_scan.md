# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T06:52:40.517668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5157`

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

- `market_context_high->unknown_24h` score `6358.4371` n `35` status `ready` deltaP `1.3889` edge `529.8605` maxDD `0.0`
- `market_context_high->unknown_4h` score `565.5845` n `40` status `ready` deltaP `8.8415` edge `47.0731` maxDD `0.0`
- `market_context_high->unknown_1h` score `140.0633` n `40` status `ready` deltaP `7.9192` edge `11.6302` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.3309` n `35` status `ready` deltaP `41.761` edge `1.3561` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.9904` n `97` status `ready` deltaP `31.9427` edge `1.0052` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.2625` n `35` status `ready` deltaP `43.2738` edge `0.3478` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.7806` n `35` status `ready` deltaP `49.1319` edge `0.2375` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2725` n `40` status `ready` deltaP `26.5549` edge `0.3751` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.5779` n `40` status `ready` deltaP `10.5793` edge `0.4645` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.943` n `40` status `ready` deltaP `24.7561` edge `0.2805` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.8911` n `40` status `ready` deltaP `9.4012` edge `0.2183` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.4389` n `126` status `ready` deltaP `9.9279` edge `0.2757` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `2.1713` n `40` status `ready` deltaP `7.7994` edge `0.1731` maxDD `-1.5324`
- `market_context_high->crypto_major_1h` score `1.9338` n `40` status `ready` deltaP `9.7006` edge `0.1355` maxDD `-1.1219`
- `market_context_high->metal_4h` score `1.7568` n `40` status `ready` deltaP `20.4878` edge `0.0523` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.6557` n `35` status `ready` deltaP `-8.7054` edge `0.3478` maxDD `-8.8096`
- `market_context_high->index_4h` score `1.6548` n `40` status `ready` deltaP `17.7744` edge `0.0498` maxDD `-0.7649`
- `market_context_high->fx_1h` score `1.301` n `40` status `ready` deltaP `17.2006` edge `0.0109` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `1.2574` n `40` status `ready` deltaP `23.872` edge `0.0433` maxDD `-1.633`
- `market_context_high->metal_1h` score `0.544` n `40` status `ready` deltaP `11.0928` edge `0.0215` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
