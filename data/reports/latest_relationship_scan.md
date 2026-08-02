# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T18:07:27.213662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4354.0696` n `68` status `ready` deltaP `25.3676` edge `362.7121` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.9475` n `40` status `ready` deltaP `56.4931` edge `1.0754` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0022` n `40` status `ready` deltaP `51.3194` edge `0.5875` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7032` n `68` status `ready` deltaP `17.7456` edge `0.35` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6863` n `68` status `ready` deltaP `16.6786` edge `0.0674` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.1114` n `40` status `ready` deltaP `14.2073` edge `0.1324` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.6796` n `40` status `ready` deltaP `20.9146` edge `0.0273` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6719` n `68` status `ready` deltaP `10.0916` edge `0.071` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6515` n `40` status `ready` deltaP `8.3537` edge `0.1184` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.6474` n `40` status `ready` deltaP `12.0958` edge `0.0398` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4707` n `40` status `ready` deltaP `14.2964` edge `0.0028` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.3598` n `68` status `ready` deltaP `14.8852` edge `0.0265` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1893` n `68` status `ready` deltaP `6.5369` edge `0.0283` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0858` n `68` status `ready` deltaP `6.1818` edge `0.038` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0412` n `68` status `ready` deltaP `3.267` edge `0.0052` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0443` n `68` status `ready` deltaP `2.9148` edge `0.0072` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1077` n `68` status `ready` deltaP `3.0645` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1859` n `68` status `ready` deltaP `2.8179` edge `0.0294` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4222` n `40` status `ready` deltaP `0.2994` edge `0.0066` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6296` n `68` status `ready` deltaP `3.5664` edge `-0.0265` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
