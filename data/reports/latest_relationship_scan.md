# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T11:22:36.405243+00:00`
- Price records: `672`
- Market context records: `5139`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `26.9451` n `66` status `ready` deltaP `29.8927` edge `2.0804` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `7.0637` n `123` status `ready` deltaP `20.2744` edge `0.5557` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.7076` n `135` status `ready` deltaP `9.8425` edge `0.5575` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9756` n `123` status `ready` deltaP `15.1423` edge `0.4736` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5841` n `123` status `ready` deltaP `13.0082` edge `0.4412` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.1742` n `66` status `ready` deltaP `17.4242` edge `0.1327` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.8419` n `123` status `ready` deltaP `8.9431` edge `0.1744` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.802` n `135` status `ready` deltaP `5.8782` edge `0.1238` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7747` n `135` status `ready` deltaP `8.2812` edge `0.1339` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6989` n `135` status `ready` deltaP `7.7933` edge `0.0656` maxDD `-2.745`
- `market_context_high->index_1h` score `0.0655` n `135` status `ready` deltaP `6.1544` edge `0.0148` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0999` n `135` status `ready` deltaP `4.42` edge `0.0143` maxDD `-1.8592`
- `market_context_high->index_4h` score `-0.3627` n `123` status `ready` deltaP `6.7073` edge `0.0368` maxDD `-2.9391`
- `market_context_high->metal_24h` score `-0.3906` n `66` status `ready` deltaP `-0.7892` edge `0.1737` maxDD `-11.4122`
- `market_context_high->crypto_alt_24h` score `-0.5068` n `66` status `ready` deltaP `16.1142` edge `0.5289` maxDD `-50.438`
- `market_context_high->commodity_1h` score `-0.5618` n `135` status `ready` deltaP `0.8272` edge `-0.0006` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.5904` n `135` status `ready` deltaP `-1.5447` edge `-0.0013` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.7726` n `123` status `ready` deltaP `1.3211` edge `0.0445` maxDD `-5.5222`
- `market_context_high->fx_24h` score `-0.9488` n `66` status `ready` deltaP `2.2886` edge `-0.0028` maxDD `-0.9885`
- `market_context_high->fx_4h` score `-0.9583` n `123` status `ready` deltaP `-2.439` edge `0.0007` maxDD `-1.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
