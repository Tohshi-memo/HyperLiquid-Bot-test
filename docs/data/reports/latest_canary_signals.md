# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:52:29.993254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `-0.0071` n `230`; crypto_major avg `-0.0097` n `8`; equity avg `-0.1245` n `120`; fx avg `0.0034` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0299` n `20`; unknown avg `-0.0051` n `792`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `0.2132` n `230`; crypto_major avg `0.1858` n `8`; equity avg `-0.2851` n `120`; fx avg `0.0096` n `6`; index avg `-0.0312` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.1912` n `791`
- 4h: commodity avg `0.1388` n `12`; crypto_alt avg `0.2558` n `230`; crypto_major avg `0.326` n `8`; equity avg `-0.7415` n `120`; fx avg `-0.0588` n `6`; index avg `-0.0359` n `25`; metal avg `0.0907` n `20`; unknown avg `0.0896` n `789`
- 24h: commodity avg `0.3727` n `12`; crypto_alt avg `0.3451` n `230`; crypto_major avg `0.2745` n `8`; equity avg `-2.3466` n `120`; fx avg `-0.2016` n `6`; index avg `-0.2742` n `25`; metal avg `-0.4189` n `20`; unknown avg `-0.2503` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
