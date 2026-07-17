# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T13:22:28.151310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.068` n `12`; crypto_alt avg `0.1912` n `230`; crypto_major avg `0.2046` n `8`; equity avg `-0.0944` n `96`; fx avg `0.0013` n `6`; index avg `-0.0252` n `25`; metal avg `-0.0364` n `20`; unknown avg `0.0727` n `769`
- 1h: commodity avg `0.3245` n `12`; crypto_alt avg `-0.7144` n `230`; crypto_major avg `-0.6381` n `8`; equity avg `-0.6218` n `96`; fx avg `0.0108` n `6`; index avg `-0.0985` n `25`; metal avg `-0.0979` n `20`; unknown avg `0.0592` n `769`
- 4h: commodity avg `0.3636` n `12`; crypto_alt avg `-0.6684` n `230`; crypto_major avg `-0.5423` n `8`; equity avg `-0.049` n `96`; fx avg `-0.0209` n `6`; index avg `-0.0237` n `25`; metal avg `-0.2955` n `20`; unknown avg `0.1751` n `769`
- 24h: commodity avg `0.112` n `12`; crypto_alt avg `-2.5327` n `230`; crypto_major avg `-3.3363` n `8`; equity avg `-5.0824` n `94`; fx avg `-0.0392` n `6`; index avg `-0.6912` n `25`; metal avg `-0.7168` n `20`; unknown avg `-0.4093` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
