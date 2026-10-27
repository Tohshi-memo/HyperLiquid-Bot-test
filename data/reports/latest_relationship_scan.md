# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T16:22:45.695748+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8641`

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

- `market_context_high->unknown_4h` score `81.0118` n `135` status `ready` deltaP `4.5472` edge `6.7359` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `12.4019` n `137` status `ready` deltaP `0.7081` edge `1.0777` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9975` n `135` status `ready` deltaP `27.1875` edge `0.054` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4718` n `137` status `ready` deltaP `10.7894` edge `0.0032` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3836` n `135` status `ready` deltaP `12.2866` edge `0.0099` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0696` n `137` status `ready` deltaP `8.7679` edge `0.0073` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.1622` n `137` status `ready` deltaP `3.5469` edge `0.0129` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4326` n `135` status `ready` deltaP `6.0795` edge `0.0453` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.5135` n `137` status `ready` deltaP `5.6799` edge `0.0246` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5735` n `137` status `ready` deltaP `-0.365` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5994` n `135` status `ready` deltaP `9.132` edge `0.0195` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8257` n `135` status `ready` deltaP `8.0137` edge `-0.0052` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9489` n `135` status `ready` deltaP `16.0995` edge `0.0914` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.446` n `137` status `ready` deltaP `1.8991` edge `-0.0068` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.8618` n `135` status `ready` deltaP `8.0671` edge `0.0875` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9528` n `137` status `ready` deltaP `-0.9463` edge `-0.0077` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.8407` n `135` status `ready` deltaP `-6.4702` edge `-0.0314` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7977` n `135` status `ready` deltaP `3.2024` edge `-0.0763` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.9225` n `135` status `ready` deltaP `0.544` edge `-0.0208` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.3171` n `135` status `ready` deltaP `0.7182` edge `-0.1631` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
