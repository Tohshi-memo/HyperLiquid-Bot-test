# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T18:37:26.665686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4093`

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

- `news_risk_high->equity_4h` score `2.4247` n `96` status `ready` deltaP `16.8191` edge `0.2893` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0634` n `96` status `ready` deltaP `16.1839` edge `0.0285` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.7228` n `96` status `ready` deltaP `6.5432` edge `0.104` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3579` n `96` status `ready` deltaP `12.3628` edge `0.0088` maxDD `-0.2931`
- `news_risk_high->equity_24h` score `0.2393` n `96` status `ready` deltaP `29.0728` edge `0.9955` maxDD `-86.0244`
- `news_risk_high->crypto_major_4h` score `-0.2358` n `96` status `ready` deltaP `3.1758` edge `0.1172` maxDD `-9.1553`
- `news_risk_high->metal_1h` score `-0.2436` n `96` status `ready` deltaP `1.0354` edge `-0.0024` maxDD `-0.5256`
- `news_risk_high->index_24h` score `-0.253` n `96` status `ready` deltaP `2.5203` edge `0.1456` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.3038` n `96` status `ready` deltaP `0.1248` edge `0.0002` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.5036` n `96` status `ready` deltaP `3.1375` edge `0.0373` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.6495` n `96` status `ready` deltaP `1.0162` edge `0.1736` maxDD `-14.0916`
- `news_risk_high->fx_4h` score `-0.65` n `96` status `ready` deltaP `-1.2195` edge `-0.0028` maxDD `-0.4593`
- `news_risk_high->crypto_major_1h` score `-0.7168` n `96` status `ready` deltaP `-1.7715` edge `0.0138` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-0.8056` n `96` status `ready` deltaP `1.9309` edge `-0.0256` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.4998` n `96` status `ready` deltaP `-11.3302` edge `0.0128` maxDD `-0.313`
- `news_risk_high->metal_24h` score `-2.821` n `96` status `ready` deltaP `4.8058` edge `-0.2041` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2544` n `96` status `ready` deltaP `-18.75` edge `-0.0136` maxDD `-2.9411`
- `news_risk_high->commodity_4h` score `-4.6878` n `96` status `ready` deltaP `-27.0071` edge `-0.0153` maxDD `-6.9573`
- `news_risk_high->crypto_major_24h` score `-6.1043` n `96` status `ready` deltaP `-14.5021` edge `0.1644` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.6106` n `96` status `ready` deltaP `-24.944` edge `-0.0121` maxDD `-32.4658`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
