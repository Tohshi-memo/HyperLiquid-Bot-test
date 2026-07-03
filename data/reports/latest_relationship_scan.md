# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T11:21:11.275345+00:00`
- Price records: `672`
- Market context records: `5552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11377`

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

- `market_context_high->equity_24h` score `4.4681` n `192` status `ready` deltaP `14.9306` edge `0.7807` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.0212` n `192` status `ready` deltaP `11.5473` edge `0.3207` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.9791` n `192` status `ready` deltaP `16.493` edge `0.509` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.4746` n `192` status `ready` deltaP `6.9995` edge `0.2403` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4745` n `192` status `ready` deltaP `7.8506` edge `0.2344` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.6439` n `192` status `ready` deltaP `16.1458` edge `0.0434` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.17` n `202` status `ready` deltaP `7.0789` edge `0.0635` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0732` n `202` status `ready` deltaP `4.8808` edge `0.0107` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3217` n `202` status `ready` deltaP `1.162` edge `0.0616` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4208` n `202` status `ready` deltaP `1.9224` edge `0.001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4278` n `202` status `ready` deltaP `2.9243` edge `0.0694` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6698` n `202` status `ready` deltaP `0.495` edge `0.0084` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7676` n `192` status `ready` deltaP `3.3664` edge `0.007` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.5101` n `192` status `ready` deltaP `2.0071` edge `0.0217` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7464` n `202` status `ready` deltaP `-5.6412` edge `-0.0122` maxDD `-3.6579`
- `market_context_high->index_24h` score `-1.9893` n `192` status `ready` deltaP `12.8472` edge `0.058` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.4758` n `192` status `ready` deltaP `-11.1789` edge `-0.046` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7407` n `192` status `ready` deltaP `-10.1372` edge `-0.0613` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2262` n `192` status `ready` deltaP `7.6389` edge `0.2166` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3723` n `192` status `ready` deltaP `-3.6458` edge `-0.1831` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
