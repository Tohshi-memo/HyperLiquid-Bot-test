# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T20:07:25.087749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.0679` n `230`; crypto_major avg `0.0716` n `8`; equity avg `-0.0037` n `92`; fx avg `-0.0007` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0373` n `765`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0688` n `230`; crypto_major avg `-0.0018` n `8`; equity avg `0.0253` n `92`; fx avg `0.003` n `6`; index avg `0.0116` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.1691` n `765`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `0.4885` n `230`; crypto_major avg `0.3277` n `8`; equity avg `0.2461` n `92`; fx avg `0.0231` n `6`; index avg `0.0094` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0364` n `765`
- 24h: commodity avg `0.0014` n `12`; crypto_alt avg `1.227` n `229`; crypto_major avg `0.9373` n `8`; equity avg `0.4052` n `92`; fx avg `0.0063` n `6`; index avg `0.0384` n `25`; metal avg `0.0065` n `20`; unknown avg `2.3929` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
