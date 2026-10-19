# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T03:22:28.517417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->commodity_24h` score `1.4186` n `82` status `ready` deltaP `14.5599` edge `0.1063` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.9225` n `49` status `ready` deltaP `16.3021` edge `0.0281` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.9225` n `49` status `ready` deltaP `16.3021` edge `0.0281` maxDD `-2.1255`
- `market_context_high->crypto_major_4h` score `0.863` n `82` status `ready` deltaP `8.3841` edge `0.3952` maxDD `-15.2359`
- `market_context_high->equity_24h` score `0.8069` n `82` status `ready` deltaP `2.4772` edge `0.9696` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `0.5924` n `82` status `ready` deltaP `3.7559` edge `0.6606` maxDD `-35.1086`
- `market_context_high->crypto_major_1h` score `0.532` n `83` status `ready` deltaP `5.4289` edge `0.1209` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.5037` n `49` status `ready` deltaP `10.8077` edge `0.0011` maxDD `-0.4943`
- `risk_on_and_context->index_1h` score `0.5037` n `49` status `ready` deltaP `10.8077` edge `0.0011` maxDD `-0.4943`
- `risk_on_high->fx_1h` score `0.1254` n `49` status `ready` deltaP `6.5423` edge `0.0015` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `0.1254` n `49` status `ready` deltaP `6.5423` edge `0.0015` maxDD `-0.1065`
- `risk_on_high->commodity_24h` score `0.12` n `49` status `ready` deltaP `11.9965` edge `0.0098` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.12` n `49` status `ready` deltaP `11.9965` edge `0.0098` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.3399` n `49` status `ready` deltaP `-0.7676` edge `0.0036` maxDD `-0.1446`
- `risk_on_and_context->fx_4h` score `-0.3399` n `49` status `ready` deltaP `-0.7676` edge `0.0036` maxDD `-0.1446`
- `market_context_high->fx_1h` score `-0.4748` n `83` status `ready` deltaP `-1.203` edge `-0.0003` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5324` n `82` status `ready` deltaP `-1.3649` edge `0.0039` maxDD `-0.7115`
- `risk_on_high->equity_4h` score `-0.5761` n `49` status `ready` deltaP `2.8958` edge `0.0975` maxDD `-7.1849`
- `risk_on_and_context->equity_4h` score `-0.5761` n `49` status `ready` deltaP `2.8958` edge `0.0975` maxDD `-7.1849`
- `market_context_high->crypto_alt_1h` score `-0.6349` n `83` status `ready` deltaP `-1.2301` edge `0.0768` maxDD `-7.3329`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
