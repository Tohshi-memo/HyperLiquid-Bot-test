# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T00:22:25.577222+00:00`
- Price records: `672`
- Market context records: `4569`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.8886` n `157` status `ready` deltaP `6.585` edge `5.8302` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.9741` n `157` status `ready` deltaP `7.3025` edge `0.3202` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5151` n `157` status `ready` deltaP `5.9859` edge `0.0023` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5925` n `157` status `ready` deltaP `1.5485` edge `0.0199` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.6897` n `157` status `ready` deltaP `2.1147` edge `0.0744` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.6933` n `157` status `ready` deltaP `-2.1883` edge `0.0244` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.7238` n `157` status `ready` deltaP `-0.2479` edge `-0.0032` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7859` n `157` status `ready` deltaP `2.9585` edge `-0.0082` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1751` n `157` status `ready` deltaP `3.6614` edge `0.0357` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6019` n `157` status `ready` deltaP `-3.1246` edge `-0.0118` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9338` n `157` status `ready` deltaP `-4.2546` edge `-0.0826` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.1446` n `155` status `ready` deltaP `1.5278` edge `-0.1799` maxDD `-4.7201`
- `market_context_high->fx_24h` score `-5.4712` n `155` status `ready` deltaP `-13.7254` edge `-0.0132` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.48` n `157` status `ready` deltaP `-2.6755` edge `-0.1101` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.5404` n `155` status `ready` deltaP `-8.9281` edge `-0.1133` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-5.7777` n `155` status `ready` deltaP `8.3815` edge `0.0471` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.6859` n `157` status `ready` deltaP `-5.7868` edge `-0.1433` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.9776` n `157` status `ready` deltaP `-3.1876` edge `-0.264` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2801` n `157` status `ready` deltaP `-8.7346` edge `-0.338` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.7525` n `157` status `ready` deltaP `-2.0497` edge `-0.3987` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
