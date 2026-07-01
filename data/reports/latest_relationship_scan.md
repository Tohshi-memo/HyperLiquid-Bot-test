# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T18:52:25.666904+00:00`
- Price records: `672`
- Market context records: `5378`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `8.1278` n `181` status `ready` deltaP `16.7607` edge `0.5786` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4134` n `181` status `ready` deltaP `22.6116` edge `0.7544` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.1784` n `205` status `ready` deltaP `14.1768` edge `0.3996` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.6527` n `181` status `ready` deltaP `13.1762` edge `0.6961` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.6147` n `205` status `ready` deltaP `11.0061` edge `0.3086` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7999` n `205` status `ready` deltaP `9.9086` edge `0.2478` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.0843` n `205` status `ready` deltaP `6.2626` edge `0.0618` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.0648` n `181` status `ready` deltaP `16.7099` edge `0.0952` maxDD `-9.0959`
- `market_context_high->fx_24h` score `-0.0731` n `181` status `ready` deltaP `7.7463` edge `0.0318` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.0882` n `205` status `ready` deltaP `4.5283` edge `0.0118` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1667` n `205` status `ready` deltaP `1.6299` edge `0.0714` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.1873` n `205` status `ready` deltaP `3.576` edge `0.0851` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.4244` n `205` status `ready` deltaP `-0.6543` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5874` n `205` status `ready` deltaP `1.1808` edge `0.0107` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.6055` n `205` status `ready` deltaP `8.2927` edge `0.0127` maxDD `-6.1421`
- `market_context_high->fx_4h` score `-1.1791` n `205` status `ready` deltaP `0.5488` edge `0.001` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.2003` n `205` status `ready` deltaP `4.7256` edge `0.0294` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5478` n `205` status `ready` deltaP `-4.0689` edge `-0.0074` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.54` n `205` status `ready` deltaP `-6.372` edge `-0.0307` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2582` n `181` status `ready` deltaP `13.4083` edge `0.3626` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
