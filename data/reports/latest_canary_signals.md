# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T18:54:32.386416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `12`; crypto_alt avg `-0.1176` n `228`; crypto_major avg `0.0144` n `8`; equity avg `-0.0255` n `67`; fx avg `0.0` n `6`; index avg `-0.0133` n `23`; metal avg `-0.0154` n `18`; unknown avg `-0.2213` n `396`
- 1h: commodity avg `0.0768` n `12`; crypto_alt avg `-0.23` n `228`; crypto_major avg `-0.1513` n `8`; equity avg `-0.0422` n `67`; fx avg `-0.0083` n `6`; index avg `-0.022` n `23`; metal avg `0.0049` n `18`; unknown avg `-0.277` n `396`
- 4h: commodity avg `0.1001` n `12`; crypto_alt avg `0.2126` n `228`; crypto_major avg `0.1115` n `8`; equity avg `0.0416` n `67`; fx avg `0.0054` n `6`; index avg `-0.0544` n `23`; metal avg `0.0391` n `18`; unknown avg `-0.6054` n `396`
- 24h: commodity avg `-0.519` n `12`; crypto_alt avg `-0.586` n `228`; crypto_major avg `1.4352` n `8`; equity avg `1.1396` n `67`; fx avg `0.0809` n `6`; index avg `0.3247` n `23`; metal avg `0.4511` n `18`; unknown avg `0.3183` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
