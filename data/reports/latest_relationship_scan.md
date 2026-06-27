# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T21:22:26.335193+00:00`
- Price records: `672`
- Market context records: `4973`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.9899` n `98` status `ready` deltaP `6.2172` edge `1.5078` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.6941` n `89` status `ready` deltaP `28.5164` edge `0.9203` maxDD `-1.8723`
- `market_context_high->crypto_major_4h` score `7.2975` n `89` status `ready` deltaP `20.2555` edge `0.5955` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.8954` n `89` status `ready` deltaP `20.8259` edge `0.571` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8906` n `85` status `ready` deltaP `27.741` edge `0.3402` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7103` n `89` status `ready` deltaP `13.2262` edge `0.1925` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5982` n `89` status `ready` deltaP `12.8871` edge `0.126` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8567` n `89` status `ready` deltaP `10.8095` edge `0.0455` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.5162` n `98` status `ready` deltaP `7.2926` edge `0.0749` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.4017` n `98` status `ready` deltaP `4.6407` edge `0.1244` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3258` n `98` status `ready` deltaP `6.7212` edge `0.0992` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0547` n `98` status `ready` deltaP `2.7496` edge `0.0351` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3995` n `98` status `ready` deltaP `1.1029` edge `0.0074` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4287` n `98` status `ready` deltaP `1.1426` edge `0.0129` maxDD `-0.7054`
- `market_context_high->fx_24h` score `-0.9908` n `85` status `ready` deltaP `0.433` edge `-0.0071` maxDD `-1.9348`
- `market_context_high->fx_4h` score `-1.0922` n `89` status `ready` deltaP `-6.0274` edge `-0.0028` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.3295` n `89` status `ready` deltaP `3.8812` edge `-0.0114` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.5884` n `98` status `ready` deltaP `-10.2438` edge `-0.0041` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.0108` n `85` status `ready` deltaP `16.2725` edge `0.0164` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9828` n `85` status `ready` deltaP `-8.2067` edge `0.0183` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
