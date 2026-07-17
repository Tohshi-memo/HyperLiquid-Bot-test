# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T22:52:33.157376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.2518` n `230`; crypto_major avg `0.0782` n `8`; equity avg `0.0159` n `96`; fx avg `0.0021` n `6`; index avg `0.0064` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0265` n `769`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `0.26` n `230`; crypto_major avg `-0.0866` n `8`; equity avg `0.0516` n `96`; fx avg `-0.0037` n `6`; index avg `-0.0121` n `25`; metal avg `0.0304` n `20`; unknown avg `0.0131` n `769`
- 4h: commodity avg `0.1584` n `12`; crypto_alt avg `-0.4645` n `230`; crypto_major avg `-0.3843` n `8`; equity avg `-0.5697` n `96`; fx avg `-0.05` n `6`; index avg `-0.1149` n `25`; metal avg `0.026` n `20`; unknown avg `0.0849` n `769`
- 24h: commodity avg `0.7155` n `12`; crypto_alt avg `-0.6908` n `230`; crypto_major avg `-0.8693` n `8`; equity avg `-1.0402` n `94`; fx avg `0.0467` n `6`; index avg `-0.2745` n `25`; metal avg `0.0555` n `20`; unknown avg `0.0319` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
