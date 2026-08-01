# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T01:52:25.216375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0858` n `12`; crypto_alt avg `-0.111` n `230`; crypto_major avg `-0.0174` n `8`; equity avg `0.0346` n `102`; fx avg `0.0031` n `6`; index avg `0.0513` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0597` n `781`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.002` n `230`; crypto_major avg `0.0428` n `8`; equity avg `-0.0111` n `102`; fx avg `0.0016` n `6`; index avg `0.08` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.1946` n `781`
- 4h: commodity avg `-0.2035` n `12`; crypto_alt avg `0.5661` n `230`; crypto_major avg `0.1907` n `8`; equity avg `-0.0129` n `102`; fx avg `-0.0179` n `6`; index avg `0.0792` n `25`; metal avg `-0.0135` n `20`; unknown avg `1.58` n `781`
- 24h: commodity avg `0.9616` n `12`; crypto_alt avg `-0.1816` n `230`; crypto_major avg `-1.8922` n `8`; equity avg `-2.3812` n `102`; fx avg `-0.1301` n `6`; index avg `-0.1917` n `25`; metal avg `-0.2216` n `20`; unknown avg `2.6414` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
