# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T05:52:28.527487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.3865` n `237`; crypto_major avg `0.2427` n `8`; equity avg `0.1025` n `154`; fx avg `0.0047` n `6`; index avg `0.0045` n `27`; metal avg `0.0063` n `20`; unknown avg `7.0034` n `1238`
- 1h: commodity avg `0.0109` n `13`; crypto_alt avg `0.3151` n `237`; crypto_major avg `0.2248` n `8`; equity avg `-0.2119` n `154`; fx avg `-0.0036` n `6`; index avg `-0.0739` n `27`; metal avg `-0.0709` n `20`; unknown avg `-0.0775` n `1234`
- 4h: commodity avg `0.0191` n `13`; crypto_alt avg `-0.2014` n `237`; crypto_major avg `-0.2785` n `8`; equity avg `-1.2158` n `154`; fx avg `-0.0048` n `6`; index avg `-0.0626` n `27`; metal avg `-0.0996` n `20`; unknown avg `291.9651` n `1214`
- 24h: commodity avg `0.0231` n `13`; crypto_alt avg `-0.2779` n `237`; crypto_major avg `0.0661` n `8`; equity avg `0.4239` n `153`; fx avg `-0.03` n `6`; index avg `0.0364` n `27`; metal avg `-0.1978` n `20`; unknown avg `1113.6329` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
