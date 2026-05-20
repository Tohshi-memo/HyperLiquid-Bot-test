# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T03:22:19.299231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0536` n `12`; crypto_alt avg `0.2302` n `228`; crypto_major avg `0.2015` n `8`; equity avg `0.0128` n `66`; fx avg `0.0135` n `6`; index avg `0.0003` n `23`; metal avg `0.194` n `18`; unknown avg `8.5984` n `384`
- 1h: commodity avg `0.1109` n `12`; crypto_alt avg `-0.1923` n `228`; crypto_major avg `-0.0733` n `8`; equity avg `-0.4748` n `66`; fx avg `0.04` n `6`; index avg `-0.335` n `23`; metal avg `-0.4396` n `18`; unknown avg `8.3721` n `384`
- 4h: commodity avg `-0.264` n `12`; crypto_alt avg `0.0685` n `228`; crypto_major avg `-0.3367` n `8`; equity avg `-0.365` n `66`; fx avg `-0.0324` n `6`; index avg `-0.3909` n `23`; metal avg `-0.5675` n `18`; unknown avg `-0.6316` n `383`
- 24h: commodity avg `0.626` n `12`; crypto_alt avg `-0.8625` n `228`; crypto_major avg `-0.6229` n `8`; equity avg `-0.0536` n `66`; fx avg `-0.1381` n `6`; index avg `-0.6999` n `23`; metal avg `-2.3157` n `18`; unknown avg `0.9666` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
