# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T14:22:30.592976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.1128` n `230`; crypto_major avg `-0.076` n `8`; equity avg `0.6596` n `102`; fx avg `-0.018` n `6`; index avg `0.0891` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0005` n `785`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.2138` n `230`; crypto_major avg `0.3092` n `8`; equity avg `1.3421` n `102`; fx avg `-0.0466` n `6`; index avg `0.0334` n `25`; metal avg `0.1009` n `20`; unknown avg `0.038` n `785`
- 4h: commodity avg `-0.1174` n `12`; crypto_alt avg `0.5982` n `230`; crypto_major avg `0.5093` n `8`; equity avg `1.1211` n `102`; fx avg `-0.0639` n `6`; index avg `0.0027` n `25`; metal avg `-0.3301` n `20`; unknown avg `0.3373` n `785`
- 24h: commodity avg `-0.364` n `12`; crypto_alt avg `0.0439` n `230`; crypto_major avg `0.4862` n `8`; equity avg `0.5624` n `102`; fx avg `-0.1828` n `6`; index avg `-0.1128` n `25`; metal avg `-0.4914` n `20`; unknown avg `1.4361` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
