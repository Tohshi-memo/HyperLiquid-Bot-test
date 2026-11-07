# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T01:07:23.702746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.9082` n `70` status `ready` deltaP `7.0863` edge `0.1556` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6164` n `70` status `ready` deltaP `11.8859` edge `0.0199` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2554` n `70` status `ready` deltaP `8.1696` edge `0.1451` maxDD `-6.6786`
- `news_risk_high->index_1h` score `-0.0267` n `70` status `ready` deltaP `6.0008` edge `0.0031` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1048` n `70` status `ready` deltaP `-0.5988` edge `0.0455` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.1061` n `70` status `ready` deltaP `4.1681` edge `0.0032` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.2002` n `70` status `ready` deltaP `-3.3036` edge `0.0496` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.283` n `70` status `ready` deltaP `0.0941` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.5356` n `70` status `ready` deltaP `-3.905` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2721` n `70` status `ready` deltaP `-4.8214` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-2.2417` n `70` status `ready` deltaP `-8.734` edge `-0.0347` maxDD `-4.1772`
- `news_risk_high->commodity_1h` score `-2.3858` n `70` status `ready` deltaP `-15.7827` edge `-0.0054` maxDD `-1.389`
- `news_risk_high->crypto_major_4h` score `-2.6456` n `70` status `ready` deltaP `-6.9512` edge `-0.0137` maxDD `-8.5004`
- `news_risk_high->crypto_alt_1h` score `-2.6651` n `70` status `ready` deltaP `-6.7066` edge `-0.0546` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-2.9479` n `70` status `ready` deltaP `-8.4756` edge `-0.0594` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.4221` n `70` status `ready` deltaP `-1.3393` edge `-0.2402` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.5144` n `70` status `ready` deltaP `22.3908` edge `0.5588` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.4607` n `70` status `ready` deltaP `-30.514` edge `-0.0085` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.0683` n `70` status `ready` deltaP `-27.8869` edge `-0.0852` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.3216` n `70` status `ready` deltaP `-29.251` edge `-0.0648` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
