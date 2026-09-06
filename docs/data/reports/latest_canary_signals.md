# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T10:22:26.003692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.082` n `232`; crypto_major avg `-0.0153` n `8`; equity avg `0.0153` n `134`; fx avg `0.0125` n `6`; index avg `0.0008` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.6003` n `794`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `0.0852` n `232`; crypto_major avg `-0.0097` n `8`; equity avg `0.077` n `134`; fx avg `0.0259` n `6`; index avg `0.0209` n `26`; metal avg `-0.0209` n `20`; unknown avg `1.1655` n `792`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.2677` n `232`; crypto_major avg `-0.0384` n `8`; equity avg `0.0935` n `134`; fx avg `0.0172` n `6`; index avg `0.0155` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.2036` n `782`
- 24h: commodity avg `0.1744` n `12`; crypto_alt avg `1.9239` n `232`; crypto_major avg `2.1036` n `8`; equity avg `0.5019` n `134`; fx avg `-0.011` n `6`; index avg `0.0866` n `26`; metal avg `0.0134` n `20`; unknown avg `493.3365` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
