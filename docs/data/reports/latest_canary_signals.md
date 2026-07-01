# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T12:07:33.359352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.1747` n `228`; crypto_major avg `-0.1749` n `8`; equity avg `-0.1306` n `88`; fx avg `-0.019` n `6`; index avg `-0.0344` n `23`; metal avg `-0.173` n `20`; unknown avg `0.2074` n `765`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.2164` n `228`; crypto_major avg `-0.2489` n `8`; equity avg `-0.2605` n `88`; fx avg `-0.0336` n `6`; index avg `-0.0365` n `23`; metal avg `0.119` n `20`; unknown avg `-0.0907` n `765`
- 4h: commodity avg `-0.1169` n `12`; crypto_alt avg `0.1179` n `228`; crypto_major avg `-0.8159` n `8`; equity avg `0.034` n `88`; fx avg `0.001` n `6`; index avg `0.0178` n `23`; metal avg `0.4427` n `20`; unknown avg `0.1439` n `765`
- 24h: commodity avg `-0.5538` n `12`; crypto_alt avg `0.655` n `228`; crypto_major avg `-0.5625` n `8`; equity avg `0.5176` n `88`; fx avg `0.1162` n `6`; index avg `-0.0192` n `23`; metal avg `-0.4716` n `20`; unknown avg `0.0535` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
