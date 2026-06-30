# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T06:22:26.110353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `-0.0051` n `228`; crypto_major avg `-0.1054` n `8`; equity avg `-0.1117` n `88`; fx avg `0.0189` n `6`; index avg `-0.0248` n `23`; metal avg `0.17` n `20`; unknown avg `-0.2972` n `765`
- 1h: commodity avg `-0.0814` n `12`; crypto_alt avg `0.0472` n `228`; crypto_major avg `-0.0328` n `8`; equity avg `-0.2371` n `88`; fx avg `0.0422` n `6`; index avg `-0.0762` n `23`; metal avg `0.2061` n `20`; unknown avg `-0.5673` n `737`
- 4h: commodity avg `-0.1253` n `12`; crypto_alt avg `0.1504` n `228`; crypto_major avg `-0.2802` n `8`; equity avg `0.2817` n `88`; fx avg `0.0035` n `6`; index avg `0.0961` n `23`; metal avg `0.4013` n `20`; unknown avg `7.8301` n `737`
- 24h: commodity avg `-0.3281` n `12`; crypto_alt avg `-0.4699` n `228`; crypto_major avg `0.2487` n `8`; equity avg `1.815` n `88`; fx avg `0.1401` n `6`; index avg `0.2055` n `23`; metal avg `-0.5171` n `20`; unknown avg `9.1641` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
