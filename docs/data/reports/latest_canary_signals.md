# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T06:52:28.896392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.0158` n `229`; crypto_major avg `0.0462` n `8`; equity avg `0.0491` n `88`; fx avg `0.0171` n `6`; index avg `0.015` n `25`; metal avg `-0.0697` n `20`; unknown avg `-0.0556` n `765`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.0178` n `229`; crypto_major avg `-0.0428` n `8`; equity avg `0.0935` n `88`; fx avg `0.0279` n `6`; index avg `0.0627` n `25`; metal avg `-0.0552` n `20`; unknown avg `-0.0608` n `731`
- 4h: commodity avg `0.1727` n `12`; crypto_alt avg `-0.9212` n `229`; crypto_major avg `-0.7241` n `8`; equity avg `0.7393` n `88`; fx avg `0.0151` n `6`; index avg `0.188` n `25`; metal avg `-0.1853` n `20`; unknown avg `-0.1554` n `731`
- 24h: commodity avg `-0.0648` n `12`; crypto_alt avg `-0.1386` n `229`; crypto_major avg `0.8628` n `8`; equity avg `-0.5884` n `88`; fx avg `0.086` n `6`; index avg `-0.0193` n `25`; metal avg `-0.3036` n `20`; unknown avg `0.9736` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
