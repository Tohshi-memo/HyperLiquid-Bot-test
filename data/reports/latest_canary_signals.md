# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T08:07:26.849873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `12`; crypto_alt avg `0.5489` n `231`; crypto_major avg `0.703` n `8`; equity avg `0.3231` n `127`; fx avg `-0.0078` n `6`; index avg `0.04` n `26`; metal avg `0.0586` n `20`; unknown avg `0.0332` n `792`
- 1h: commodity avg `0.106` n `12`; crypto_alt avg `0.7495` n `231`; crypto_major avg `1.0077` n `8`; equity avg `0.43` n `127`; fx avg `-0.0192` n `6`; index avg `0.0389` n `26`; metal avg `-0.0179` n `20`; unknown avg `0.1109` n `791`
- 4h: commodity avg `-0.1523` n `12`; crypto_alt avg `0.8321` n `231`; crypto_major avg `1.113` n `8`; equity avg `0.4441` n `127`; fx avg `0.003` n `6`; index avg `0.0173` n `26`; metal avg `-0.1931` n `20`; unknown avg `0.161` n `775`
- 24h: commodity avg `0.3257` n `12`; crypto_alt avg `1.1723` n `231`; crypto_major avg `1.5481` n `8`; equity avg `1.9515` n `127`; fx avg `-0.1028` n `6`; index avg `0.3011` n `26`; metal avg `-0.3195` n `20`; unknown avg `0.4813` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
