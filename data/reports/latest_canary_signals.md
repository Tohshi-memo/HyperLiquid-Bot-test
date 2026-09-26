# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T06:22:25.188111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.2327` n `234`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0132` n `141`; fx avg `0.0003` n `6`; index avg `0.0034` n `26`; metal avg `0.0014` n `20`; unknown avg `6.1421` n `961`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `0.2167` n `234`; crypto_major avg `-0.1245` n `8`; equity avg `-0.0324` n `141`; fx avg `-0.0053` n `6`; index avg `-0.0027` n `26`; metal avg `0.0007` n `20`; unknown avg `1.7891` n `935`
- 4h: commodity avg `0.0143` n `12`; crypto_alt avg `-0.076` n `234`; crypto_major avg `-0.7332` n `8`; equity avg `-0.0276` n `141`; fx avg `-0.0055` n `6`; index avg `0.0014` n `26`; metal avg `-0.0095` n `20`; unknown avg `1.4435` n `929`
- 24h: commodity avg `0.109` n `12`; crypto_alt avg `2.9573` n `234`; crypto_major avg `0.7056` n `8`; equity avg `-0.7563` n `141`; fx avg `-0.092` n `6`; index avg `0.052` n `26`; metal avg `0.166` n `20`; unknown avg `1128.7996` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
