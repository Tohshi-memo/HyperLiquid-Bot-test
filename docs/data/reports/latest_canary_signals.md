# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T20:22:23.592707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `0.193` n `230`; crypto_major avg `0.2873` n `8`; equity avg `0.0058` n `96`; fx avg `0.0123` n `6`; index avg `-0.0039` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0858` n `770`
- 1h: commodity avg `-0.0928` n `12`; crypto_alt avg `0.2141` n `230`; crypto_major avg `0.245` n `8`; equity avg `-0.0378` n `96`; fx avg `0.0162` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0928` n `770`
- 4h: commodity avg `0.1549` n `12`; crypto_alt avg `0.4752` n `230`; crypto_major avg `0.7423` n `8`; equity avg `0.0297` n `96`; fx avg `-0.0181` n `6`; index avg `-0.0263` n `25`; metal avg `-0.0246` n `20`; unknown avg `0.391` n `770`
- 24h: commodity avg `0.3573` n `12`; crypto_alt avg `-0.2777` n `230`; crypto_major avg `0.5967` n `8`; equity avg `-0.2248` n `96`; fx avg `-0.1042` n `6`; index avg `0.0341` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.0092` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
