# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T14:37:30.528812+00:00`
- Price records: `672`
- Market context records: `5153`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.3233` n `63` status `ready` deltaP `34.623` edge `2.3151` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.5331` n `130` status `ready` deltaP `19.7162` edge `0.5152` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.4994` n `141` status `ready` deltaP `10.3548` edge `0.4534` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.2729` n `130` status `ready` deltaP `16.2641` edge `0.4909` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `5.0396` n `63` status `ready` deltaP `19.8909` edge `0.8522` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.8654` n `63` status `ready` deltaP `18.0803` edge `0.8694` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `4.2533` n `130` status `ready` deltaP `14.878` edge `0.4845` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0033` n `63` status `ready` deltaP `20.2381` edge `0.1553` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.0312` n `130` status `ready` deltaP `10.7692` edge `0.178` maxDD `-7.4425`
- `market_context_high->metal_24h` score `0.9863` n `63` status `ready` deltaP `0.9424` edge `0.251` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.841` n `141` status `ready` deltaP `8.0604` edge `0.1409` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.825` n `141` status `ready` deltaP `5.626` edge `0.1274` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.0976` n `141` status `ready` deltaP `6.7057` edge `0.0524` maxDD `-4.4338`
- `market_context_high->metal_1h` score `-0.0364` n `141` status `ready` deltaP `5.4051` edge `0.0161` maxDD `-1.8777`
- `market_context_high->index_1h` score `-0.1285` n `141` status `ready` deltaP `3.4197` edge `0.0111` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2363` n `141` status `ready` deltaP `2.1829` edge `0.0004` maxDD `-0.6194`
- `market_context_high->fx_24h` score `-0.3655` n `63` status `ready` deltaP `7.3909` edge `0.0098` maxDD `-0.8294`
- `market_context_high->index_4h` score `-0.4797` n `130` status `ready` deltaP `5.7997` edge `0.0331` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6085` n `130` status `ready` deltaP `2.9526` edge `0.0057` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6433` n `141` status `ready` deltaP `-0.1656` edge `-0.0005` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
