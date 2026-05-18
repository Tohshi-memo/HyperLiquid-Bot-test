# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T02:37:12.311081+00:00`
- Price records: `672`
- Market context records: `1075`
- Flow alert records: `5000`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.2326` n `162` status `ready` deltaP `34.9607` edge `1.166` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.6875` n `162` status `ready` deltaP `12.009` edge `0.5173` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.2202` n `162` status `ready` deltaP `14.1414` edge `0.3904` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.3706` n `162` status `ready` deltaP `-2.2447` edge `0.5459` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3682` n `162` status `ready` deltaP `14.7026` edge `0.2968` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.548` n `164` status `ready` deltaP `8.689` edge `0.1499` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.2718` n `164` status `ready` deltaP `12.9573` edge `0.1882` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.7862` n `164` status `ready` deltaP `6.7073` edge `0.0891` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6237` n `170` status `ready` deltaP `8.2599` edge `0.0286` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5336` n `170` status `ready` deltaP `2.9447` edge `0.0626` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.3423` n `170` status `ready` deltaP `8.193` edge `0.0409` maxDD `-3.3594`
- `market_context_high->fx_1h` score `0.0152` n `170` status `ready` deltaP `6.8457` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.0892` n `170` status `ready` deltaP `7.3811` edge `0.0044` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3221` n `170` status `ready` deltaP `2.825` edge `0.0386` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.5148` n `164` status `ready` deltaP `6.8597` edge `0.1618` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.676` n `164` status `ready` deltaP `1.6768` edge `0.0018` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6811` n `170` status `ready` deltaP `-0.9951` edge `0.0001` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.9455` n `164` status `ready` deltaP `4.5731` edge `-0.0845` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.7443` n `164` status `ready` deltaP `8.0793` edge `-0.1484` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.0706` n `162` status `ready` deltaP `5.275` edge `-0.0212` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
