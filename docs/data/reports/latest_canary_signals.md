# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:22:26.483384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0225` n `230`; crypto_major avg `0.0084` n `8`; equity avg `0.0012` n `114`; fx avg `0.0003` n `6`; index avg `0.0018` n `25`; metal avg `-0.0219` n `20`; unknown avg `0.0275` n `791`
- 1h: commodity avg `-0.0379` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `-0.0637` n `8`; equity avg `0.0033` n `114`; fx avg `0.0012` n `6`; index avg `0.0058` n `25`; metal avg `-0.0217` n `20`; unknown avg `0.1255` n `791`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `-0.2511` n `230`; crypto_major avg `-0.1684` n `8`; equity avg `0.0367` n `114`; fx avg `0.0031` n `6`; index avg `0.0107` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0086` n `791`
- 24h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.2589` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.2797` n `114`; fx avg `-0.0009` n `6`; index avg `0.044` n `25`; metal avg `0.0312` n `20`; unknown avg `0.0778` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
