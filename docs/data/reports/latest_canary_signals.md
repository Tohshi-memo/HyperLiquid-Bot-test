# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T23:52:24.140321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.1333` n `234`; crypto_major avg `0.0237` n `8`; equity avg `-0.0123` n `141`; fx avg `-0.0057` n `6`; index avg `0.0003` n `26`; metal avg `0.0034` n `20`; unknown avg `1.2196` n `960`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `0.1183` n `234`; crypto_major avg `-0.1638` n `8`; equity avg `-0.0321` n `141`; fx avg `-0.0084` n `6`; index avg `0.0076` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.9248` n `958`
- 4h: commodity avg `0.0662` n `12`; crypto_alt avg `0.8232` n `234`; crypto_major avg `0.2683` n `8`; equity avg `-0.0194` n `141`; fx avg `-0.0211` n `6`; index avg `0.0008` n `26`; metal avg `-0.0159` n `20`; unknown avg `0.15` n `852`
- 24h: commodity avg `-0.3769` n `12`; crypto_alt avg `3.0956` n `234`; crypto_major avg `1.2187` n `8`; equity avg `0.1574` n `141`; fx avg `-0.2609` n `6`; index avg `0.2726` n `26`; metal avg `0.1848` n `20`; unknown avg `1122.6774` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
