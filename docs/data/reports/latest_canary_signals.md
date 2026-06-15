# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T18:22:37.027006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `-0.1268` n `228`; crypto_major avg `-0.005` n `8`; equity avg `0.0659` n `77`; fx avg `0.0019` n `6`; index avg `0.0589` n `23`; metal avg `0.1534` n `18`; unknown avg `-0.1326` n `687`
- 1h: commodity avg `0.1433` n `12`; crypto_alt avg `0.0884` n `228`; crypto_major avg `0.1079` n `8`; equity avg `0.0441` n `77`; fx avg `0.0035` n `6`; index avg `-0.037` n `23`; metal avg `0.0108` n `18`; unknown avg `0.4843` n `687`
- 4h: commodity avg `0.4948` n `12`; crypto_alt avg `-0.1195` n `228`; crypto_major avg `0.9505` n `8`; equity avg `1.0787` n `77`; fx avg `0.0013` n `6`; index avg `0.3069` n `23`; metal avg `-0.5471` n `18`; unknown avg `4.5472` n `687`
- 24h: commodity avg `-0.659` n `12`; crypto_alt avg `6.368` n `228`; crypto_major avg `7.7126` n `8`; equity avg `3.1987` n `76`; fx avg `0.0594` n `6`; index avg `1.3168` n `23`; metal avg `2.2191` n `18`; unknown avg `6.7647` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
