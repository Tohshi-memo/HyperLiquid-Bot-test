# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T04:09:55.007917+00:00`
- Correlation status: `ready`
- Asset price records: `420`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0968` n `7`; crypto_alt avg `0.0736` n `223`; crypto_major avg `0.0845` n `7`; equity avg `0.1258` n `47`; fx avg `-0.0048` n `4`; index avg `0.02` n `6`; metal avg `0.0657` n `7`; unknown avg `0.0597` n `313`
- 1h: commodity avg `0.0517` n `7`; crypto_alt avg `0.1344` n `223`; crypto_major avg `0.2433` n `7`; equity avg `0.4` n `47`; fx avg `0.0156` n `4`; index avg `0.1822` n `6`; metal avg `0.1941` n `7`; unknown avg `0.0142` n `313`
- 4h: commodity avg `0.0688` n `7`; crypto_alt avg `1.3065` n `223`; crypto_major avg `0.7719` n `7`; equity avg `0.6448` n `47`; fx avg `-0.0306` n `4`; index avg `0.5601` n `6`; metal avg `1.2283` n `7`; unknown avg `0.1451` n `313`
- 24h: commodity avg `-1.485` n `7`; crypto_alt avg `2.7125` n `223`; crypto_major avg `1.9676` n `7`; equity avg `3.1561` n `47`; fx avg `-0.1731` n `4`; index avg `2.2916` n `6`; metal avg `2.3485` n `7`; unknown avg `1.4942` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1811`, n `416`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1748`, n `416`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `416`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `416`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1231`, n `416`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.11`, n `416`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `412`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `416`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `416`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0946`, n `412`, weak_sample_signal
