# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:37:36.553242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `0.0376` n `8`; equity avg `0.0299` n `114`; fx avg `0.0169` n `6`; index avg `-0.021` n `25`; metal avg `-0.0227` n `20`; unknown avg `0.0136` n `792`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.0731` n `230`; crypto_major avg `0.0501` n `8`; equity avg `0.0692` n `114`; fx avg `0.0229` n `6`; index avg `-0.0199` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0008` n `792`
- 4h: commodity avg `0.043` n `12`; crypto_alt avg `0.1184` n `230`; crypto_major avg `0.5107` n `8`; equity avg `0.9068` n `114`; fx avg `0.0348` n `6`; index avg `0.0946` n `25`; metal avg `0.2199` n `20`; unknown avg `0.1025` n `792`
- 24h: commodity avg `0.0286` n `12`; crypto_alt avg `-0.2325` n `230`; crypto_major avg `0.7788` n `8`; equity avg `1.6845` n `114`; fx avg `0.021` n `6`; index avg `0.1893` n `25`; metal avg `0.3017` n `20`; unknown avg `0.1797` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
