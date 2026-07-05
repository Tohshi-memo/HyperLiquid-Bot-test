# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T01:20:58.456688+00:00`
- Price records: `672`
- Market context records: `5723`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9885` n `218` status `ready` deltaP `16.7447` edge `0.523` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.6091` n `273` status `ready` deltaP `9.1927` edge `0.1877` maxDD `-10.5251`
- `market_context_high->equity_4h` score `0.1988` n `273` status `ready` deltaP `7.55` edge `0.1301` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2061` n `285` status `ready` deltaP `3.0854` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4549` n `285` status `ready` deltaP `1.4855` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6118` n `285` status `ready` deltaP `3.3617` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7411` n `285` status `ready` deltaP `-1.4387` edge `-0.0047` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.898` n `285` status `ready` deltaP `2.6316` edge `0.0311` maxDD `-5.5448`
- `market_context_high->crypto_alt_4h` score `-0.9132` n `273` status `ready` deltaP `6.8743` edge `0.1329` maxDD `-13.0531`
- `market_context_high->crypto_alt_1h` score `-1.0582` n `285` status `ready` deltaP `0.737` edge `0.0273` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1219` n `218` status `ready` deltaP `10.8611` edge `0.0421` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1514` n `273` status `ready` deltaP `1.5323` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2575` n `273` status `ready` deltaP `2.6267` edge `0.0058` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5881` n `273` status `ready` deltaP `-6.7107` edge `-0.0495` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8863` n `218` status `ready` deltaP `2.2681` edge `0.0293` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8467` n `273` status `ready` deltaP `-3.6753` edge `-0.0285` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3497` n `218` status `ready` deltaP `7.0225` edge `0.0364` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5567` n `218` status `ready` deltaP `-6.2133` edge `-0.2389` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3536` n `218` status `ready` deltaP `-9.5327` edge `-0.0686` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
