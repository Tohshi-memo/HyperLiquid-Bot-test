# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T08:07:28.618049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.0213` n `233`; crypto_major avg `-0.0446` n `8`; equity avg `-0.0489` n `136`; fx avg `-0.0022` n `6`; index avg `0.0013` n `27`; metal avg `-0.0176` n `20`; unknown avg `0.0811` n `836`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.1772` n `233`; crypto_major avg `-0.2106` n `8`; equity avg `-0.1468` n `136`; fx avg `-0.002` n `6`; index avg `-0.0088` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.0155` n `836`
- 4h: commodity avg `0.0635` n `12`; crypto_alt avg `-0.3012` n `233`; crypto_major avg `-0.4436` n `8`; equity avg `-0.5212` n `136`; fx avg `-0.0103` n `6`; index avg `-0.0775` n `26`; metal avg `-0.0253` n `20`; unknown avg `51.3875` n `804`
- 24h: commodity avg `0.1629` n `12`; crypto_alt avg `0.1199` n `233`; crypto_major avg `-0.6745` n `8`; equity avg `-0.9677` n `136`; fx avg `-0.0108` n `6`; index avg `-0.1414` n `26`; metal avg `0.0039` n `20`; unknown avg `0.1785` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
