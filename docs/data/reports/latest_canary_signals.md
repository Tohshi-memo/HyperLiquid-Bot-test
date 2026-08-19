# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T10:52:30.276542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.04` n `230`; crypto_major avg `0.0603` n `8`; equity avg `-0.0238` n `120`; fx avg `-0.005` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.1109` n `791`
- 1h: commodity avg `0.0536` n `12`; crypto_alt avg `0.1416` n `230`; crypto_major avg `0.0923` n `8`; equity avg `-0.0217` n `120`; fx avg `0.009` n `6`; index avg `0.0045` n `25`; metal avg `0.0611` n `20`; unknown avg `-0.0104` n `791`
- 4h: commodity avg `0.1016` n `12`; crypto_alt avg `0.0899` n `230`; crypto_major avg `0.163` n `8`; equity avg `0.3562` n `120`; fx avg `-0.0804` n `6`; index avg `0.0583` n `25`; metal avg `0.1066` n `20`; unknown avg `-0.0968` n `789`
- 24h: commodity avg `0.5066` n `12`; crypto_alt avg `0.2984` n `230`; crypto_major avg `0.3243` n `8`; equity avg `-1.8171` n `120`; fx avg `-0.2125` n `6`; index avg `-0.2121` n `25`; metal avg `-0.4504` n `20`; unknown avg `-0.3509` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
