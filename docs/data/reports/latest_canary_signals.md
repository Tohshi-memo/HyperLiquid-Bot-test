# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:07:34.867128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.1879` n `230`; crypto_major avg `0.1659` n `8`; equity avg `0.2554` n `120`; fx avg `0.0035` n `6`; index avg `0.0154` n `25`; metal avg `0.032` n `20`; unknown avg `0.1376` n `791`
- 1h: commodity avg `0.0335` n `12`; crypto_alt avg `0.3339` n `230`; crypto_major avg `0.2607` n `8`; equity avg `0.4348` n `120`; fx avg `-0.005` n `6`; index avg `0.0553` n `25`; metal avg `0.0734` n `20`; unknown avg `0.1324` n `791`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.2864` n `230`; crypto_major avg `0.3401` n `8`; equity avg `0.4146` n `120`; fx avg `-0.0711` n `6`; index avg `0.0618` n `25`; metal avg `0.1548` n `20`; unknown avg `0.0765` n `789`
- 24h: commodity avg `0.4768` n `12`; crypto_alt avg `0.352` n `230`; crypto_major avg `0.3901` n `8`; equity avg `-1.7905` n `120`; fx avg `-0.1985` n `6`; index avg `-0.2213` n `25`; metal avg `-0.4095` n `20`; unknown avg `-0.1741` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
