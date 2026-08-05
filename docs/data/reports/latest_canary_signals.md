# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T23:36:02.975507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0214` n `230`; crypto_major avg `0.0122` n `8`; equity avg `-0.0806` n `108`; fx avg `0.0016` n `6`; index avg `-0.0088` n `25`; metal avg `0.0487` n `20`; unknown avg `0.2718` n `782`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0925` n `230`; crypto_major avg `0.0119` n `8`; equity avg `-0.1793` n `108`; fx avg `0.001` n `6`; index avg `-0.042` n `25`; metal avg `0.0674` n `20`; unknown avg `0.3266` n `782`
- 4h: commodity avg `-0.044` n `12`; crypto_alt avg `-0.0946` n `230`; crypto_major avg `-0.5355` n `8`; equity avg `-0.9085` n `108`; fx avg `0.0203` n `6`; index avg `-0.0846` n `25`; metal avg `0.0881` n `20`; unknown avg `0.3363` n `782`
- 24h: commodity avg `-0.0191` n `12`; crypto_alt avg `0.5924` n `230`; crypto_major avg `0.7294` n `8`; equity avg `-0.9105` n `108`; fx avg `-0.043` n `6`; index avg `-0.1153` n `25`; metal avg `0.9546` n `20`; unknown avg `1.2832` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
