# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T15:16:17.007442+00:00`
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

- `news_risk_high->unknown_24h` score `4848.5167` n `63` status `ready` deltaP `26.8105` edge `403.9064` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.4878` n `40` status `ready` deltaP `58.4028` edge `1.1077` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.857` n `40` status `ready` deltaP `51.3194` edge `0.5754` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.8488` n `68` status `ready` deltaP `18.9652` edge `0.354` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.8349` n `68` status `ready` deltaP `18.3554` edge `0.0686` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9774` n `40` status `ready` deltaP `12.5305` edge `0.1264` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7402` n `68` status `ready` deltaP `10.6904` edge `0.0727` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7398` n `40` status `ready` deltaP `9.4207` edge `0.1226` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.5917` n `40` status `ready` deltaP `19.3902` edge `0.0262` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5766` n `40` status `ready` deltaP `10.8982` edge `0.0387` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4629` n `40` status `ready` deltaP `14.1467` edge `0.0028` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2246` n `68` status `ready` deltaP `13.3608` edge `0.0254` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1988` n `68` status `ready` deltaP `6.6894` edge `0.0285` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1193` n `68` status `ready` deltaP `6.7806` edge `0.0383` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.049` n `68` status `ready` deltaP `3.1173` edge `0.0052` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.059` n `68` status `ready` deltaP `2.6154` edge `0.0073` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.0991` n `68` status `ready` deltaP `3.2142` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1345` n `68` status `ready` deltaP `3.4167` edge `0.032` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3887` n `40` status `ready` deltaP `0.8982` edge `0.0069` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.7004` n `68` status `ready` deltaP `2.3688` edge `-0.0276` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
