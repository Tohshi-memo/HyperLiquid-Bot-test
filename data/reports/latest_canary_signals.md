# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T12:37:25.073418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0928` n `12`; crypto_alt avg `0.1484` n `230`; crypto_major avg `0.2046` n `8`; equity avg `0.627` n `120`; fx avg `-0.0435` n `6`; index avg `0.0826` n `25`; metal avg `0.1991` n `20`; unknown avg `0.0009` n `792`
- 1h: commodity avg `-0.0817` n `12`; crypto_alt avg `0.2095` n `230`; crypto_major avg `0.1974` n `8`; equity avg `0.7509` n `120`; fx avg `-0.0625` n `6`; index avg `0.1236` n `25`; metal avg `0.2522` n `20`; unknown avg `-0.0083` n `792`
- 4h: commodity avg `0.0794` n `12`; crypto_alt avg `0.2773` n `230`; crypto_major avg `0.342` n `8`; equity avg `0.0224` n `120`; fx avg `-0.0922` n `6`; index avg `0.0334` n `25`; metal avg `0.3196` n `20`; unknown avg `0.0665` n `789`
- 24h: commodity avg `0.2971` n `12`; crypto_alt avg `0.5335` n `230`; crypto_major avg `0.6916` n `8`; equity avg `-1.166` n `120`; fx avg `-0.2645` n `6`; index avg `-0.0992` n `25`; metal avg `-0.1558` n `20`; unknown avg `-0.0521` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
