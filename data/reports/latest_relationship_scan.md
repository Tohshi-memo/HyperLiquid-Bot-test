# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T05:37:25.821291+00:00`
- Price records: `672`
- Market context records: `5424`
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

- `market_context_high->crypto_major_24h` score `4.5539` n `187` status `ready` deltaP `20.2828` edge `0.6983` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.2111` n `187` status `ready` deltaP `10.9849` edge `0.6313` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.8703` n `198` status `ready` deltaP `16.7513` edge `0.4401` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0378` n `198` status `ready` deltaP `12.1397` edge `0.3363` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5734` n `198` status `ready` deltaP `12.4076` edge `0.2956` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4415` n `198` status `ready` deltaP `7.9674` edge `0.0802` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1063` n `198` status `ready` deltaP `6.36` edge `0.0158` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0446` n `187` status `ready` deltaP `8.9777` edge `0.0334` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.2264` n `198` status `ready` deltaP `3.3871` edge `0.0831` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2469` n `198` status `ready` deltaP `1.3473` edge `0.0666` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4315` n `198` status `ready` deltaP `2.4693` edge `0.0151` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.6007` n `198` status `ready` deltaP `-0.1315` edge `-0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.9792` n `198` status `ready` deltaP `6.0791` edge `0.0388` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1472` n `198` status `ready` deltaP `0.7068` edge `0.0022` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.2058` n `187` status `ready` deltaP `15.3938` edge `0.0955` maxDD `-12.5551`
- `market_context_high->commodity_1h` score `-1.4895` n `198` status `ready` deltaP `-3.3857` edge `-0.0071` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7117` n `198` status `ready` deltaP `-8.729` edge `-0.037` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3625` n `198` status `ready` deltaP `-7.682` edge `-0.0485` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.942` n `187` status `ready` deltaP `11.1222` edge `0.3004` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2641` n `187` status `ready` deltaP `-5.1498` edge `-0.1592` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
