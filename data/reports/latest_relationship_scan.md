# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T06:52:26.340692+00:00`
- Price records: `672`
- Market context records: `4699`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9752`

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

- `market_context_high->unknown_1h` score `78.1894` n `143` status `ready` deltaP `13.4909` edge `6.4676` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2798` n `135` status `ready` deltaP `11.3742` edge `0.4852` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4509` n `135` status `ready` deltaP `12.882` edge `0.2107` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3461` n `143` status `ready` deltaP `1.8937` edge `0.0226` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7914` n `135` status `ready` deltaP `3.6168` edge `-0.0133` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9014` n `135` status `ready` deltaP `-0.8729` edge `-0.0015` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-1.1974` n `143` status `ready` deltaP `-1.7975` edge `0.0109` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2186` n `135` status `ready` deltaP `5.7035` edge `0.0165` maxDD `-9.1941`
- `market_context_high->fx_1h` score `-1.3078` n `143` status `ready` deltaP `-5.2982` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.3416` n `135` status `ready` deltaP `0.6324` edge `0.0007` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6856` n `143` status `ready` deltaP `-4.3424` edge `-0.0111` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8709` n `143` status `ready` deltaP `-5.1998` edge `-0.0766` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.326` n `143` status `ready` deltaP `-1.6478` edge `-0.0867` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.9372` n `143` status `ready` deltaP `-2.9972` edge `-0.1095` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.6239` n `135` status `ready` deltaP `15.1967` edge `0.0638` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7877` n `135` status `ready` deltaP `-13.044` edge `-0.016` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4047` n `135` status `ready` deltaP `-10.6366` edge `-0.092` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.5994` n `135` status `ready` deltaP `-3.1595` edge `-0.2157` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.0827` n `135` status `ready` deltaP `-0.0915` edge `-0.2785` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5549` n `135` status `ready` deltaP `-3.5953` edge `-0.3674` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
