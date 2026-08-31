# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T14:07:34.956396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1484` n `12`; crypto_alt avg `0.1601` n `232`; crypto_major avg `0.1555` n `8`; equity avg `-0.0683` n `128`; fx avg `-0.0147` n `6`; index avg `-0.0112` n `26`; metal avg `0.0247` n `20`; unknown avg `-0.0681` n `792`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `-0.158` n `232`; crypto_major avg `-0.2837` n `8`; equity avg `0.2773` n `128`; fx avg `-0.0077` n `6`; index avg `-0.0164` n `26`; metal avg `-0.1` n `20`; unknown avg `-0.1006` n `792`
- 4h: commodity avg `-0.1512` n `12`; crypto_alt avg `-0.3371` n `232`; crypto_major avg `-0.2589` n `8`; equity avg `-0.0235` n `128`; fx avg `-0.0007` n `6`; index avg `-0.0563` n `26`; metal avg `-0.2197` n `20`; unknown avg `-0.4061` n `792`
- 24h: commodity avg `0.4902` n `12`; crypto_alt avg `-1.7786` n `231`; crypto_major avg `-2.372` n `8`; equity avg `-0.5926` n `128`; fx avg `-0.1104` n `6`; index avg `-0.1653` n `26`; metal avg `-0.4827` n `20`; unknown avg `-0.0905` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
