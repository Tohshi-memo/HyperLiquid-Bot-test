# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T15:52:32.566374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1966` n `13`; crypto_alt avg `-0.4103` n `237`; crypto_major avg `-0.3187` n `8`; equity avg `-0.3379` n `154`; fx avg `-0.0047` n `6`; index avg `-0.0448` n `27`; metal avg `-0.0357` n `20`; unknown avg `0.4643` n `1238`
- 1h: commodity avg `0.3067` n `13`; crypto_alt avg `0.2968` n `237`; crypto_major avg `0.2927` n `8`; equity avg `0.3688` n `154`; fx avg `-0.0039` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0074` n `20`; unknown avg `1.4155` n `1232`
- 4h: commodity avg `0.3062` n `13`; crypto_alt avg `0.8287` n `237`; crypto_major avg `0.4663` n `8`; equity avg `1.1785` n `153`; fx avg `0.0173` n `6`; index avg `0.1645` n `27`; metal avg `0.0152` n `20`; unknown avg `628.2686` n `1154`
- 24h: commodity avg `-0.0023` n `13`; crypto_alt avg `0.3075` n `237`; crypto_major avg `0.3207` n `8`; equity avg `0.8946` n `153`; fx avg `0.0567` n `6`; index avg `-0.0419` n `27`; metal avg `0.1585` n `20`; unknown avg `803.5628` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2339`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
