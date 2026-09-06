# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T18:22:59.297925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10185`

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

- `risk_on_high->unknown_24h` score `210.5781` n `103` status `ready` deltaP `25.2124` edge `17.39` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `210.5781` n `103` status `ready` deltaP `25.2124` edge `17.39` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `18.5488` n `103` status `ready` deltaP `32.376` edge `1.4613` maxDD `-7.8459`
- `risk_on_and_context->crypto_major_24h` score `18.5488` n `103` status `ready` deltaP `32.376` edge `1.4613` maxDD `-7.8459`
- `risk_on_high->crypto_alt_24h` score `9.4724` n `103` status `ready` deltaP `20.9884` edge `0.8038` maxDD `-8.682`
- `risk_on_and_context->crypto_alt_24h` score `9.4724` n `103` status `ready` deltaP `20.9884` edge `0.8038` maxDD `-8.682`
- `market_context_high->crypto_alt_24h` score `5.6228` n `196` status `ready` deltaP `18.8634` edge `0.5225` maxDD `-10.0415`
- `market_context_high->equity_24h` score `5.4823` n `196` status `ready` deltaP `20.3976` edge `0.3893` maxDD `-2.8075`
- `risk_on_high->equity_24h` score `4.1939` n `103` status `ready` deltaP `16.7122` edge `0.3065` maxDD `-2.8075`
- `risk_on_and_context->equity_24h` score `4.1939` n `103` status `ready` deltaP `16.7122` edge `0.3065` maxDD `-2.8075`
- `market_context_high->index_24h` score `1.1162` n `196` status `ready` deltaP `17.9209` edge `0.0864` maxDD `-2.6954`
- `risk_on_high->index_24h` score `1.0688` n `103` status `ready` deltaP `15.5036` edge `0.0672` maxDD `-2.186`
- `risk_on_and_context->index_24h` score `1.0688` n `103` status `ready` deltaP `15.5036` edge `0.0672` maxDD `-2.186`
- `risk_on_high->index_1h` score `0.0064` n `129` status `ready` deltaP `7.2947` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0064` n `129` status `ready` deltaP `7.2947` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_24h` score `-0.0345` n `103` status `ready` deltaP `14.7013` edge `0.071` maxDD `-6.7507`
- `risk_on_and_context->metal_24h` score `-0.0345` n `103` status `ready` deltaP `14.7013` edge `0.071` maxDD `-6.7507`
- `risk_on_high->metal_1h` score `-0.2657` n `129` status `ready` deltaP `5.8569` edge `-0.0026` maxDD `-1.6408`
- `risk_on_and_context->metal_1h` score `-0.2657` n `129` status `ready` deltaP `5.8569` edge `-0.0026` maxDD `-1.6408`
- `risk_on_high->crypto_alt_1h` score `-0.309` n `129` status `ready` deltaP `2.6006` edge `0.0586` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
