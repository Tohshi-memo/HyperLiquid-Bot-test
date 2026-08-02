# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T12:07:29.708919+00:00`
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

- `news_risk_high->unknown_24h` score `5184.9382` n `60` status `ready` deltaP `28.75` edge `431.9286` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5283` n `40` status `ready` deltaP `58.9236` edge `1.1076` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.6902` n `40` status `ready` deltaP `51.3194` edge `0.5615` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.6075` n `68` status `ready` deltaP `16.9835` edge `0.3471` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6596` n `68` status `ready` deltaP `16.3737` edge `0.0672` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9955` n `40` status `ready` deltaP `12.6829` edge `0.1277` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7091` n `68` status `ready` deltaP `10.391` edge `0.0721` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.6147` n `40` status `ready` deltaP `19.8476` edge `0.0261` maxDD `-1.3685`
- `market_context_high->crypto_alt_4h` score `0.5911` n `40` status `ready` deltaP `7.8963` edge `0.1137` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.5555` n `40` status `ready` deltaP `10.5988` edge `0.038` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4692` n `40` status `ready` deltaP `14.2964` edge `0.0026` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.26` n `68` status `ready` deltaP `13.8182` edge `0.0253` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1719` n `68` status `ready` deltaP `6.232` edge `0.0281` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1357` n `68` status `ready` deltaP `7.08` edge `0.0384` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0427` n `68` status `ready` deltaP `2.9148` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0827` n `68` status `ready` deltaP `3.5136` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1595` n `68` status `ready` deltaP `3.1173` edge `0.0308` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3724` n `40` status `ready` deltaP `1.1976` edge `0.007` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.7214` n `68` status `ready` deltaP `2.0694` edge `-0.0283` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
