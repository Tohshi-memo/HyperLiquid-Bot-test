# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T00:52:28.624111+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `53.9478` n `78` status `ready` deltaP `-36.8189` edge `7.4302` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.5599` n `78` status `ready` deltaP `34.1212` edge `0.1874` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9527` n `106` status `ready` deltaP `10.9497` edge `0.0535` maxDD `-0.7687`
- `market_context_high->index_24h` score `0.3472` n `78` status `ready` deltaP `13.9423` edge `-0.0354` maxDD `-0.2895`
- `market_context_high->metal_4h` score `-0.112` n `106` status `ready` deltaP `16.915` edge `0.0136` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.3251` n `112` status `ready` deltaP `4.3039` edge `0.0012` maxDD `-1.7257`
- `market_context_high->fx_1h` score `-0.3692` n `112` status `ready` deltaP `-1.4917` edge `-0.0009` maxDD `-0.2527`
- `market_context_high->crypto_major_24h` score `-0.399` n `78` status `ready` deltaP `-1.8697` edge `0.1696` maxDD `-11.3294`
- `market_context_high->commodity_1h` score `-0.4387` n `112` status `ready` deltaP `-0.3101` edge `0.0097` maxDD `-0.8688`
- `market_context_high->index_1h` score `-0.6604` n `112` status `ready` deltaP `-4.6514` edge `-0.0015` maxDD `-0.5064`
- `market_context_high->fx_4h` score `-0.6916` n `106` status `ready` deltaP `0.9348` edge `-0.0034` maxDD `-0.504`
- `market_context_high->index_4h` score `-1.2605` n `106` status `ready` deltaP `-11.2517` edge `-0.0057` maxDD `-0.8045`
- `market_context_high->crypto_major_4h` score `-1.4273` n `106` status `ready` deltaP `1.5532` edge `-0.0085` maxDD `-4.6638`
- `market_context_high->crypto_alt_1h` score `-2.011` n `112` status `ready` deltaP `-6.3997` edge `-0.0197` maxDD `-4.7507`
- `market_context_high->crypto_major_1h` score `-2.0673` n `112` status `ready` deltaP `-6.9932` edge `-0.0246` maxDD `-4.0845`
- `market_context_high->equity_1h` score `-2.2559` n `112` status `ready` deltaP `-9.1264` edge `-0.0394` maxDD `-3.6868`
- `market_context_high->metal_24h` score `-2.6552` n `78` status `ready` deltaP `-16.1726` edge `0.0186` maxDD `-7.0954`
- `market_context_high->fx_24h` score `-2.7193` n `78` status `ready` deltaP `-23.9984` edge `-0.0279` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-3.7788` n `78` status `ready` deltaP `7.8525` edge `-0.1616` maxDD `-12.4517`
- `market_context_high->crypto_alt_4h` score `-5.6857` n `106` status `ready` deltaP `-8.062` edge `-0.0519` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
