# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T22:52:28.227708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0221` n `232`; crypto_major avg `-0.07` n `8`; equity avg `-0.0204` n `129`; fx avg `-0.0025` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0122` n `20`; unknown avg `0.1872` n `793`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `-0.3436` n `232`; crypto_major avg `-0.4557` n `8`; equity avg `-0.0563` n `129`; fx avg `0.0048` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.3851` n `791`
- 4h: commodity avg `0.062` n `12`; crypto_alt avg `-0.1029` n `232`; crypto_major avg `-0.3535` n `8`; equity avg `0.4974` n `129`; fx avg `0.0012` n `6`; index avg `0.0748` n `26`; metal avg `0.0785` n `20`; unknown avg `1.5058` n `773`
- 24h: commodity avg `0.3845` n `12`; crypto_alt avg `0.3229` n `231`; crypto_major avg `0.4058` n `8`; equity avg `0.3815` n `129`; fx avg `-0.0837` n `6`; index avg `-0.0563` n `26`; metal avg `-0.3213` n `20`; unknown avg `-0.0033` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
