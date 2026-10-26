# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T08:37:28.960126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0942` n `13`; crypto_alt avg `0.6548` n `237`; crypto_major avg `0.4487` n `8`; equity avg `0.3572` n `152`; fx avg `-0.0017` n `6`; index avg `0.0502` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.4091` n `1240`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.8004` n `237`; crypto_major avg `0.5355` n `8`; equity avg `-0.0009` n `152`; fx avg `0.0188` n `6`; index avg `0.0402` n `26`; metal avg `0.0501` n `20`; unknown avg `17.8982` n `1144`
- 4h: commodity avg `0.1237` n `13`; crypto_alt avg `0.3775` n `237`; crypto_major avg `0.3306` n `8`; equity avg `-0.1782` n `152`; fx avg `0.0188` n `6`; index avg `-0.0365` n `26`; metal avg `-0.0175` n `20`; unknown avg `17.7197` n `1126`
- 24h: commodity avg `-0.5234` n `13`; crypto_alt avg `0.2363` n `237`; crypto_major avg `0.0086` n `8`; equity avg `-0.4498` n `152`; fx avg `0.052` n `6`; index avg `0.0032` n `26`; metal avg `0.1843` n `20`; unknown avg `-0.2949` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.252`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
