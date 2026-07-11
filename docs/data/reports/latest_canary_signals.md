# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T14:22:29.674268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `0.067` n `230`; crypto_major avg `0.0503` n `8`; equity avg `0.0023` n `92`; fx avg `-0.0101` n `6`; index avg `0.0008` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0062` n `765`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.1496` n `230`; crypto_major avg `0.1777` n `8`; equity avg `-0.0348` n `92`; fx avg `0.0012` n `6`; index avg `0.0` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0263` n `765`
- 4h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.5108` n `230`; crypto_major avg `0.4546` n `8`; equity avg `-0.1073` n `92`; fx avg `-0.0017` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0171` n `20`; unknown avg `-0.1409` n `765`
- 24h: commodity avg `0.0807` n `12`; crypto_alt avg `1.1231` n `229`; crypto_major avg `0.6918` n `8`; equity avg `0.3765` n `92`; fx avg `-0.0347` n `6`; index avg `0.1171` n `25`; metal avg `0.0387` n `20`; unknown avg `3.0449` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
