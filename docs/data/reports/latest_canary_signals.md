# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T15:52:24.784298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.0075` n `232`; crypto_major avg `0.0206` n `8`; equity avg `-0.0004` n `134`; fx avg `-0.0055` n `6`; index avg `0.0059` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.1894` n `794`
- 1h: commodity avg `0.0191` n `12`; crypto_alt avg `-0.1246` n `232`; crypto_major avg `0.0245` n `8`; equity avg `0.0376` n `134`; fx avg `-0.0047` n `6`; index avg `0.0055` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.1911` n `792`
- 4h: commodity avg `0.0471` n `12`; crypto_alt avg `0.0811` n `232`; crypto_major avg `0.8023` n `8`; equity avg `0.0398` n `134`; fx avg `0.0094` n `6`; index avg `0.0068` n `26`; metal avg `0.0055` n `20`; unknown avg `-0.2799` n `729`
- 24h: commodity avg `0.1009` n `12`; crypto_alt avg `2.3296` n `232`; crypto_major avg `1.8273` n `8`; equity avg `0.5376` n `134`; fx avg `-0.0107` n `6`; index avg `0.0407` n `26`; metal avg `-0.0442` n `20`; unknown avg `0.2216` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
