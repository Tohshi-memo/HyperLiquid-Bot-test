# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T08:52:21.090166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1171` n `12`; crypto_alt avg `-0.0703` n `228`; crypto_major avg `-0.1312` n `8`; equity avg `-0.0444` n `66`; fx avg `-0.0194` n `6`; index avg `-0.0751` n `23`; metal avg `0.0536` n `18`; unknown avg `0.0354` n `386`
- 1h: commodity avg `-0.2821` n `12`; crypto_alt avg `0.1192` n `228`; crypto_major avg `0.1165` n `8`; equity avg `0.2875` n `66`; fx avg `0.0188` n `6`; index avg `0.0632` n `23`; metal avg `0.3677` n `18`; unknown avg `0.2793` n `386`
- 4h: commodity avg `-0.0931` n `12`; crypto_alt avg `0.0784` n `228`; crypto_major avg `0.3077` n `8`; equity avg `-0.0981` n `66`; fx avg `-0.0102` n `6`; index avg `-0.1077` n `23`; metal avg `-0.1711` n `18`; unknown avg `0.8387` n `374`
- 24h: commodity avg `-1.5837` n `12`; crypto_alt avg `2.7077` n `228`; crypto_major avg `3.3388` n `8`; equity avg `1.6097` n `66`; fx avg `0.0929` n `6`; index avg `1.2001` n `23`; metal avg `0.2018` n `18`; unknown avg `5.5392` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
