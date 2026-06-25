# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T20:07:30.560659+00:00`
- Price records: `672`
- Market context records: `4755`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `82.9224` n `137` status `ready` deltaP `13.2982` edge `6.8633` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.1348` n `134` status `ready` deltaP `13.8264` edge `0.5401` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.1349` n `122` status `ready` deltaP `15.3119` edge `0.2515` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4155` n `134` status `ready` deltaP `7.0213` edge `0.0068` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5268` n `134` status `ready` deltaP `6.5481` edge `0.0574` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.5279` n `137` status `ready` deltaP `2.086` edge `0.0217` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.818` n `134` status `ready` deltaP `-0.8668` edge `-0.0023` maxDD `-1.7431`
- `market_context_high->equity_1h` score `-0.9178` n `137` status `ready` deltaP `-1.1135` edge `-0.0153` maxDD `-5.262`
- `market_context_high->fx_1h` score `-1.1882` n `137` status `ready` deltaP `-4.2397` edge `-0.0047` maxDD `-0.951`
- `market_context_high->commodity_4h` score `-1.3179` n `134` status `ready` deltaP `7.8063` edge `0.0222` maxDD `-8.7256`
- `market_context_high->index_1h` score `-1.4897` n `137` status `ready` deltaP `-2.4793` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.5154` n `137` status `ready` deltaP `-3.0421` edge `-0.0692` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5769` n `122` status `ready` deltaP `16.9655` edge `0.0674` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7352` n `137` status `ready` deltaP `-0.3464` edge `-0.0505` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2237` n `137` status `ready` deltaP `0.271` edge `-0.072` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.278` n `122` status `ready` deltaP `-15.5054` edge `-0.0219` maxDD `-4.4982`
- `market_context_high->crypto_alt_4h` score `-5.5514` n `134` status `ready` deltaP `1.6768` edge `-0.0417` maxDD `-49.1624`
- `market_context_high->index_24h` score `-7.1815` n `122` status `ready` deltaP `-11.7087` edge `-0.1157` maxDD `-23.0429`
- `market_context_high->crypto_major_4h` score `-8.1714` n `134` status `ready` deltaP `2.5915` edge `-0.1418` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3392` n `134` status `ready` deltaP `4.1317` edge `-0.2726` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
