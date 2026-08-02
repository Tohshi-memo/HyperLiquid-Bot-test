# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T14:22:27.249557+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5184.7532` n `60` status `ready` deltaP `27.1875` edge `431.9236` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5919` n `40` status `ready` deltaP `58.9236` edge `1.1129` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8078` n `40` status `ready` deltaP `51.3194` edge `0.5713` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7808` n `68` status `ready` deltaP `18.3554` edge `0.3524` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7837` n `68` status `ready` deltaP `17.7456` edge `0.0684` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9561` n `40` status `ready` deltaP `12.2256` edge `0.1257` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.739` n `68` status `ready` deltaP `10.6904` edge `0.0726` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7225` n `40` status `ready` deltaP `9.2683` edge `0.1214` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.5844` n `40` status `ready` deltaP `11.0479` edge `0.0387` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.5822` n `40` status `ready` deltaP `19.2378` edge `0.026` maxDD `-1.3685`
- `market_context_high->fx_1h` score `0.4707` n `40` status `ready` deltaP `14.2964` edge `0.0028` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.21` n `68` status `ready` deltaP `13.2084` edge `0.0252` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1901` n `68` status `ready` deltaP `6.5369` edge `0.0284` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1248` n `68` status `ready` deltaP `6.9303` edge `0.038` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0412` n `68` status `ready` deltaP `3.267` edge `0.0052` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0427` n `68` status `ready` deltaP `2.9148` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.075` n `68` status `ready` deltaP `3.6633` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1415` n `68` status `ready` deltaP `3.4167` edge `0.0311` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3833` n `40` status `ready` deltaP `1.0479` edge `0.0066` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6926` n `68` status `ready` deltaP `2.5185` edge `-0.0276` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
