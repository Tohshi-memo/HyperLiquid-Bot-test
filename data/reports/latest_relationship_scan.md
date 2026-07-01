# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T18:37:27.440713+00:00`
- Price records: `672`
- Market context records: `5377`
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

- `market_context_high->unknown_24h` score `8.123` n `181` status `ready` deltaP `16.7607` edge `0.5782` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4338` n `181` status `ready` deltaP `22.6116` edge `0.7561` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.1436` n `205` status `ready` deltaP `14.1768` edge `0.3967` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.6028` n `181` status `ready` deltaP `13.0026` edge `0.6931` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.5533` n `205` status `ready` deltaP `10.8537` edge `0.3045` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7301` n `205` status `ready` deltaP `9.7561` edge `0.243` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.0567` n `205` status `ready` deltaP `6.1129` edge `0.0605` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.0305` n `181` status `ready` deltaP `16.5363` edge `0.0935` maxDD `-9.0959`
- `market_context_high->fx_24h` score `-0.0882` n `181` status `ready` deltaP `7.5727` edge `0.0317` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1026` n `205` status `ready` deltaP `4.3786` edge `0.0116` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1978` n `205` status `ready` deltaP `1.4802` edge `0.0698` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2113` n `205` status `ready` deltaP `3.4263` edge `0.0841` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.4166` n `205` status `ready` deltaP `-0.5046` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6029` n `205` status `ready` deltaP `1.0311` edge `0.0104` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.6931` n `205` status `ready` deltaP `8.2927` edge `0.0054` maxDD `-6.1421`
- `market_context_high->fx_4h` score `-1.1791` n `205` status `ready` deltaP `0.5488` edge `0.001` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.2269` n `205` status `ready` deltaP `4.5731` edge `0.0282` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5478` n `205` status `ready` deltaP `-4.0689` edge `-0.0074` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.5557` n `205` status `ready` deltaP `-6.5244` edge `-0.0317` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2465` n `181` status `ready` deltaP `13.4083` edge `0.3641` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
