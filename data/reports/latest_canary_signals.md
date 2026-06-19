# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T22:07:31.050081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `-0.0592` n `228`; crypto_major avg `-0.0516` n `8`; equity avg `-0.0012` n `78`; fx avg `0.031` n `6`; index avg `0.004` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.1724` n `687`
- 1h: commodity avg `0.2011` n `12`; crypto_alt avg `-0.3732` n `228`; crypto_major avg `-0.4012` n `8`; equity avg `-0.0573` n `78`; fx avg `-0.0033` n `6`; index avg `0.0045` n `23`; metal avg `-0.0125` n `18`; unknown avg `101.6487` n `687`
- 4h: commodity avg `0.2283` n `12`; crypto_alt avg `-0.7042` n `228`; crypto_major avg `-0.3966` n `8`; equity avg `-0.0741` n `78`; fx avg `-0.0307` n `6`; index avg `-0.017` n `23`; metal avg `0.147` n `18`; unknown avg `-0.3679` n `687`
- 24h: commodity avg `0.5039` n `12`; crypto_alt avg `-3.9817` n `228`; crypto_major avg `-4.8764` n `8`; equity avg `0.6479` n `78`; fx avg `-0.1362` n `6`; index avg `0.2102` n `23`; metal avg `-4.1136` n `18`; unknown avg `-0.635` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
