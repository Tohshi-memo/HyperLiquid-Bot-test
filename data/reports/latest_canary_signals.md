# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T01:52:26.788470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `0.0066` n `230`; crypto_major avg `0.004` n `8`; equity avg `0.0199` n `112`; fx avg `-0.0026` n `6`; index avg `0.0212` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0002` n `783`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.2345` n `230`; crypto_major avg `0.1796` n `8`; equity avg `0.0432` n `112`; fx avg `0.0034` n `6`; index avg `0.0164` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.1291` n `783`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `0.1343` n `230`; crypto_major avg `0.1101` n `8`; equity avg `0.1797` n `112`; fx avg `0.0138` n `6`; index avg `0.0058` n `25`; metal avg `0.0768` n `20`; unknown avg `-0.3023` n `782`
- 24h: commodity avg `-0.1385` n `12`; crypto_alt avg `-0.4966` n `230`; crypto_major avg `-0.0028` n `8`; equity avg `2.2578` n `112`; fx avg `-0.052` n `6`; index avg `0.2664` n `25`; metal avg `0.4081` n `20`; unknown avg `-0.0758` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
