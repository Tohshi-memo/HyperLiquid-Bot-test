# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T09:52:28.212173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4854`

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

- `market_context_high->unknown_1h` score `340.915` n `50` status `ready` deltaP `10.4251` edge `28.345` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0435` n `50` status `ready` deltaP `9.6037` edge `23.9396` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.0808` n `71` status `ready` deltaP `39.7178` edge `1.0129` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.6027` n `50` status `ready` deltaP `35.4722` edge `0.7887` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.3079` n `71` status `ready` deltaP `36.341` edge `0.6652` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0201` n `50` status `ready` deltaP `16.5347` edge `0.8124` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9865` n `50` status `ready` deltaP `17.5427` edge `0.5356` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9589` n `50` status `ready` deltaP `15.5793` edge `0.4387` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4453` n `100` status `ready` deltaP `17.5793` edge `0.3876` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9395` n `50` status `ready` deltaP `32.8415` edge `0.0395` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.9373` n `50` status `ready` deltaP `14.2036` edge `0.2164` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8896` n `50` status `ready` deltaP `14.1497` edge `0.1915` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.7135` n `50` status `ready` deltaP `12.7917` edge `0.4488` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.5375` n `100` status `ready` deltaP `23.7988` edge `0.1224` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.0399` n `71` status `ready` deltaP `8.4018` edge `0.5209` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2189` n `71` status `ready` deltaP `11.6197` edge `0.2062` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9504` n `50` status `ready` deltaP `15.4861` edge `0.0757` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.9183` n `111` status `ready` deltaP `5.8613` edge `0.0937` maxDD `-2.4998`
- `news_risk_high->crypto_major_4h` score `0.7903` n `100` status `ready` deltaP `10.5427` edge `0.262` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
