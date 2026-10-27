# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T15:37:33.531866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8542`

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

- `market_context_high->unknown_4h` score `80.8378` n `135` status `ready` deltaP `4.5472` edge `6.7214` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.7145` n `135` status `ready` deltaP `0.7696` edge `1.27` maxDD `-1.5807`
- `market_context_high->index_24h` score `2.0035` n `135` status `ready` deltaP `27.1875` edge `0.0545` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5062` n `135` status `ready` deltaP `11.2054` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3446` n `135` status `ready` deltaP `11.8293` edge `0.0097` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0529` n `135` status `ready` deltaP `8.9987` edge `0.0079` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2231` n `135` status `ready` deltaP `2.8765` edge `0.0123` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4848` n `135` status `ready` deltaP `5.6222` edge `0.044` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.5456` n `135` status `ready` deltaP `5.2872` edge `0.0231` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.6045` n `135` status `ready` deltaP `-0.8117` edge `-0.0038` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6312` n `135` status `ready` deltaP `8.6111` edge `0.0189` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8179` n `135` status `ready` deltaP `8.0137` edge `-0.0042` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9513` n `135` status `ready` deltaP `16.0995` edge `0.0912` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.5158` n `135` status `ready` deltaP `1.4415` edge `-0.0127` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.9314` n `135` status `ready` deltaP `8.0671` edge `0.0817` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-2.0029` n `135` status `ready` deltaP `-1.4904` edge `-0.0105` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.7897` n `135` status `ready` deltaP `-6.0129` edge `-0.0302` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.779` n `135` status `ready` deltaP `3.2024` edge `-0.0739` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.9865` n `135` status `ready` deltaP `0.544` edge `-0.029` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.2523` n `135` status `ready` deltaP `0.8706` edge `-0.1558` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
