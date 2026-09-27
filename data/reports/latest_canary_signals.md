# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T03:22:26.697162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.083` n `234`; crypto_major avg `-0.1899` n `8`; equity avg `-0.0184` n `141`; fx avg `-0.0034` n `6`; index avg `0.0022` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.3197` n `961`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.355` n `234`; crypto_major avg `-0.3301` n `8`; equity avg `-0.0041` n `141`; fx avg `-0.0045` n `6`; index avg `0.0072` n `26`; metal avg `-0.006` n `20`; unknown avg `2.419` n `955`
- 4h: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.2105` n `234`; crypto_major avg `-0.1018` n `8`; equity avg `0.0675` n `141`; fx avg `-0.0051` n `6`; index avg `0.0063` n `26`; metal avg `-0.0042` n `20`; unknown avg `2.1526` n `947`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `1.0367` n `234`; crypto_major avg `-0.3792` n `8`; equity avg `0.2405` n `141`; fx avg `-0.002` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0091` n `20`; unknown avg `4.5541` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
