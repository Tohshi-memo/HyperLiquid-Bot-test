# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T13:52:29.707247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.0361` n `230`; crypto_major avg `0.0025` n `8`; equity avg `0.0262` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0893` n `791`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0454` n `230`; crypto_major avg `0.066` n `8`; equity avg `0.0373` n `114`; fx avg `-0.0039` n `6`; index avg `0.0042` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.1352` n `791`
- 4h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0393` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `-0.1052` n `114`; fx avg `-0.0145` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.1669` n `791`
- 24h: commodity avg `0.0392` n `12`; crypto_alt avg `0.0747` n `230`; crypto_major avg `0.0369` n `8`; equity avg `0.2571` n `114`; fx avg `-0.0218` n `6`; index avg `0.0367` n `25`; metal avg `0.0312` n `20`; unknown avg `0.1946` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
