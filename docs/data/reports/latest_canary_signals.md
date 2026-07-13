# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T03:52:29.598410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.1023` n `230`; crypto_major avg `0.0799` n `8`; equity avg `0.1182` n `92`; fx avg `0.0015` n `6`; index avg `-0.0136` n `25`; metal avg `0.0269` n `20`; unknown avg `0.0249` n `766`
- 1h: commodity avg `-0.0513` n `12`; crypto_alt avg `-1.0698` n `230`; crypto_major avg `-0.9892` n `8`; equity avg `-0.6908` n `92`; fx avg `0.0285` n `6`; index avg `-0.1415` n `25`; metal avg `-0.1802` n `20`; unknown avg `1.4603` n `766`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `-1.2628` n `230`; crypto_major avg `-1.1623` n `8`; equity avg `-1.7892` n `92`; fx avg `0.0997` n `6`; index avg `-0.411` n `25`; metal avg `-0.2456` n `20`; unknown avg `1.7363` n `766`
- 24h: commodity avg `0.1438` n `12`; crypto_alt avg `-2.479` n `230`; crypto_major avg `-1.4754` n `8`; equity avg `-2.2702` n `92`; fx avg `0.0432` n `6`; index avg `-0.4603` n `25`; metal avg `-0.4985` n `20`; unknown avg `-0.1138` n `741`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
