# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T17:37:26.654444+00:00`
- Price records: `672`
- Market context records: `5477`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11466`

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

- `market_context_high->crypto_major_24h` score `3.5283` n `192` status `ready` deltaP `16.493` edge `0.6381` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.5924` n `195` status `ready` deltaP `13.0495` edge `0.2929` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.398` n `195` status `ready` deltaP `13.9775` edge `0.3359` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.046` n `195` status `ready` deltaP `10.5128` edge `0.2645` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.1205` n `192` status `ready` deltaP `9.8958` edge `0.5353` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.6102` n `195` status `ready` deltaP `9.207` edge `0.086` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2329` n `195` status `ready` deltaP `7.5219` edge `0.0186` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.148` n `192` status `ready` deltaP `10.7639` edge `0.0333` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3148` n `195` status `ready` deltaP `1.2183` edge `0.0004` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.357` n `195` status `ready` deltaP `3.5053` edge `0.0144` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4329` n `195` status `ready` deltaP `0.747` edge `0.0551` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5948` n `195` status `ready` deltaP `2.0528` edge `0.0613` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.7295` n `195` status `ready` deltaP `8.2255` edge `0.0453` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9129` n `195` status `ready` deltaP `3.1261` edge `0.0056` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4939` n `195` status `ready` deltaP `-3.2251` edge `-0.0082` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8432` n `192` status `ready` deltaP `13.5416` edge `0.0721` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.1901` n `195` status `ready` deltaP `-8.9884` edge `-0.0368` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2583` n `195` status `ready` deltaP `-5.9404` edge `-0.0447` maxDD `-14.3114`
- `market_context_high->crypto_alt_24h` score `-7.0678` n `192` status `ready` deltaP `7.6389` edge `0.2298` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.1141` n `192` status `ready` deltaP `-3.6458` edge `-0.15` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
