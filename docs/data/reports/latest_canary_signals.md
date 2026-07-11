# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T03:37:28.818759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.1106` n `229`; crypto_major avg `0.0728` n `8`; equity avg `0.0147` n `92`; fx avg `0.0` n `6`; index avg `0.0004` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.1116` n `765`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `0.1694` n `229`; crypto_major avg `0.1437` n `8`; equity avg `0.0277` n `92`; fx avg `0.0037` n `6`; index avg `0.0064` n `25`; metal avg `0.0357` n `20`; unknown avg `-0.008` n `765`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1842` n `229`; crypto_major avg `-0.024` n `8`; equity avg `0.0877` n `92`; fx avg `0.0048` n `6`; index avg `0.0017` n `25`; metal avg `0.0321` n `20`; unknown avg `3.194` n `765`
- 24h: commodity avg `-0.3632` n `12`; crypto_alt avg `0.5324` n `229`; crypto_major avg `-0.0775` n `8`; equity avg `-0.6816` n `92`; fx avg `-0.1777` n `6`; index avg `0.0303` n `25`; metal avg `-0.0261` n `20`; unknown avg `3.1692` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
