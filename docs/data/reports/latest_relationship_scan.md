# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T08:52:28.417348+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `market_context_high->crypto_alt_4h` score `7.2531` n `135` status `ready` deltaP `17.081` edge `0.582` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0389` n `54` status `ready` deltaP `38.5017` edge `0.3299` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0389` n `54` status `ready` deltaP `38.5017` edge `0.3299` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.5016` n `61` status `ready` deltaP `36.6554` edge `0.3827` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.5016` n `61` status `ready` deltaP `36.6554` edge `0.3827` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.1393` n `135` status `ready` deltaP `24.1599` edge `0.4827` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.3321` n `61` status `ready` deltaP `14.5067` edge `0.3257` maxDD `-2.5791`
- `risk_on_and_context->crypto_alt_4h` score `4.3321` n `61` status `ready` deltaP `14.5067` edge `0.3257` maxDD `-2.5791`
- `market_context_high->crypto_alt_1h` score `1.1654` n `147` status `ready` deltaP `10.313` edge `0.1348` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0918` n `147` status `ready` deltaP `8.4219` edge `0.1154` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3567` n `135` status `ready` deltaP `12.5486` edge `0.0506` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.1103` n `73` status `ready` deltaP `6.3906` edge `0.005` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1103` n `73` status `ready` deltaP `6.3906` edge `0.005` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.0588` n `73` status `ready` deltaP `6.7632` edge `0.0196` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0588` n `73` status `ready` deltaP `6.7632` edge `0.0196` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.165` n `147` status `ready` deltaP `7.4064` edge `0.0043` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2877` n `147` status `ready` deltaP `8.096` edge `0.009` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.4895` n `147` status `ready` deltaP `7.9978` edge `0.0349` maxDD `-7.0778`
- `risk_on_high->metal_1h` score `-0.4912` n `73` status `ready` deltaP `0.9392` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4912` n `73` status `ready` deltaP `0.9392` edge `0.0039` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
