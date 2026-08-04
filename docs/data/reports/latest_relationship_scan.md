# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T05:07:27.958300+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3995` n `46` status `ready` deltaP `26.2983` edge `2.9456` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.4834` n `46` status `ready` deltaP `45.5616` edge `0.5039` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.2099` n `46` status `ready` deltaP `38.2623` edge `0.447` maxDD `-0.434`
- `market_context_high->unknown_4h` score `6.0899` n `88` status `ready` deltaP `2.1203` edge `0.5929` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2597` n `88` status `ready` deltaP `15.826` edge `0.0841` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.4101` n `88` status `ready` deltaP `19.1519` edge `0.0109` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2613` n `88` status `ready` deltaP `5.8315` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2347` n `88` status `ready` deltaP `8.5806` edge `-0.0028` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4367` n `88` status `ready` deltaP `2.0278` edge `-0.0161` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4487` n `88` status `ready` deltaP `6.1114` edge `0.0252` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5455` n `88` status `ready` deltaP `-1.7692` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9529` n `88` status `ready` deltaP `3.4091` edge `-0.0059` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2863` n `88` status `ready` deltaP `-3.62` edge `-0.012` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4754` n `88` status `ready` deltaP `6.2126` edge `-0.077` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.5884` n `46` status `ready` deltaP `-3.359` edge `0.0106` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7631` n `88` status `ready` deltaP `-8.7445` edge `-0.0423` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.1965` n `88` status `ready` deltaP `3.1982` edge `-0.243` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6295` n `88` status `ready` deltaP `-12.9491` edge `-0.0788` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8324` n `46` status `ready` deltaP `-23.8149` edge `-0.1271` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.3936` n `88` status `ready` deltaP `1.8569` edge `-0.299` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
