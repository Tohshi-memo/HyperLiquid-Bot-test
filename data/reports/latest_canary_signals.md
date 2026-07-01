# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T00:37:26.058038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.062` n `228`; crypto_major avg `0.1061` n `8`; equity avg `0.0261` n `88`; fx avg `0.0158` n `6`; index avg `0.0252` n `23`; metal avg `0.0386` n `20`; unknown avg `-0.0592` n `765`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `0.1237` n `228`; crypto_major avg `-0.0431` n `8`; equity avg `-0.1892` n `88`; fx avg `0.0483` n `6`; index avg `-0.0282` n `23`; metal avg `-0.081` n `20`; unknown avg `-0.2531` n `765`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.0308` n `228`; crypto_major avg `-0.1886` n `8`; equity avg `-0.001` n `88`; fx avg `0.0355` n `6`; index avg `-0.0094` n `23`; metal avg `-0.1492` n `20`; unknown avg `-0.8257` n `765`
- 24h: commodity avg `0.1645` n `12`; crypto_alt avg `-1.3942` n `228`; crypto_major avg `-1.2947` n `8`; equity avg `1.622` n `88`; fx avg `0.1006` n `6`; index avg `0.3719` n `23`; metal avg `0.0299` n `20`; unknown avg `7.3145` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
