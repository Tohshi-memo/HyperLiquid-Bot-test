# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T03:37:26.623256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0658` n `12`; crypto_alt avg `-0.0073` n `230`; crypto_major avg `-0.0421` n `8`; equity avg `0.0253` n `102`; fx avg `-0.0051` n `6`; index avg `-0.0198` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.0037` n `774`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `-0.0057` n `230`; crypto_major avg `0.0312` n `8`; equity avg `0.1606` n `102`; fx avg `-0.0116` n `6`; index avg `0.0218` n `25`; metal avg `0.0419` n `20`; unknown avg `-0.0744` n `774`
- 4h: commodity avg `-0.1518` n `12`; crypto_alt avg `-0.2792` n `230`; crypto_major avg `-0.5571` n `8`; equity avg `-1.3693` n `102`; fx avg `-0.0105` n `6`; index avg `-0.3133` n `25`; metal avg `-0.2656` n `20`; unknown avg `0.3601` n `774`
- 24h: commodity avg `-0.8078` n `12`; crypto_alt avg `-3.8488` n `230`; crypto_major avg `-3.2491` n `8`; equity avg `-3.1611` n `102`; fx avg `-0.1381` n `6`; index avg `-0.6851` n `25`; metal avg `-0.2439` n `20`; unknown avg `1161.8644` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
