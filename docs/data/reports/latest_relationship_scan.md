# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T04:22:16.328405+00:00`
- Price records: `672`
- Market context records: `1594`
- Flow alert records: `6504`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.9879` n `182` status `ready` deltaP `30.2407` edge `1.0641` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.6733` n `182` status `ready` deltaP `27.171` edge `1.0766` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.852` n `182` status `ready` deltaP `26.9135` edge `0.8381` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.1461` n `182` status `ready` deltaP `20.8391` edge `0.5226` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2446` n `182` status `ready` deltaP `22.3424` edge `0.3134` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1459` n `199` status `ready` deltaP `9.8166` edge `0.1395` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1328` n `199` status `ready` deltaP `12.4923` edge `0.2657` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0423` n `199` status `ready` deltaP `8.8223` edge `0.2175` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.0736` n `182` status `ready` deltaP `8.8904` edge `0.0395` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3636` n `199` status `ready` deltaP `0.5183` edge `0.0523` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5491` n `199` status `ready` deltaP `0.9133` edge `0.029` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5946` n `199` status `ready` deltaP `-1.3954` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7142` n `199` status `ready` deltaP `5.4472` edge `0.0057` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7224` n `199` status `ready` deltaP `0.0256` edge `0.0028` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.8255` n `199` status `ready` deltaP `-1.6948` edge `-0.0024` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8849` n `199` status `ready` deltaP `-0.5935` edge `0.0262` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0301` n `199` status `ready` deltaP `-1.0862` edge `0.0303` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3031` n `199` status `ready` deltaP `10.3636` edge `0.0915` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3712` n `199` status `ready` deltaP `-10.2448` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.244` n `199` status `ready` deltaP `-14.7001` edge `-0.1116` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
