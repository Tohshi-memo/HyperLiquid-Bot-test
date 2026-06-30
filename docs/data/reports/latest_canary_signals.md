# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T00:52:27.281942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.1616` n `228`; crypto_major avg `0.1469` n `8`; equity avg `0.1092` n `88`; fx avg `0.0057` n `6`; index avg `0.0062` n `23`; metal avg `-0.0634` n `20`; unknown avg `1.2493` n `765`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.4991` n `228`; crypto_major avg `-0.7194` n `8`; equity avg `-0.4205` n `88`; fx avg `0.0703` n `6`; index avg `-0.1395` n `23`; metal avg `-0.3107` n `20`; unknown avg `1.6402` n `765`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.7791` n `228`; crypto_major avg `-0.9653` n `8`; equity avg `-0.3431` n `88`; fx avg `0.078` n `6`; index avg `-0.1488` n `23`; metal avg `-0.2387` n `20`; unknown avg `1.2119` n `763`
- 24h: commodity avg `-0.2278` n `12`; crypto_alt avg `0.9954` n `228`; crypto_major avg `2.1366` n `8`; equity avg `1.97` n `88`; fx avg `0.23` n `6`; index avg `0.218` n `23`; metal avg `-0.4999` n `20`; unknown avg `2.1502` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
