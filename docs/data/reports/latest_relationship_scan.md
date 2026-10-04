# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T01:07:51.409283+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `market_context_high->unknown_1h` score `382.3086` n `50` status `ready` deltaP `13.2695` edge `31.7755` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6884` n `50` status `ready` deltaP `12.8049` edge `26.722` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2648` n `50` status `ready` deltaP `29.286` edge `1.0805` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.1683` n `50` status `ready` deltaP `35.5529` edge `0.8353` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.5707` n `62` status `ready` deltaP `28.5711` edge `0.7389` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4605` n `68` status `ready` deltaP `38.0291` edge `0.6385` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1407` n `68` status `ready` deltaP `25.0897` edge `0.5622` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0606` n `50` status `ready` deltaP `16.3232` edge `0.5499` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.424` n `50` status `ready` deltaP `14.2073` edge `0.4862` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4402` n `62` status `ready` deltaP `31.9031` edge `0.1732` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8279` n `68` status `ready` deltaP `26.9637` edge `0.2005` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.0085` n `50` status `ready` deltaP `12.7066` edge `0.2323` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9335` n `50` status `ready` deltaP `32.8415` edge `0.039` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.8672` n `68` status `ready` deltaP `12.6101` edge `0.1904` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8024` n `50` status `ready` deltaP `11.9042` edge `0.1992` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3734` n `68` status `ready` deltaP `20.1399` edge `0.1051` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0078` n `68` status `ready` deltaP `24.7975` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5454` n `50` status `ready` deltaP `21.5389` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4431` n `50` status `ready` deltaP `7.8614` edge `0.3188` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
