# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T17:07:27.639077+00:00`
- Price records: `672`
- Market context records: `4743`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7454`

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

- `market_context_high->unknown_1h` score `81.4979` n `138` status `ready` deltaP `13.6727` edge `6.7421` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1736` n `135` status `ready` deltaP `12.7462` edge `0.4672` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2696` n `126` status `ready` deltaP `16.1706` edge `0.257` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3759` n `135` status `ready` deltaP `7.7992` edge `0.0067` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.5363` n `138` status `ready` deltaP `2.0415` edge `0.0213` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5908` n `135` status `ready` deltaP `5.9914` edge `0.0529` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9195` n `135` status `ready` deltaP `-1.1778` edge `-0.003` maxDD `-1.8962`
- `market_context_high->equity_1h` score `-0.9632` n `138` status `ready` deltaP `-1.7487` edge `-0.0153` maxDD `-5.3889`
- `market_context_high->fx_1h` score `-1.2354` n `138` status `ready` deltaP `-4.7015` edge `-0.0051` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.5613` n `138` status `ready` deltaP `-3.2695` edge `-0.0079` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.6986` n `135` status `ready` deltaP `6.9015` edge `0.0186` maxDD `-9.1592`
- `market_context_high->commodity_24h` score `-2.5096` n `126` status `ready` deltaP `17.4355` edge `0.0729` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.5567` n `138` status `ready` deltaP `-3.5039` edge `-0.0698` maxDD `-15.4366`
- `market_context_high->crypto_alt_1h` score `-2.6146` n `138` status `ready` deltaP `0.1736` edge `-0.0385` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1741` n `138` status `ready` deltaP `0.5207` edge `-0.0628` maxDD `-25.1414`
- `market_context_high->fx_24h` score `-4.421` n `126` status `ready` deltaP `-14.3849` edge `-0.02` maxDD `-4.8682`
- `market_context_high->crypto_alt_4h` score `-5.8462` n `135` status `ready` deltaP `1.023` edge `-0.0497` maxDD `-51.1969`
- `market_context_high->index_24h` score `-7.403` n `126` status `ready` deltaP `-11.1607` edge `-0.1037` maxDD `-24.4384`
- `market_context_high->metal_4h` score `-8.4369` n `135` status `ready` deltaP `2.6118` edge `-0.2748` maxDD `-61.2747`
- `market_context_high->crypto_major_4h` score `-8.6674` n `135` status `ready` deltaP `1.3708` edge `-0.1586` maxDD `-71.6061`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
