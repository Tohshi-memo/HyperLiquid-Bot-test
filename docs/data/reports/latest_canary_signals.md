# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T00:22:27.728353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `-0.1176` n `228`; crypto_major avg `-0.177` n `8`; equity avg `-0.219` n `88`; fx avg `0.0107` n `6`; index avg `-0.0704` n `23`; metal avg `0.0133` n `20`; unknown avg `0.1606` n `765`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `0.0171` n `228`; crypto_major avg `-0.2297` n `8`; equity avg `-0.1945` n `88`; fx avg `0.0452` n `6`; index avg `-0.0471` n `23`; metal avg `-0.1501` n `20`; unknown avg `0.0755` n `765`
- 4h: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.6219` n `228`; crypto_major avg `-0.63` n `8`; equity avg `-0.0735` n `88`; fx avg `0.0675` n `6`; index avg `-0.05` n `23`; metal avg `-0.056` n `20`; unknown avg `1.1732` n `763`
- 24h: commodity avg `-0.107` n `12`; crypto_alt avg `1.6806` n `228`; crypto_major avg `2.9062` n `8`; equity avg `2.0503` n `88`; fx avg `0.2207` n `6`; index avg `0.2809` n `23`; metal avg `-0.2159` n `20`; unknown avg `1.8394` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
