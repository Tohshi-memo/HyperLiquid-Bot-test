# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T10:37:31.245134+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0412` n `142` status `ready` deltaP `14.4838` edge `0.5405` maxDD `-6.0235`
- `market_context_high->crypto_major_4h` score `5.7697` n `142` status `ready` deltaP `22.6146` edge `0.4622` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `5.7638` n `68` status `ready` deltaP `32.3081` edge `0.3502` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.7638` n `68` status `ready` deltaP `32.3081` edge `0.3502` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `2.1915` n `68` status `ready` deltaP `8.5186` edge `0.2586` maxDD `-5.9544`
- `risk_on_and_context->crypto_alt_4h` score `2.1915` n `68` status `ready` deltaP `8.5186` edge `0.2586` maxDD `-5.9544`
- `market_context_high->crypto_major_1h` score `0.8631` n `154` status `ready` deltaP `6.7929` edge `0.1072` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5892` n `154` status `ready` deltaP `8.2413` edge `0.1256` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.3767` n `142` status `ready` deltaP `13.0389` edge `0.049` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.2675` n `80` status `ready` deltaP `8.2057` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2675` n `80` status `ready` deltaP `8.2057` edge `0.006` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1145` n `154` status `ready` deltaP `8.3031` edge `0.0048` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.3518` n `154` status `ready` deltaP `7.3392` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.3729` n `80` status `ready` deltaP `10.8071` edge `0.0265` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3729` n `80` status `ready` deltaP `10.8071` edge `0.0265` maxDD `-5.3696`
- `market_context_high->equity_1h` score `-0.3846` n `154` status `ready` deltaP `9.6545` edge `0.0373` maxDD `-7.0778`
- `risk_on_high->crypto_major_1h` score `-0.388` n `80` status `ready` deltaP `4.0494` edge `0.0129` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.388` n `80` status `ready` deltaP `4.0494` edge `0.0129` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
