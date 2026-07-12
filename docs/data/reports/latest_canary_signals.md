# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T19:07:24.010227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.085` n `12`; crypto_alt avg `0.047` n `230`; crypto_major avg `0.0153` n `8`; equity avg `0.0296` n `92`; fx avg `0.0267` n `6`; index avg `0.0037` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0507` n `765`
- 1h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.1157` n `230`; crypto_major avg `0.2045` n `8`; equity avg `0.0673` n `92`; fx avg `0.0179` n `6`; index avg `0.0013` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0769` n `765`
- 4h: commodity avg `0.1083` n `12`; crypto_alt avg `-0.2282` n `230`; crypto_major avg `0.0225` n `8`; equity avg `-0.0004` n `92`; fx avg `0.0026` n `6`; index avg `0.0033` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.188` n `759`
- 24h: commodity avg `0.511` n `12`; crypto_alt avg `-1.3899` n `230`; crypto_major avg `-0.5306` n `8`; equity avg `-0.1865` n `92`; fx avg `0.0269` n `6`; index avg `-0.095` n `25`; metal avg `-0.1062` n `20`; unknown avg `0.1605` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
