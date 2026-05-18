# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T08:52:14.781195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0574` n `12`; crypto_alt avg `0.1278` n `228`; crypto_major avg `0.0789` n `8`; equity avg `0.0793` n `66`; fx avg `0.0122` n `5`; index avg `0.0501` n `23`; metal avg `0.0752` n `18`; unknown avg `1.0442` n `383`
- 1h: commodity avg `-0.0657` n `12`; crypto_alt avg `0.2399` n `228`; crypto_major avg `0.0731` n `8`; equity avg `0.6212` n `66`; fx avg `-0.0042` n `5`; index avg `0.3003` n `23`; metal avg `0.3477` n `18`; unknown avg `0.9763` n `383`
- 4h: commodity avg `-0.3329` n `12`; crypto_alt avg `-0.7937` n `228`; crypto_major avg `-0.6122` n `8`; equity avg `0.8778` n `66`; fx avg `-0.0695` n `5`; index avg `0.3631` n `23`; metal avg `0.6347` n `18`; unknown avg `0.7744` n `363`
- 24h: commodity avg `0.5789` n `12`; crypto_alt avg `-2.7631` n `228`; crypto_major avg `-1.2447` n `8`; equity avg `0.626` n `65`; fx avg `0.0364` n `5`; index avg `0.3872` n `23`; metal avg `0.2795` n `18`; unknown avg `0.538` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
