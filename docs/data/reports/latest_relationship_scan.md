# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T13:52:30.600337+00:00`
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

- `news_risk_high->unknown_24h` score `5184.7918` n `60` status `ready` deltaP `27.5347` edge `431.9245` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5631` n `40` status `ready` deltaP `58.9236` edge `1.1105` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.7814` n `40` status `ready` deltaP `51.3194` edge `0.5691` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.742` n `68` status `ready` deltaP `18.0505` edge `0.3512` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7569` n `68` status `ready` deltaP `17.4408` edge `0.0682` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9648` n `40` status `ready` deltaP `12.378` edge `0.1258` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7127` n `68` status `ready` deltaP `10.391` edge `0.0724` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6918` n `40` status `ready` deltaP `8.9634` edge `0.1195` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.5828` n `40` status `ready` deltaP `11.0479` edge `0.0385` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.5807` n `40` status `ready` deltaP `19.2378` edge `0.0258` maxDD `-1.3685`
- `market_context_high->fx_1h` score `0.4692` n `40` status `ready` deltaP `14.2964` edge `0.0026` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2076` n `68` status `ready` deltaP `13.2084` edge `0.025` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1814` n `68` status `ready` deltaP `6.3845` edge `0.0283` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1138` n `68` status `ready` deltaP `6.7806` edge `0.0376` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0505` n `68` status `ready` deltaP `2.7651` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0827` n `68` status `ready` deltaP `3.5136` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1431` n `68` status `ready` deltaP `3.4167` edge `0.0309` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3942` n `40` status `ready` deltaP `0.8982` edge `0.0062` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6942` n `68` status `ready` deltaP `2.5185` edge `-0.0278` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
