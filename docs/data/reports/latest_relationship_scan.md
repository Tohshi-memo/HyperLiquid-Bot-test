# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T02:52:23.778011+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `57.0997` n `50` status `ready` deltaP `19.4107` edge `4.6289` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6355` n `50` status `ready` deltaP `46.6066` edge `2.6197` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.9711` n `50` status `ready` deltaP `27.8475` edge `0.6946` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.8389` n `71` status `ready` deltaP `18.0436` edge `0.6473` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.0759` n `50` status `ready` deltaP `30.1005` edge `0.4818` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.4084` n `120` status `ready` deltaP `12.744` edge `0.5223` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.503` n `50` status `ready` deltaP `43.4073` edge `0.0901` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3202` n `120` status `ready` deltaP `28.7406` edge `0.187` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.5287` n `78` status `ready` deltaP `5.5236` edge `0.2096` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4718` n `50` status `ready` deltaP `26.9948` edge `0.0411` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2881` n `71` status `ready` deltaP `33.3734` edge `0.0231` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.2815` n `120` status `ready` deltaP `17.7033` edge `0.1128` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.8939` n `120` status `ready` deltaP `9.2416` edge `0.0579` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5333` n `78` status `ready` deltaP `11.669` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4281` n `78` status `ready` deltaP `12.287` edge `0.005` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0672` n `120` status `ready` deltaP `10.7113` edge `0.0117` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3483` n `120` status `ready` deltaP `4.3613` edge `-0.0005` maxDD `-0.8587`
- `market_context_high->crypto_major_4h` score `-0.3879` n `120` status `ready` deltaP `13.9431` edge `0.2198` maxDD `-20.9394`
- `news_risk_high->index_1h` score `-0.4138` n `78` status `ready` deltaP `-0.1305` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_alt_4h` score `-0.5494` n `120` status `ready` deltaP `15.1626` edge `0.3131` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
