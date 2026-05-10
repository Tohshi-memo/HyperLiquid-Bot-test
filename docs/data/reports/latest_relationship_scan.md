# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T12:43:57.033303+00:00`
- Price records: `672`
- Market context records: `977`
- Flow alert records: `2734`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.319` n `150` status `ready` deltaP `35.382` edge `1.0741` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.7951` n `150` status `ready` deltaP `11.9792` edge `0.7364` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2472` n `150` status `ready` deltaP `0.8264` edge `0.3589` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5469` n `150` status `ready` deltaP `-1.2916` edge `0.2537` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2044` n `210` status `ready` deltaP `3.7425` edge `0.0388` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5913` n `210` status `ready` deltaP `1.1691` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6368` n `210` status `ready` deltaP `1.2746` edge `0.0153` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6597` n `200` status `ready` deltaP `1.9146` edge `0.0023` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7054` n `210` status `ready` deltaP `3.2207` edge `0.0051` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1067` n `210` status `ready` deltaP `5.6729` edge `-0.0074` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1728` n `210` status `ready` deltaP `-1.075` edge `-0.0134` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5217` n `200` status `ready` deltaP `1.1098` edge `0.081` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7045` n `200` status `ready` deltaP `-1.5854` edge `0.0208` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8199` n `210` status `ready` deltaP `-1.199` edge `-0.0294` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0325` n `210` status `ready` deltaP `0.2837` edge `-0.0273` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.6201` n `200` status `ready` deltaP `8.4085` edge `0.0962` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9076` n `200` status `ready` deltaP `-0.5305` edge `0.078` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.0945` n `200` status `ready` deltaP `8.4512` edge `-0.1264` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.3094` n `200` status `ready` deltaP `-1.811` edge `0.0141` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0166` n `150` status `ready` deltaP `5.0139` edge `0.0022` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
