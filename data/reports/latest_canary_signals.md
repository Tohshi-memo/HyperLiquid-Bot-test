# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T21:45:45.613085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.112` n `12`; crypto_alt avg `-0.039` n `228`; crypto_major avg `0.1348` n `8`; equity avg `-0.0186` n `69`; fx avg `-0.0006` n `6`; index avg `0.034` n `23`; metal avg `0.0204` n `18`; unknown avg `-0.0207` n `421`
- 1h: commodity avg `0.2371` n `12`; crypto_alt avg `0.0574` n `228`; crypto_major avg `0.3267` n `8`; equity avg `0.0484` n `69`; fx avg `-0.0017` n `6`; index avg `0.0476` n `23`; metal avg `0.0147` n `18`; unknown avg `0.0449` n `421`
- 4h: commodity avg `0.2606` n `12`; crypto_alt avg `0.3994` n `228`; crypto_major avg `0.2919` n `8`; equity avg `0.2836` n `69`; fx avg `0.0056` n `6`; index avg `0.0332` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.045` n `421`
- 24h: commodity avg `0.1552` n `12`; crypto_alt avg `1.9529` n `228`; crypto_major avg `3.1892` n `8`; equity avg `1.0724` n `69`; fx avg `0.0312` n `6`; index avg `0.0934` n `23`; metal avg `0.1284` n `18`; unknown avg `0.4279` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
