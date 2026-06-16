# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T17:22:45.540384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.1176` n `228`; crypto_major avg `-0.1371` n `8`; equity avg `-0.1537` n `77`; fx avg `0.0102` n `6`; index avg `-0.0632` n `23`; metal avg `-0.2044` n `18`; unknown avg `0.124` n `687`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1005` n `228`; crypto_major avg `-0.1837` n `8`; equity avg `-0.3463` n `77`; fx avg `0.0081` n `6`; index avg `-0.2267` n `23`; metal avg `-0.3016` n `18`; unknown avg `0.1214` n `687`
- 4h: commodity avg `-0.1263` n `12`; crypto_alt avg `-0.7142` n `228`; crypto_major avg `-1.3361` n `8`; equity avg `-0.9579` n `77`; fx avg `0.0717` n `6`; index avg `-0.7035` n `23`; metal avg `-0.2719` n `18`; unknown avg `0.8923` n `687`
- 24h: commodity avg `-0.938` n `12`; crypto_alt avg `-1.7997` n `228`; crypto_major avg `-1.3632` n `8`; equity avg `-1.0975` n `77`; fx avg `-0.0033` n `6`; index avg `-0.8136` n `23`; metal avg `0.2331` n `18`; unknown avg `0.4787` n `623`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
