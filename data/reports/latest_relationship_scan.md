# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T13:07:32.753632+00:00`
- Price records: `672`
- Market context records: `5146`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `26.5155` n `67` status `ready` deltaP `31.3925` edge `2.0346` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.4447` n `128` status `ready` deltaP `18.8072` edge `0.5139` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.6263` n `140` status `ready` deltaP `10.231` edge `0.4648` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.0956` n `128` status `ready` deltaP `15.968` edge `0.4781` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.875` n `128` status `ready` deltaP `13.9292` edge `0.4593` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `1.8053` n `67` status `ready` deltaP `17.3793` edge `0.6152` maxDD `-41.4495`
- `market_context_high->crypto_major_24h` score `1.1799` n `67` status `ready` deltaP `15.853` edge `0.6137` maxDD `-43.0186`
- `market_context_high->equity_4h` score `1.1132` n `128` status `ready` deltaP `11.0899` edge `0.1827` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.8983` n `140` status `ready` deltaP `8.2806` edge `0.1442` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8898` n `140` status `ready` deltaP `5.8511` edge `0.1313` maxDD `-5.0257`
- `market_context_high->commodity_24h` score `0.8744` n `67` status `ready` deltaP `16.5423` edge `0.1251` maxDD `-5.1955`
- `market_context_high->equity_1h` score `0.6143` n `140` status `ready` deltaP `7.0958` edge `0.0632` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.0166` n `67` status `ready` deltaP `-1.3319` edge `0.1837` maxDD `-8.8149`
- `market_context_high->metal_1h` score `-0.0372` n `140` status `ready` deltaP `5.2053` edge `0.0171` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.0929` n `140` status `ready` deltaP `4.3541` edge `0.0136` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.3778` n `128` status `ready` deltaP `6.593` edge `0.0363` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4365` n `67` status `ready` deltaP `4.7368` edge `0.002` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4774` n `140` status `ready` deltaP `-0.1155` edge `-0.0008` maxDD `-0.7711`
- `market_context_high->commodity_1h` score `-0.6506` n `140` status `ready` deltaP `-0.3807` edge `-0.0012` maxDD `-2.3737`
- `market_context_high->fx_4h` score `-0.8048` n `128` status `ready` deltaP `0.0572` edge `0.0025` maxDD `-1.8177`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
