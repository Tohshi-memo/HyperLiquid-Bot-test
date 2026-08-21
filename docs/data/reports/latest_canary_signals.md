# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T13:57:18.579111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1163` n `12`; crypto_alt avg `0.7309` n `230`; crypto_major avg `0.7521` n `8`; equity avg `0.2022` n `121`; fx avg `0.0132` n `6`; index avg `0.0261` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.016` n `793`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.1631` n `230`; crypto_major avg `0.7728` n `8`; equity avg `-0.26` n `121`; fx avg `-0.0029` n `6`; index avg `-0.1082` n `25`; metal avg `-0.0148` n `20`; unknown avg `1.132` n `793`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `1.6424` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `-0.2243` n `121`; fx avg `-0.0108` n `6`; index avg `-0.0626` n `25`; metal avg `0.0017` n `20`; unknown avg `1.3649` n `793`
- 24h: commodity avg `0.1206` n `12`; crypto_alt avg `8.3461` n `230`; crypto_major avg `6.9991` n `8`; equity avg `1.79` n `121`; fx avg `-0.0901` n `6`; index avg `0.1014` n `25`; metal avg `0.8386` n `20`; unknown avg `3.5275` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
