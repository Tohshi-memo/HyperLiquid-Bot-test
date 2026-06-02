# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T09:37:26.426681+00:00`
- Price records: `672`
- Market context records: `2650`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.7324` n `127` status `ready` deltaP `17.5785` edge `0.56` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `6.3377` n `127` status `ready` deltaP `9.5759` edge `0.8364` maxDD `-21.7679`
- `market_context_high->crypto_alt_4h` score `5.6677` n `127` status `ready` deltaP `26.1763` edge `0.5657` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.2831` n `127` status `ready` deltaP `16.8787` edge `0.4254` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5072` n `127` status `ready` deltaP `8.4705` edge `0.1741` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1334` n `133` status `ready` deltaP `10.3035` edge `0.1445` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.909` n `127` status `ready` deltaP `10.8337` edge `0.1016` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.4948` n `133` status `ready` deltaP `6.8468` edge `0.115` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.2613` n `127` status `ready` deltaP `9.3336` edge `0.0437` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0576` n `133` status `ready` deltaP `4.455` edge `0.0149` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.0611` n `127` status `ready` deltaP `6.4396` edge `0.0336` maxDD `-2.5301`
- `market_context_high->unknown_1h` score `-0.1421` n `133` status `ready` deltaP `1.7401` edge `0.0307` maxDD `-1.665`
- `market_context_high->commodity_1h` score `-0.4258` n `133` status `ready` deltaP `4.132` edge `0.0057` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5603` n `133` status `ready` deltaP `-0.8183` edge `0.0034` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.5859` n `127` status `ready` deltaP `5.8863` edge `-0.0002` maxDD `-0.6957`
- `market_context_high->metal_1h` score `-0.7071` n `133` status `ready` deltaP `-0.6787` edge `0.0025` maxDD `-1.5521`
- `market_context_high->equity_1h` score `-0.8611` n `133` status `ready` deltaP `-1.3799` edge `0.0213` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.0855` n `127` status `ready` deltaP `-2.6803` edge `0.0105` maxDD `-0.6474`
- `market_context_high->equity_24h` score `-1.273` n `127` status `ready` deltaP `8.0805` edge `-0.0622` maxDD `-3.1535`
- `market_context_high->commodity_4h` score `-1.321` n `127` status `ready` deltaP `2.4762` edge `0.0084` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
