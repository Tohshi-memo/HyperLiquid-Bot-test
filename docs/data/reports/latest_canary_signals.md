# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T19:22:26.560685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.2281` n `232`; crypto_major avg `0.1615` n `8`; equity avg `0.0187` n `134`; fx avg `-0.0104` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.4288` n `796`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.1809` n `232`; crypto_major avg `0.0697` n `8`; equity avg `0.0006` n `134`; fx avg `-0.0081` n `6`; index avg `0.0109` n `26`; metal avg `0.0317` n `20`; unknown avg `0.0035` n `794`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `-0.2534` n `232`; crypto_major avg `-0.1318` n `8`; equity avg `0.1706` n `134`; fx avg `-0.0216` n `6`; index avg `0.0682` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.8704` n `768`
- 24h: commodity avg `0.1485` n `12`; crypto_alt avg `0.4051` n `232`; crypto_major avg `-0.7382` n `8`; equity avg `0.4169` n `134`; fx avg `-0.1314` n `6`; index avg `0.085` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.6949` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
