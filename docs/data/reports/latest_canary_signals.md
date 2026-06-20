# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T11:33:10.188302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0697` n `12`; crypto_alt avg `0.015` n `228`; crypto_major avg `0.0359` n `8`; equity avg `-0.0481` n `78`; fx avg `0.0` n `6`; index avg `-0.0007` n `23`; metal avg `0.0002` n `18`; unknown avg `0.184` n `687`
- 1h: commodity avg `-0.1295` n `12`; crypto_alt avg `-0.027` n `228`; crypto_major avg `0.0265` n `8`; equity avg `-0.0653` n `78`; fx avg `0.009` n `6`; index avg `0.0112` n `23`; metal avg `0.003` n `18`; unknown avg `-0.0891` n `687`
- 4h: commodity avg `-0.1623` n `12`; crypto_alt avg `-0.0037` n `228`; crypto_major avg `-0.0742` n `8`; equity avg `-0.1797` n `78`; fx avg `0.3242` n `6`; index avg `0.0038` n `23`; metal avg `-0.0184` n `18`; unknown avg `-0.3656` n `687`
- 24h: commodity avg `0.3756` n `12`; crypto_alt avg `-3.0972` n `228`; crypto_major avg `-3.3766` n `8`; equity avg `1.0932` n `78`; fx avg `-0.0719` n `6`; index avg `0.2926` n `23`; metal avg `-4.1007` n `18`; unknown avg `-0.1509` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
