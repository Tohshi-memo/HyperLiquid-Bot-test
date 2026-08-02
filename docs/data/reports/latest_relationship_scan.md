# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T16:07:24.224161+00:00`
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

- `news_risk_high->unknown_24h` score `4641.6958` n `65` status `ready` deltaP `26.4851` edge `386.6735` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.349` n `40` status `ready` deltaP `57.8819` edge `1.0996` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8906` n `40` status `ready` deltaP `51.3194` edge `0.5782` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.8196` n `68` status `ready` deltaP `18.6603` edge `0.3536` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7959` n `68` status `ready` deltaP `17.8981` edge `0.0684` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0129` n `40` status `ready` deltaP `12.9878` edge `0.1279` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7311` n `40` status `ready` deltaP `9.2683` edge `0.1225` maxDD `-4.9116`
- `news_risk_high->equity_1h` score `0.7271` n `68` status `ready` deltaP `10.5407` edge `0.0726` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.6091` n `40` status `ready` deltaP `19.6951` edge `0.0264` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5929` n `40` status `ready` deltaP `11.1976` edge `0.0388` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4622` n `40` status `ready` deltaP `14.1467` edge `0.0027` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2514` n `68` status `ready` deltaP `13.6657` edge `0.0256` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1988` n `68` status `ready` deltaP `6.6894` edge `0.0285` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1372` n `68` status `ready` deltaP `6.9303` edge `0.0396` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0349` n `68` status `ready` deltaP `3.0645` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0498` n `68` status `ready` deltaP `3.1173` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1069` n `68` status `ready` deltaP `3.0645` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1205` n `68` status `ready` deltaP `3.5664` edge `0.0328` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3708` n `40` status `ready` deltaP `1.0479` edge `0.0082` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6841` n `68` status `ready` deltaP `2.6682` edge `-0.0275` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
