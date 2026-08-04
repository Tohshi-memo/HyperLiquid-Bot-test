# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T11:37:24.218148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0811` n `12`; crypto_alt avg `-0.0889` n `230`; crypto_major avg `-0.1404` n `8`; equity avg `-0.0807` n `107`; fx avg `-0.022` n `6`; index avg `-0.0013` n `25`; metal avg `0.1525` n `20`; unknown avg `0.0368` n `781`
- 1h: commodity avg `-0.4386` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `0.3856` n `8`; equity avg `0.4596` n `107`; fx avg `-0.0438` n `6`; index avg `0.0999` n `25`; metal avg `0.2806` n `20`; unknown avg `0.1175` n `781`
- 4h: commodity avg `-0.358` n `12`; crypto_alt avg `-0.1291` n `230`; crypto_major avg `0.1844` n `8`; equity avg `0.6662` n `107`; fx avg `-0.0296` n `6`; index avg `0.0923` n `25`; metal avg `0.2372` n `20`; unknown avg `0.2415` n `781`
- 24h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.8265` n `230`; crypto_major avg `1.2691` n `8`; equity avg `4.8491` n `107`; fx avg `0.0441` n `6`; index avg `0.5411` n `25`; metal avg `0.5646` n `20`; unknown avg `0.8771` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
