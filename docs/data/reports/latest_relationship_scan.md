# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T02:37:31.986945+00:00`
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

- `news_risk_high->unknown_24h` score `57.0186` n `50` status `ready` deltaP `19.2374` edge `4.6233` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6691` n `50` status `ready` deltaP `46.6066` edge `2.6225` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.8924` n `50` status `ready` deltaP `27.6742` edge `0.6892` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.8135` n `71` status `ready` deltaP `17.8911` edge `0.6462` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.0387` n `50` status `ready` deltaP `30.1005` edge `0.4787` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.3273` n `120` status `ready` deltaP `12.5707` edge `0.5167` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4994` n `50` status `ready` deltaP `43.4073` edge `0.0898` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3166` n `120` status `ready` deltaP `28.7406` edge `0.1867` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6881` n `77` status `ready` deltaP `6.2563` edge `0.218` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4682` n `50` status `ready` deltaP `26.9948` edge `0.0408` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2747` n `71` status `ready` deltaP `33.2209` edge `0.023` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.2561` n `120` status `ready` deltaP `17.5508` edge `0.1117` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.8783` n `120` status `ready` deltaP `9.0918` edge `0.0576` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5838` n `77` status `ready` deltaP `12.2852` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4022` n `77` status `ready` deltaP `11.7875` edge `0.005` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0585` n `120` status `ready` deltaP `10.8638` edge `0.0118` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3561` n `120` status `ready` deltaP `4.2116` edge `-0.0005` maxDD `-0.8587`
- `market_context_high->crypto_major_4h` score `-0.4181` n `120` status `ready` deltaP `13.7906` edge `0.2183` maxDD `-20.9394`
- `news_risk_high->index_1h` score `-0.4497` n `77` status `ready` deltaP `-0.7465` edge `-0.009` maxDD `-0.8275`
- `market_context_high->crypto_alt_4h` score `-0.5298` n `120` status `ready` deltaP `15.315` edge `0.3146` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
