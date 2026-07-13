# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T22:37:31.682935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0575` n `12`; crypto_alt avg `-0.101` n `230`; crypto_major avg `-0.1093` n `8`; equity avg `-0.0689` n `92`; fx avg `-0.0336` n `6`; index avg `0.0036` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.1283` n `766`
- 1h: commodity avg `0.0789` n `12`; crypto_alt avg `0.4161` n `230`; crypto_major avg `0.4746` n `8`; equity avg `0.0179` n `92`; fx avg `-0.0429` n `6`; index avg `0.0192` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.0015` n `766`
- 4h: commodity avg `0.0998` n `12`; crypto_alt avg `-0.3325` n `230`; crypto_major avg `0.0543` n `8`; equity avg `0.0103` n `92`; fx avg `-0.0417` n `6`; index avg `-0.0459` n `25`; metal avg `0.0338` n `20`; unknown avg `-0.3265` n `766`
- 24h: commodity avg `0.9082` n `12`; crypto_alt avg `-1.8562` n `230`; crypto_major avg `-2.2763` n `8`; equity avg `-2.9936` n `92`; fx avg `-0.0614` n `6`; index avg `-0.5759` n `25`; metal avg `-0.2899` n `20`; unknown avg `-0.3776` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
