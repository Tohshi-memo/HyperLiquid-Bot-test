# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T06:37:23.468988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `0.0163` n `8`; equity avg `0.0057` n `96`; fx avg `-0.0051` n `6`; index avg `0.0119` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0045` n `770`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.1158` n `230`; crypto_major avg `0.1442` n `8`; equity avg `0.0127` n `96`; fx avg `0.0038` n `6`; index avg `0.0158` n `25`; metal avg `0.0119` n `20`; unknown avg `0.0158` n `752`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.205` n `230`; crypto_major avg `-0.2602` n `8`; equity avg `0.1132` n `96`; fx avg `0.01` n `6`; index avg `0.0104` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.0086` n `752`
- 24h: commodity avg `0.2776` n `12`; crypto_alt avg `0.2823` n `230`; crypto_major avg `1.081` n `8`; equity avg `0.107` n `96`; fx avg `-0.0026` n `6`; index avg `-0.0262` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0016` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
