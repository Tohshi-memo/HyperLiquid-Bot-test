# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T14:52:32.685046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1458` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `-0.0022` n `8`; equity avg `-0.0412` n `98`; fx avg `-0.0003` n `6`; index avg `0.0201` n `25`; metal avg `0.0386` n `20`; unknown avg `0.0095` n `771`
- 1h: commodity avg `-0.0841` n `12`; crypto_alt avg `-0.0812` n `230`; crypto_major avg `-0.05` n `8`; equity avg `0.3269` n `98`; fx avg `0.0154` n `6`; index avg `0.1093` n `25`; metal avg `0.1856` n `20`; unknown avg `0.0425` n `771`
- 4h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.0503` n `230`; crypto_major avg `0.1443` n `8`; equity avg `0.8342` n `98`; fx avg `0.0062` n `6`; index avg `0.1088` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.0162` n `771`
- 24h: commodity avg `0.4895` n `12`; crypto_alt avg `2.0427` n `230`; crypto_major avg `2.5324` n `8`; equity avg `2.9769` n `98`; fx avg `-0.026` n `6`; index avg `0.4093` n `25`; metal avg `0.5935` n `20`; unknown avg `0.3073` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0532`, n `666`, weak_sample_signal
