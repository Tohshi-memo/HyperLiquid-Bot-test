# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T12:07:29.387629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1186` n `12`; crypto_alt avg `-0.0406` n `230`; crypto_major avg `-0.0641` n `8`; equity avg `-0.1399` n `113`; fx avg `-0.0043` n `6`; index avg `-0.0086` n `25`; metal avg `0.0382` n `20`; unknown avg `0.0097` n `787`
- 1h: commodity avg `0.0701` n `12`; crypto_alt avg `0.0711` n `230`; crypto_major avg `0.0207` n `8`; equity avg `-0.1131` n `113`; fx avg `0.0117` n `6`; index avg `-0.01` n `25`; metal avg `0.16` n `20`; unknown avg `-0.0458` n `787`
- 4h: commodity avg `-0.1812` n `12`; crypto_alt avg `-0.0622` n `230`; crypto_major avg `-0.205` n `8`; equity avg `0.2312` n `113`; fx avg `0.0179` n `6`; index avg `0.052` n `25`; metal avg `0.1981` n `20`; unknown avg `2.8716` n `787`
- 24h: commodity avg `0.0355` n `12`; crypto_alt avg `-0.6829` n `230`; crypto_major avg `-0.6326` n `8`; equity avg `1.9127` n `113`; fx avg `-0.0275` n `6`; index avg `0.3628` n `25`; metal avg `-0.1047` n `20`; unknown avg `0.9113` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
