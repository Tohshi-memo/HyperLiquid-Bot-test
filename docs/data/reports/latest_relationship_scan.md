# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T17:22:29.862759+00:00`
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

- `news_risk_high->unknown_24h` score `4354.2265` n `68` status `ready` deltaP `25.8884` edge `362.7217` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.1067` n `40` status `ready` deltaP `57.0139` edge `1.0852` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9626` n `40` status `ready` deltaP `51.3194` edge `0.5842` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7334` n `68` status `ready` deltaP `17.8981` edge `0.3515` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7277` n `68` status `ready` deltaP `17.1359` edge `0.0678` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0751` n `40` status `ready` deltaP `13.75` edge `0.1308` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7007` n `68` status `ready` deltaP `10.391` edge `0.0714` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6806` n `40` status `ready` deltaP `8.6585` edge `0.1201` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6542` n `40` status `ready` deltaP `20.4573` edge `0.0271` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.6209` n `40` status `ready` deltaP `11.6467` edge `0.0394` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4622` n `40` status `ready` deltaP `14.1467` edge `0.0027` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.3208` n `68` status `ready` deltaP `14.4279` edge `0.0263` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1893` n `68` status `ready` deltaP `6.5369` edge `0.0283` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1162` n `68` status `ready` deltaP `6.6309` edge `0.0389` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0443` n `68` status `ready` deltaP `2.9148` edge `0.0072` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0498` n `68` status `ready` deltaP `3.1173` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1154` n `68` status `ready` deltaP `2.9148` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1525` n `68` status `ready` deltaP `3.267` edge `0.0307` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3918` n `40` status `ready` deltaP `0.7485` edge `0.0075` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.656` n `68` status `ready` deltaP `3.1173` edge `-0.0269` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
