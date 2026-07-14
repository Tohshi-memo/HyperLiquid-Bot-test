# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T12:52:29.772770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.082` n `12`; crypto_alt avg `0.1379` n `230`; crypto_major avg `0.3058` n `8`; equity avg `0.1115` n `92`; fx avg `-0.0031` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0594` n `20`; unknown avg `-0.0428` n `766`
- 1h: commodity avg `0.1454` n `12`; crypto_alt avg `1.0384` n `230`; crypto_major avg `1.3707` n `8`; equity avg `0.8124` n `92`; fx avg `-0.0177` n `6`; index avg `0.1404` n `25`; metal avg `0.3336` n `20`; unknown avg `0.4432` n `766`
- 4h: commodity avg `-0.0042` n `12`; crypto_alt avg `1.0831` n `230`; crypto_major avg `1.6622` n `8`; equity avg `0.6494` n `92`; fx avg `-0.0044` n `6`; index avg `0.2082` n `25`; metal avg `0.3176` n `20`; unknown avg `0.6827` n `766`
- 24h: commodity avg `1.3037` n `12`; crypto_alt avg `0.5018` n `230`; crypto_major avg `1.5766` n `8`; equity avg `0.2237` n `92`; fx avg `-0.0212` n `6`; index avg `0.1189` n `25`; metal avg `0.1638` n `20`; unknown avg `-0.1953` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
