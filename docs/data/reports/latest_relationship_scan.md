# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T11:52:26.938421+00:00`
- Price records: `672`
- Market context records: `5554`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.4679` n `191` status `ready` deltaP `14.8379` edge `0.7813` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.9864` n `192` status `ready` deltaP `11.5473` edge `0.3178` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.8854` n `191` status `ready` deltaP `16.3567` edge `0.5021` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.453` n `192` status `ready` deltaP `6.9995` edge `0.2385` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4409` n `192` status `ready` deltaP `7.8506` edge `0.2316` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.668` n `191` status `ready` deltaP `16.3567` edge `0.044` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1761` n `203` status `ready` deltaP `7.1097` edge `0.0638` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.066` n `203` status `ready` deltaP `4.9409` edge `0.0109` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2499` n `203` status `ready` deltaP `1.7293` edge `0.0638` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.2692` n `203` status `ready` deltaP `2.0044` edge `0.001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3673` n `203` status `ready` deltaP `3.5014` edge `0.0706` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6945` n `203` status `ready` deltaP `0.2463` edge `0.008` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6951` n `192` status `ready` deltaP `3.5823` edge `0.0072` maxDD `-1.4541`
- `market_context_high->index_4h` score `-1.5137` n `192` status `ready` deltaP `2.0071` edge `0.0214` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6767` n `203` status `ready` deltaP `-5.5153` edge `-0.0114` maxDD `-3.6579`
- `market_context_high->index_24h` score `-2.0019` n `191` status `ready` deltaP `12.6945` edge `0.0574` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5062` n `192` status `ready` deltaP `-11.3948` edge `-0.0471` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7383` n `192` status `ready` deltaP `-10.1372` edge `-0.0611` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.3391` n `191` status `ready` deltaP `7.4426` edge `0.2085` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4274` n `191` status `ready` deltaP `-3.9403` edge `-0.1882` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
