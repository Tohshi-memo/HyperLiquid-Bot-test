# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T00:07:29.270909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0307` n `230`; crypto_major avg `0.0321` n `8`; equity avg `0.0566` n `112`; fx avg `-0.0005` n `6`; index avg `0.0148` n `25`; metal avg `0.0355` n `20`; unknown avg `0.0513` n `783`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0183` n `230`; crypto_major avg `0.0123` n `8`; equity avg `0.1929` n `112`; fx avg `-0.0071` n `6`; index avg `0.0082` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.1354` n `783`
- 4h: commodity avg `-0.0419` n `12`; crypto_alt avg `-0.2799` n `230`; crypto_major avg `-0.2185` n `8`; equity avg `0.215` n `112`; fx avg `0.0258` n `6`; index avg `0.0104` n `25`; metal avg `0.1282` n `20`; unknown avg `-0.0763` n `782`
- 24h: commodity avg `-0.1931` n `12`; crypto_alt avg `-0.5881` n `230`; crypto_major avg `-0.205` n `8`; equity avg `1.6057` n `112`; fx avg `-0.1341` n `6`; index avg `0.0403` n `25`; metal avg `0.4663` n `20`; unknown avg `0.0798` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
