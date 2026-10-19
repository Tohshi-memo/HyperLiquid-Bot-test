# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T03:07:26.621648+00:00`
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

- `market_context_high->commodity_24h` score `1.4581` n `83` status `ready` deltaP `14.724` edge `0.1085` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `0.9334` n `83` status `ready` deltaP `8.9865` edge `0.4002` maxDD `-15.2359`
- `risk_on_high->equity_1h` score `0.8419` n `50` status `ready` deltaP `15.3093` edge `0.028` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.8419` n `50` status `ready` deltaP `15.3093` edge `0.028` maxDD `-2.1255`
- `market_context_high->crypto_major_1h` score `0.4906` n `84` status `ready` deltaP `4.9045` edge `0.1191` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.4281` n `50` status `ready` deltaP `9.8559` edge `0.0012` maxDD `-0.4988`
- `risk_on_and_context->index_1h` score `0.4281` n `50` status `ready` deltaP `9.8559` edge `0.0012` maxDD `-0.4988`
- `market_context_high->crypto_major_24h` score `0.3889` n `83` status `ready` deltaP `3.5475` edge `0.6359` maxDD `-35.1086`
- `risk_on_high->commodity_24h` score `0.2355` n `50` status `ready` deltaP `12.4348` edge `0.0165` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2355` n `50` status `ready` deltaP `12.4348` edge `0.0165` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1952` n `50` status `ready` deltaP `7.3994` edge `0.0016` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `0.1952` n `50` status `ready` deltaP `7.3994` edge `0.0016` maxDD `-0.1065`
- `market_context_high->equity_24h` score `0.0593` n `83` status `ready` deltaP `2.3573` edge `0.9382` maxDD `-58.251`
- `risk_on_high->fx_4h` score `-0.4054` n `50` status `ready` deltaP `-1.5535` edge `0.0034` maxDD `-0.146`
- `risk_on_and_context->fx_4h` score `-0.4054` n `50` status `ready` deltaP `-1.5535` edge `0.0034` maxDD `-0.146`
- `market_context_high->fx_1h` score `-0.4434` n `84` status `ready` deltaP `-0.6006` edge `-0.0003` maxDD `-0.537`
- `market_context_high->fx_4h` score `-0.5543` n `83` status `ready` deltaP `-1.7704` edge `0.0038` maxDD `-0.7115`
- `risk_on_high->crypto_major_4h` score `-0.5583` n `50` status `ready` deltaP `2.3841` edge `0.1606` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `-0.5583` n `50` status `ready` deltaP `2.3841` edge `0.1606` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `-0.6711` n `84` status `ready` deltaP `-1.7608` edge `0.0757` maxDD `-7.3329`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
