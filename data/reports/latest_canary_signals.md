# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T05:07:35.361616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0785` n `13`; crypto_alt avg `-0.3076` n `239`; crypto_major avg `-0.1897` n `8`; equity avg `-0.3161` n `158`; fx avg `-0.011` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0261` n `20`; unknown avg `34.1095` n `1259`
- 1h: commodity avg `-0.0775` n `13`; crypto_alt avg `-0.4258` n `239`; crypto_major avg `-0.4326` n `8`; equity avg `-0.4265` n `158`; fx avg `-0.0201` n `6`; index avg `-0.0341` n `27`; metal avg `0.008` n `20`; unknown avg `13.9798` n `1253`
- 4h: commodity avg `0.2338` n `13`; crypto_alt avg `-0.6009` n `239`; crypto_major avg `-0.8691` n `8`; equity avg `0.3244` n `158`; fx avg `-0.0658` n `6`; index avg `0.0344` n `27`; metal avg `0.098` n `20`; unknown avg `3.6289` n `1232`
- 24h: commodity avg `0.1169` n `13`; crypto_alt avg `-2.0228` n `239`; crypto_major avg `-2.7107` n `8`; equity avg `0.1235` n `158`; fx avg `-0.0955` n `6`; index avg `0.0452` n `27`; metal avg `0.4916` n `20`; unknown avg `1.7214` n `984`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
