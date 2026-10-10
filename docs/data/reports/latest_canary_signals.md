# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T08:22:31.244331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `-0.2041` n `235`; crypto_major avg `-0.0873` n `8`; equity avg `-0.0251` n `150`; fx avg `0.0197` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.2843` n `1117`
- 1h: commodity avg `-0.0096` n `13`; crypto_alt avg `-0.1547` n `235`; crypto_major avg `0.0838` n `8`; equity avg `-0.0483` n `150`; fx avg `0.0411` n `6`; index avg `-0.017` n `26`; metal avg `0.0013` n `20`; unknown avg `0.4816` n `1099`
- 4h: commodity avg `0.013` n `13`; crypto_alt avg `-0.1137` n `235`; crypto_major avg `0.1949` n `8`; equity avg `-0.1076` n `150`; fx avg `0.0356` n `6`; index avg `-0.0296` n `26`; metal avg `-0.0039` n `20`; unknown avg `1.6605` n `1082`
- 24h: commodity avg `0.1511` n `13`; crypto_alt avg `1.1583` n `235`; crypto_major avg `-0.0376` n `8`; equity avg `-0.3621` n `150`; fx avg `-0.0321` n `6`; index avg `-0.0574` n `26`; metal avg `-0.0576` n `20`; unknown avg `631.996` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
