# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T01:08:00.619789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `0.0846` n `231`; crypto_major avg `0.1413` n `8`; equity avg `-0.0459` n `127`; fx avg `-0.0036` n `6`; index avg `-0.0251` n `26`; metal avg `0.0817` n `20`; unknown avg `-0.0821` n `792`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.6208` n `231`; crypto_major avg `0.3058` n `8`; equity avg `0.3003` n `127`; fx avg `-0.0294` n `6`; index avg `0.0442` n `26`; metal avg `0.0079` n `20`; unknown avg `-0.0334` n `792`
- 4h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.3951` n `231`; crypto_major avg `0.0953` n `8`; equity avg `-0.0858` n `127`; fx avg `-0.0248` n `6`; index avg `0.0284` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.1616` n `792`
- 24h: commodity avg `0.2633` n `12`; crypto_alt avg `1.9838` n `231`; crypto_major avg `2.8593` n `8`; equity avg `0.3525` n `127`; fx avg `0.0227` n `6`; index avg `0.0965` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.8409` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
