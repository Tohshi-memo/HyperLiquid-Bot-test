# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T12:37:24.000577+00:00`
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

- `news_risk_high->unknown_24h` score `5184.896` n `60` status `ready` deltaP `28.4027` edge `431.9274` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5415` n `40` status `ready` deltaP `58.9236` edge `1.1087` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.7118` n `40` status `ready` deltaP `51.3194` edge `0.5633` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.6475` n `68` status `ready` deltaP `17.2883` edge `0.3484` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6875` n `68` status `ready` deltaP `16.6786` edge `0.0675` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9923` n `40` status `ready` deltaP `12.6829` edge `0.1273` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6971` n `68` status `ready` deltaP `10.2413` edge `0.0721` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6155` n `40` status `ready` deltaP `8.2012` edge `0.1148` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.5981` n `40` status `ready` deltaP `19.5427` edge `0.026` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5649` n `40` status `ready` deltaP `10.7485` edge `0.0382` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4762` n `40` status `ready` deltaP `14.4461` edge `0.0025` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2344` n `68` status `ready` deltaP `13.5133` edge `0.0252` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1719` n `68` status `ready` deltaP `6.232` edge `0.0281` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1154` n `68` status `ready` deltaP `6.7806` edge `0.0378` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0357` n `68` status `ready` deltaP `3.4167` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0505` n `68` status `ready` deltaP `2.7651` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0827` n `68` status `ready` deltaP `3.5136` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1532` n `68` status `ready` deltaP `3.267` edge `0.0306` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3926` n `40` status `ready` deltaP `0.8982` edge `0.0064` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.7121` n `68` status `ready` deltaP `2.2191` edge `-0.0281` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
