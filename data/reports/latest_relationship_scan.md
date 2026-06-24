# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T07:07:30.099955+00:00`
- Price records: `672`
- Market context records: `4598`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9849`

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

- `market_context_high->unknown_1h` score `68.4683` n `148` status `ready` deltaP `6.0285` edge `5.7114` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.104` n `148` status `ready` deltaP `8.3759` edge `0.4072` maxDD `-4.6834`
- `market_context_high->fx_1h` score `-0.5664` n `148` status `ready` deltaP `-1.9583` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.5865` n `148` status `ready` deltaP `0.9629` edge `0.0243` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.7288` n `148` status `ready` deltaP `2.2206` edge `0.0` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.917` n `148` status `ready` deltaP `1.2031` edge `-0.0133` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9677` n `148` status `ready` deltaP `-3.3703` edge `-0.0029` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2242` n `148` status `ready` deltaP `3.1971` edge `0.0325` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.6823` n `148` status `ready` deltaP `-0.5191` edge `-0.0353` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7452` n `148` status `ready` deltaP `-4.6448` edge `-0.0136` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.608` n `146` status `ready` deltaP `2.2046` edge `-0.1397` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0157` n `148` status `ready` deltaP `-4.8107` edge `-0.0894` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.592` n `146` status `ready` deltaP `11.2847` edge `0.067` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4352` n `146` status `ready` deltaP `-13.5464` edge `-0.0114` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5416` n `148` status `ready` deltaP `-2.2455` edge `-0.1181` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8603` n `148` status `ready` deltaP `-6.3764` edge `-0.1539` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4976` n `146` status `ready` deltaP `-7.9576` edge `-0.1176` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1254` n `148` status `ready` deltaP `-3.4196` edge `-0.2814` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3037` n `148` status `ready` deltaP `-6.3901` edge `-0.357` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.2759` n `148` status `ready` deltaP `-5.2736` edge `-0.4443` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
