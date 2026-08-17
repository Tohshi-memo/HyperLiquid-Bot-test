# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:52:27.139375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0317` n `12`; crypto_alt avg `0.0667` n `230`; crypto_major avg `0.0922` n `8`; equity avg `0.021` n `114`; fx avg `-0.0322` n `6`; index avg `0.0019` n `25`; metal avg `-0.0083` n `20`; unknown avg `1.0796` n `792`
- 1h: commodity avg `-0.0751` n `12`; crypto_alt avg `0.3199` n `230`; crypto_major avg `0.4225` n `8`; equity avg `0.1336` n `114`; fx avg `-0.0371` n `6`; index avg `0.0209` n `25`; metal avg `0.0494` n `20`; unknown avg `1.9811` n `792`
- 4h: commodity avg `0.1402` n `12`; crypto_alt avg `-0.2503` n `230`; crypto_major avg `-0.0266` n `8`; equity avg `0.13` n `114`; fx avg `-0.0208` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0826` n `20`; unknown avg `-0.0397` n `792`
- 24h: commodity avg `-0.0992` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.9928` n `8`; equity avg `1.3032` n `114`; fx avg `-0.0435` n `6`; index avg `0.1539` n `25`; metal avg `0.1833` n `20`; unknown avg `-0.0125` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
