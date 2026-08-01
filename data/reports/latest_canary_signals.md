# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T13:07:35.190276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `0.0477` n `230`; crypto_major avg `-0.0215` n `8`; equity avg `-0.0267` n `102`; fx avg `-0.003` n `6`; index avg `0.02` n `25`; metal avg `0.002` n `20`; unknown avg `0.016` n `782`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `0.0344` n `230`; crypto_major avg `0.0296` n `8`; equity avg `-0.0998` n `102`; fx avg `0.0104` n `6`; index avg `0.0173` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.0417` n `782`
- 4h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.0697` n `230`; crypto_major avg `-0.1762` n `8`; equity avg `-0.1279` n `102`; fx avg `-0.0609` n `6`; index avg `0.001` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0781` n `781`
- 24h: commodity avg `0.378` n `12`; crypto_alt avg `0.2252` n `230`; crypto_major avg `-1.4498` n `8`; equity avg `-2.3704` n `102`; fx avg `-0.1561` n `6`; index avg `-0.2262` n `25`; metal avg `0.0554` n `20`; unknown avg `4.4287` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
