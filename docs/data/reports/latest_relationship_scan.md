# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T22:22:30.976792+00:00`
- Price records: `672`
- Market context records: `5498`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `3.198` n `190` status `ready` deltaP `16.2189` edge `0.6124` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.7198` n `193` status `ready` deltaP `12.6019` edge `0.3065` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.6617` n `193` status `ready` deltaP `14.7984` edge `0.3524` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2363` n `193` status `ready` deltaP `10.8658` edge `0.278` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.1981` n `190` status `ready` deltaP `10.7511` edge `0.6194` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5771` n `193` status `ready` deltaP `9.0325` edge `0.0844` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3078` n `190` status `ready` deltaP `12.2368` edge `0.0368` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1823` n `193` status `ready` deltaP `6.9948` edge `0.0179` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2712` n `193` status `ready` deltaP `1.2837` edge `0.065` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3704` n `193` status `ready` deltaP `0.1784` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.378` n `193` status `ready` deltaP `3.0227` edge `0.0729` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.4708` n `193` status `ready` deltaP `2.2626` edge `0.0132` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.7672` n `193` status `ready` deltaP `7.5138` edge `0.0469` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8054` n `193` status `ready` deltaP `3.6712` edge `0.0065` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5482` n `193` status `ready` deltaP `-3.7247` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7834` n `190` status `ready` deltaP `14.2708` edge `0.0749` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.786` n `193` status `ready` deltaP `-9.7987` edge `-0.0394` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4338` n `193` status `ready` deltaP `-7.7238` edge `-0.0507` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1294` n `190` status `ready` deltaP `7.2442` edge `0.2273` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2643` n `190` status `ready` deltaP `-4.2379` edge `-0.1653` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
