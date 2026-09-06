# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T00:01:07.304653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.0422` n `232`; crypto_major avg `-0.0461` n `8`; equity avg `0.0097` n `134`; fx avg `-0.0053` n `6`; index avg `0.0006` n `26`; metal avg `0.002` n `20`; unknown avg `1.053` n `792`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `-0.0046` n `232`; crypto_major avg `0.002` n `8`; equity avg `0.0346` n `134`; fx avg `-0.0131` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.1035` n `792`
- 4h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.2579` n `232`; crypto_major avg `-0.3717` n `8`; equity avg `0.0454` n `134`; fx avg `-0.014` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.2592` n `770`
- 24h: commodity avg `0.1315` n `12`; crypto_alt avg `2.9238` n `232`; crypto_major avg `2.1687` n `8`; equity avg `0.3332` n `134`; fx avg `-0.0676` n `6`; index avg `0.065` n `26`; metal avg `0.0547` n `20`; unknown avg `1.9177` n `698`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
