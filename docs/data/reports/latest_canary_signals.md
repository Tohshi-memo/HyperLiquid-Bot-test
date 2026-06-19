# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T22:52:26.106919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `0.0568` n `228`; crypto_major avg `0.0835` n `8`; equity avg `0.0951` n `78`; fx avg `0.0266` n `6`; index avg `0.0036` n `23`; metal avg `0.0368` n `18`; unknown avg `-0.0688` n `687`
- 1h: commodity avg `-0.1453` n `12`; crypto_alt avg `0.317` n `228`; crypto_major avg `0.4062` n `8`; equity avg `0.1588` n `78`; fx avg `0.0709` n `6`; index avg `0.0063` n `23`; metal avg `0.0442` n `18`; unknown avg `-0.4202` n `687`
- 4h: commodity avg `0.1244` n `12`; crypto_alt avg `-0.0625` n `228`; crypto_major avg `0.1235` n `8`; equity avg `0.1172` n `78`; fx avg `0.0021` n `6`; index avg `0.0028` n `23`; metal avg `0.1835` n `18`; unknown avg `-0.6629` n `687`
- 24h: commodity avg `0.4288` n `12`; crypto_alt avg `-3.6304` n `228`; crypto_major avg `-4.4438` n `8`; equity avg `0.8113` n `78`; fx avg `-0.0963` n `6`; index avg `0.2126` n `23`; metal avg `-4.074` n `18`; unknown avg `-0.7457` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
