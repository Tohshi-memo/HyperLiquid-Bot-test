# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T14:52:30.971782+00:00`
- Price records: `672`
- Market context records: `2672`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.0437` n `111` status `ready` deltaP `16.0051` edge `0.9963` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5517` n `111` status `ready` deltaP `17.3048` edge `0.6301` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2132` n `126` status `ready` deltaP `22.4279` edge `0.4667` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.1545` n `126` status `ready` deltaP `10.1917` edge `0.2926` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.517` n `126` status `ready` deltaP `7.7841` edge `0.1795` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.1958` n `135` status `ready` deltaP `7.6281` edge `0.0842` maxDD `-6.1656`
- `market_context_high->index_4h` score `-0.0964` n `126` status `ready` deltaP `8.3987` edge `0.0158` maxDD `-2.3986`
- `market_context_high->fx_24h` score `-0.1519` n `111` status `ready` deltaP `10.8202` edge `0.0024` maxDD `-0.6418`
- `market_context_high->index_1h` score `-0.194` n `135` status `ready` deltaP `2.5538` edge `0.0075` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.2391` n `111` status `ready` deltaP `6.9679` edge `0.0317` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `-0.2598` n `135` status `ready` deltaP `1.9783` edge `0.0231` maxDD `-1.9684`
- `market_context_high->crypto_major_1h` score `-0.3398` n `135` status `ready` deltaP `4.3657` edge `0.0579` maxDD `-5.1125`
- `market_context_high->commodity_1h` score `-0.3651` n `135` status `ready` deltaP `3.0495` edge `0.0082` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.4511` n `126` status `ready` deltaP `2.2019` edge `0.0131` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.5023` n `111` status `ready` deltaP `7.9627` edge `0.1919` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5423` n `135` status `ready` deltaP `-0.693` edge `0.0038` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7826` n `135` status `ready` deltaP `-1.9938` edge `-0.0047` maxDD `-2.9203`
- `market_context_high->metal_4h` score `-1.1952` n `126` status `ready` deltaP `-0.3412` edge `-0.0078` maxDD `-5.7863`
- `market_context_high->commodity_4h` score `-1.2196` n `126` status `ready` deltaP `3.8788` edge `0.0098` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3208` n `135` status `ready` deltaP `-5.357` edge `0.0095` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
