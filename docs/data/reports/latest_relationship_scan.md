# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T21:37:26.579449+00:00`
- Price records: `672`
- Market context records: `4762`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.3548` n `131` status `ready` deltaP `12.9543` edge `0.5683` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.749` n `129` status `ready` deltaP `15.6385` edge `0.5792` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.705` n `116` status `ready` deltaP `13.9128` edge `0.225` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2258` n `131` status `ready` deltaP `3.0317` edge `0.0239` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.3462` n `129` status `ready` deltaP `9.3815` edge `0.0357` maxDD `-6.41`
- `market_context_high->equity_4h` score `-0.3952` n `129` status `ready` deltaP `8.0131` edge `0.0645` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4749` n `129` status `ready` deltaP `6.1189` edge `0.0052` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5932` n `129` status `ready` deltaP `0.2222` edge `0.0001` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6817` n `131` status `ready` deltaP `0.0971` edge `-0.0111` maxDD `-4.156`
- `market_context_high->fx_1h` score `-1.1177` n `131` status `ready` deltaP `-3.6442` edge `-0.0039` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5459` n `131` status `ready` deltaP `-3.0763` edge `-0.0079` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.3447` n `116` status `ready` deltaP `18.5525` edge `0.0866` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3452` n `131` status `ready` deltaP `-1.833` edge `-0.0676` maxDD `-14.3342`
- `market_context_high->crypto_major_1h` score `-3.419` n `131` status `ready` deltaP `-1.1896` edge `-0.0873` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.8274` n `116` status `ready` deltaP `-14.9784` edge `-0.0205` maxDD `-3.8875`
- `market_context_high->crypto_alt_1h` score `-4.6904` n `131` status `ready` deltaP `-2.6866` edge `-0.0751` maxDD `-19.8288`
- `market_context_high->crypto_alt_4h` score `-5.3812` n `129` status `ready` deltaP `2.5348` edge `-0.0414` maxDD `-47.8982`
- `market_context_high->index_24h` score `-6.4593` n `116` status `ready` deltaP `-9.381` edge `-0.1115` maxDD `-21.1387`
- `market_context_high->crypto_major_4h` score `-8.2264` n `129` status `ready` deltaP `2.6742` edge `-0.1494` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2992` n `129` status `ready` deltaP `6.0408` edge `-0.2802` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
