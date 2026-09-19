# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T23:07:27.794579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.1353` n `234`; crypto_major avg `0.0488` n `8`; equity avg `0.0108` n `140`; fx avg `0.0009` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0023` n `20`; unknown avg `1.5269` n `941`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.879` n `234`; crypto_major avg `0.4606` n `8`; equity avg `0.0106` n `140`; fx avg `0.0016` n `6`; index avg `-0.0086` n `26`; metal avg `-0.001` n `20`; unknown avg `4.7173` n `933`
- 4h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.1713` n `234`; crypto_major avg `-0.6766` n `8`; equity avg `0.0692` n `140`; fx avg `-0.0292` n `6`; index avg `0.0069` n `26`; metal avg `-0.0076` n `20`; unknown avg `54.5864` n `911`
- 24h: commodity avg `0.0604` n `12`; crypto_alt avg `1.1649` n `234`; crypto_major avg `-0.1936` n `8`; equity avg `-0.0085` n `140`; fx avg `-0.0601` n `6`; index avg `0.0229` n `26`; metal avg `-0.024` n `20`; unknown avg `4.2152` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
