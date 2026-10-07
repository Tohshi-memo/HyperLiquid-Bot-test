# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T10:52:30.399168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.2377` n `95` status `ready` deltaP `-4.5603` edge `3.1041` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.326` n `62` status `ready` deltaP `35.8379` edge `0.6419` maxDD `-0.6258`
- `market_context_high->unknown_24h` score `7.2197` n `95` status `ready` deltaP `7.4196` edge `0.5902` maxDD `-1.3748`
- `news_risk_high->crypto_alt_4h` score `7.0442` n `62` status `ready` deltaP `23.2396` edge `0.5665` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5989` n `62` status `ready` deltaP `26.0417` edge `0.1263` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9027` n `62` status `ready` deltaP `32.4597` edge `0.0517` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.7799` n `62` status `ready` deltaP `6.9165` edge `0.1955` maxDD `-0.1298`
- `market_context_high->crypto_major_4h` score `2.2712` n `95` status `ready` deltaP `14.4287` edge `0.1895` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.255` n `62` status `ready` deltaP `8.6778` edge `0.1656` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0409` n `62` status `ready` deltaP `18.3861` edge `0.1073` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4414` n `62` status `ready` deltaP `20.4858` edge `0.0898` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1598` n `62` status `ready` deltaP `3.3079` edge `0.1265` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `1.1065` n `95` status `ready` deltaP `5.3454` edge `0.4036` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.9102` n `95` status `ready` deltaP `14.3508` edge `0.0044` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.6344` n `95` status `ready` deltaP `17.1502` edge `0.0142` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.3888` n `62` status `ready` deltaP `26.1537` edge `0.0321` maxDD `-8.196`
- `market_context_high->metal_24h` score `0.3061` n `95` status `ready` deltaP `15.3819` edge `0.0852` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.1939` n `95` status `ready` deltaP `10.4775` edge `0.0439` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1748` n `62` status `ready` deltaP `7.2001` edge `0.0084` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
