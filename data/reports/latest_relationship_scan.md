# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T04:52:26.824403+00:00`
- Price records: `672`
- Market context records: `5421`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_24h` score `4.0532` n `190` status `ready` deltaP `19.6637` edge `0.6607` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7992` n `201` status `ready` deltaP `16.2966` edge `0.4372` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9486` n `201` status `ready` deltaP `11.7151` edge `0.3317` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.9271` n `190` status `ready` deltaP `9.693` edge `0.5653` maxDD `-24.2131`
- `market_context_high->equity_4h` score `2.4884` n `201` status `ready` deltaP `12.1253` edge `0.2904` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4241` n `201` status `ready` deltaP `7.9006` edge `0.0792` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1202` n `201` status `ready` deltaP `6.5183` edge `0.0159` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0627` n `190` status `ready` deltaP `9.3239` edge `0.0326` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.2191` n `201` status `ready` deltaP `3.4937` edge `0.083` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2848` n `201` status `ready` deltaP `1.0985` edge `0.0651` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5296` n `201` status `ready` deltaP `1.6929` edge `0.0121` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5984` n `201` status `ready` deltaP `-0.1035` edge `-0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-1.0111` n `201` status `ready` deltaP `5.7851` edge `0.0381` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1816` n `201` status `ready` deltaP `0.3224` edge `0.0019` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.406` n `190` status `ready` deltaP `14.2708` edge `0.0863` maxDD `-12.5551`
- `market_context_high->commodity_1h` score `-1.4618` n `201` status `ready` deltaP `-3.0841` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.651` n `201` status `ready` deltaP `-7.832` edge `-0.0352` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2669` n `201` status `ready` deltaP `-6.862` edge `-0.046` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.3354` n `190` status `ready` deltaP `10.689` edge `0.2705` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2042` n `190` status `ready` deltaP `-4.9433` edge `-0.1529` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
