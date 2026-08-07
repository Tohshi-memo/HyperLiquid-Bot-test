# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T07:07:29.289613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `0.0642` n `8`; equity avg `0.0853` n `112`; fx avg `0.0023` n `6`; index avg `0.0324` n `25`; metal avg `-0.0312` n `20`; unknown avg `-0.0181` n `782`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `-0.1234` n `230`; crypto_major avg `0.1198` n `8`; equity avg `0.1449` n `112`; fx avg `-0.0533` n `6`; index avg `0.0286` n `25`; metal avg `0.079` n `20`; unknown avg `0.0134` n `782`
- 4h: commodity avg `0.1321` n `12`; crypto_alt avg `-0.0348` n `230`; crypto_major avg `-0.1798` n `8`; equity avg `0.2518` n `112`; fx avg `-0.0504` n `6`; index avg `0.0529` n `25`; metal avg `0.2807` n `20`; unknown avg `-0.0794` n `766`
- 24h: commodity avg `0.6144` n `12`; crypto_alt avg `0.1336` n `230`; crypto_major avg `-0.9325` n `8`; equity avg `1.2882` n `109`; fx avg `-0.0764` n `6`; index avg `-0.0284` n `25`; metal avg `0.2938` n `20`; unknown avg `110.7503` n `765`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
