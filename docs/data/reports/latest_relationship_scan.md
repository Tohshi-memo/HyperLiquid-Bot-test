# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T04:52:24.044826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `8.5224` n `64` status `ready` deltaP `22.9421` edge `0.6001` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.5224` n `64` status `ready` deltaP `22.9421` edge `0.6001` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `4.9522` n `166` status `ready` deltaP `19.29` edge `0.3311` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6469` n `102` status `ready` deltaP `33.8644` edge `0.2634` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.2021` n `64` status `ready` deltaP `22.904` edge `0.2258` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.2021` n `64` status `ready` deltaP `22.904` edge `0.2258` maxDD `-0.5985`
- `risk_on_high->equity_4h` score `2.9087` n `64` status `ready` deltaP `26.2576` edge `0.086` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `2.9087` n `64` status `ready` deltaP `26.2576` edge `0.086` maxDD `-0.1594`
- `risk_on_high->unknown_1h` score `2.627` n `64` status `ready` deltaP `5.2957` edge `0.2125` maxDD `-0.9779`
- `risk_on_and_context->unknown_1h` score `2.627` n `64` status `ready` deltaP `5.2957` edge `0.2125` maxDD `-0.9779`
- `risk_on_high->crypto_alt_4h` score `2.5933` n `64` status `ready` deltaP `14.7104` edge `0.2827` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.5933` n `64` status `ready` deltaP `14.7104` edge `0.2827` maxDD `-1.5298`
- `market_context_high->unknown_1h` score `2.1755` n `166` status `ready` deltaP `10.1526` edge `0.155` maxDD `-0.9779`
- `risk_on_high->index_4h` score `1.9888` n `64` status `ready` deltaP `26.372` edge `0.0118` maxDD `-0.084`
- `risk_on_and_context->index_4h` score `1.9888` n `64` status `ready` deltaP `26.372` edge `0.0118` maxDD `-0.084`
- `risk_on_high->metal_4h` score `1.7788` n `64` status `ready` deltaP `22.561` edge `0.0276` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7788` n `64` status `ready` deltaP `22.561` edge `0.0276` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.4009` n `64` status `ready` deltaP `18.881` edge `0.0079` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.4009` n `64` status `ready` deltaP `18.881` edge `0.0079` maxDD `-0.0291`
- `news_risk_high->unknown_1h` score `1.2483` n `32` status `ready` deltaP `-13.4543` edge `0.2239` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
