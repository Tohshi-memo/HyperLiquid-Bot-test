# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T08:07:24.691893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1341` n `12`; crypto_alt avg `-0.0722` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `-0.0612` n `92`; fx avg `0.003` n `6`; index avg `-0.0179` n `25`; metal avg `-0.0149` n `20`; unknown avg `0.0301` n `766`
- 1h: commodity avg `0.1929` n `12`; crypto_alt avg `-0.198` n `230`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0107` n `92`; fx avg `0.01` n `6`; index avg `0.005` n `25`; metal avg `-0.0677` n `20`; unknown avg `-0.0481` n `766`
- 4h: commodity avg `0.2118` n `12`; crypto_alt avg `0.187` n `230`; crypto_major avg `-0.002` n `8`; equity avg `0.9679` n `92`; fx avg `0.0778` n `6`; index avg `0.1907` n `25`; metal avg `0.0983` n `20`; unknown avg `0.0127` n `750`
- 24h: commodity avg `1.4802` n `12`; crypto_alt avg `-0.9895` n `230`; crypto_major avg `-0.9722` n `8`; equity avg `-0.4307` n `92`; fx avg `-0.0851` n `6`; index avg `-0.0973` n `25`; metal avg `-0.1481` n `20`; unknown avg `-0.2744` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
