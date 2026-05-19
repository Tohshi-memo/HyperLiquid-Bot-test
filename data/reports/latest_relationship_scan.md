# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T17:37:19.991468+00:00`
- Price records: `672`
- Market context records: `1241`
- Flow alert records: `5480`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.5945` n `128` status `ready` deltaP `43.4895` edge `1.3728` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0525` n `128` status `ready` deltaP `5.0686` edge `0.7589` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8145` n `128` status `ready` deltaP `22.6562` edge `0.7018` maxDD `-15.1306`
- `market_context_high->metal_24h` score `7.2585` n `128` status `ready` deltaP `0.8681` edge `0.7658` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.0269` n `128` status `ready` deltaP `-7.1181` edge `0.5312` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.7606` n `128` status `ready` deltaP `22.7431` edge `0.2704` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.4748` n `128` status `ready` deltaP `17.5495` edge `0.2389` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.1982` n `128` status `ready` deltaP `22.3958` edge `0.4934` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `1.8474` n `128` status `ready` deltaP `1.5625` edge `0.4165` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6359` n `128` status `ready` deltaP `14.0434` edge `0.111` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6756` n `128` status `ready` deltaP `9.899` edge `0.022` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5439` n `128` status `ready` deltaP `5.3096` edge `0.0468` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4484` n `128` status `ready` deltaP `6.8577` edge `0.0381` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1959` n `128` status `ready` deltaP `15.4536` edge `0.0564` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.1766` n `128` status `ready` deltaP `10.2685` edge `0.0073` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `-0.0243` n `128` status `ready` deltaP `6.7645` edge `0.1439` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3102` n `128` status `ready` deltaP `0.6456` edge `0.0402` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4611` n `128` status `ready` deltaP `1.7777` edge `0.0056` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6724` n `128` status `ready` deltaP `8.0983` edge `0.1563` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
