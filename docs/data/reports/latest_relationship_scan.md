# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T15:07:26.843280+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4956.9064` n `62` status `ready` deltaP `26.8817` edge `412.9384` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.5305` n `40` status `ready` deltaP `58.5764` edge `1.1101` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8438` n `40` status `ready` deltaP `51.3194` edge `0.5743` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.833` n `68` status `ready` deltaP `18.8127` edge `0.3537` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.8227` n `68` status `ready` deltaP `18.203` edge `0.0686` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9664` n `40` status `ready` deltaP `12.378` edge `0.126` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7414` n `68` status `ready` deltaP `10.6904` edge `0.0728` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7374` n `40` status `ready` deltaP `9.4207` edge `0.1223` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.583` n `40` status `ready` deltaP `19.2378` edge `0.0261` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5758` n `40` status `ready` deltaP `10.8982` edge `0.0386` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4707` n `40` status `ready` deltaP `14.2964` edge `0.0028` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2112` n `68` status `ready` deltaP `13.2084` edge `0.0253` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.198` n `68` status `ready` deltaP `6.6894` edge `0.0284` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.117` n `68` status `ready` deltaP `6.7806` edge `0.038` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0412` n `68` status `ready` deltaP `3.267` edge `0.0052` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0505` n `68` status `ready` deltaP `2.7651` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0905` n `68` status `ready` deltaP `3.3639` edge `0.0063` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1369` n `68` status `ready` deltaP `3.4167` edge `0.0317` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.391` n `40` status `ready` deltaP `0.8982` edge `0.0066` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.7012` n `68` status `ready` deltaP `2.3688` edge `-0.0277` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
