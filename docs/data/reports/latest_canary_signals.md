# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T23:22:28.266245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0421` n `12`; crypto_alt avg `0.072` n `228`; crypto_major avg `-0.0264` n `8`; equity avg `0.0336` n `78`; fx avg `0.0072` n `6`; index avg `0.0068` n `23`; metal avg `-0.0119` n `18`; unknown avg `-0.1308` n `687`
- 1h: commodity avg `-0.2149` n `12`; crypto_alt avg `-0.0721` n `228`; crypto_major avg `-0.0679` n `8`; equity avg `0.1389` n `78`; fx avg `-0.0102` n `6`; index avg `0.015` n `23`; metal avg `0.0011` n `18`; unknown avg `-0.2427` n `687`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `0.1838` n `228`; crypto_major avg `0.0079` n `8`; equity avg `0.1261` n `78`; fx avg `-0.0156` n `6`; index avg `-0.0109` n `23`; metal avg `0.1313` n `18`; unknown avg `-0.7048` n `687`
- 24h: commodity avg `0.2745` n `12`; crypto_alt avg `-3.6925` n `228`; crypto_major avg `-4.5692` n `8`; equity avg `0.8267` n `78`; fx avg `-0.1153` n `6`; index avg `0.221` n `23`; metal avg `-4.1107` n `18`; unknown avg `-0.7279` n `572`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
