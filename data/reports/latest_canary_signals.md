# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T01:22:26.156984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `-0.3474` n `232`; crypto_major avg `-0.303` n `8`; equity avg `-0.0601` n `134`; fx avg `0.0236` n `6`; index avg `0.0137` n `26`; metal avg `-0.0715` n `20`; unknown avg `0.6589` n `794`
- 1h: commodity avg `0.0307` n `12`; crypto_alt avg `-0.9575` n `232`; crypto_major avg `-0.5735` n `8`; equity avg `-0.0976` n `134`; fx avg `-0.0716` n `6`; index avg `-0.0002` n `26`; metal avg `-0.1395` n `20`; unknown avg `0.8517` n `784`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.5127` n `232`; crypto_major avg `-0.5099` n `8`; equity avg `0.0096` n `134`; fx avg `-0.109` n `6`; index avg `-0.0088` n `26`; metal avg `-0.2217` n `20`; unknown avg `0.5622` n `783`
- 24h: commodity avg `-0.0207` n `12`; crypto_alt avg `0.1171` n `232`; crypto_major avg `0.0525` n `8`; equity avg `0.2301` n `134`; fx avg `-0.1109` n `6`; index avg `0.0089` n `26`; metal avg `-0.2218` n `20`; unknown avg `150.7628` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
