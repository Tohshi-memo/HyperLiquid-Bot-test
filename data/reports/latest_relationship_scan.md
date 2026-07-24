# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T11:52:29.765103+00:00`
- Price records: `672`
- Market context records: `7772`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `6.6007` n `132` status `ready` deltaP `26.0162` edge `0.5108` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.2228` n `133` status `ready` deltaP `12.0562` edge `0.2306` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9602` n `133` status `ready` deltaP `12.8585` edge `0.0384` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.6221` n `132` status `ready` deltaP `22.3973` edge `0.0392` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4706` n `133` status `ready` deltaP `7.8958` edge `0.0725` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4575` n `133` status `ready` deltaP `12.3647` edge `0.1275` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3855` n `133` status `ready` deltaP `1.8165` edge `0.2286` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3254` n `133` status `ready` deltaP `8.3441` edge `0.0145` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2364` n `133` status `ready` deltaP `6.8276` edge `0.0859` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.1782` n `133` status `ready` deltaP `6.3162` edge `0.0321` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.122` n `133` status `ready` deltaP `4.2783` edge `0.0249` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0427` n `133` status `ready` deltaP `4.8963` edge `0.0097` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2996` n `133` status `ready` deltaP `9.9469` edge `0.0411` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9238` n `133` status `ready` deltaP `0.8183` edge `0.0179` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.0135` n `132` status `ready` deltaP `8.4733` edge `0.0174` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4476` n `133` status `ready` deltaP `-3.3972` edge `-0.0001` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.717` n `133` status `ready` deltaP `-0.8436` edge `0.068` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.9455` n `132` status `ready` deltaP `-12.8788` edge `0.0467` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2668` n `133` status `ready` deltaP `-1.4238` edge `-0.1204` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
