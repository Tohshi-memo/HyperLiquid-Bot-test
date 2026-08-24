# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T15:37:30.768982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.9054` n `51` status `ready` deltaP `14.7569` edge `3.8104` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.6027` n `51` status `ready` deltaP `40.237` edge `0.9584` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8929` n `51` status `ready` deltaP `24.1063` edge `0.9183` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.518` n `51` status `ready` deltaP `48.9481` edge `0.1487` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.8678` n `81` status `ready` deltaP `8.5841` edge `0.3777` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.111` n `51` status `ready` deltaP `27.995` edge `0.233` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5838` n `51` status `ready` deltaP `16.3349` edge `0.2202` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3016` n `51` status `ready` deltaP `38.8451` edge `0.0296` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6884` n `130` status `ready` deltaP `19.144` edge `0.0539` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0795` n `51` status `ready` deltaP `15.0735` edge `0.0292` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0574` n `51` status `ready` deltaP `19.0912` edge `0.0447` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.9324` n `51` status `ready` deltaP `28.5948` edge `-0.1087` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2785` n `51` status `ready` deltaP `9.7217` edge `0.0062` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1895` n `51` status `ready` deltaP `8.3891` edge `-0.0093` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1779` n `130` status `ready` deltaP `11.4775` edge `-0.0158` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0409` n `130` status `ready` deltaP `10.9051` edge `-0.0244` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1263` n `51` status `ready` deltaP `2.043` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2481` n `51` status `ready` deltaP `6.6057` edge `-0.0116` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4318` n `130` status `ready` deltaP `2.561` edge `0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
