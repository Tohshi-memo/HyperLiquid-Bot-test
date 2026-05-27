# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T08:22:19.318284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8533` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.0865` n `228`; crypto_major avg `0.1754` n `8`; equity avg `0.2389` n `67`; fx avg `0.0037` n `6`; index avg `0.2077` n `23`; metal avg `0.0909` n `18`; unknown avg `0.1091` n `418`
- 1h: commodity avg `-0.4014` n `12`; crypto_alt avg `0.4948` n `228`; crypto_major avg `0.1791` n `8`; equity avg `0.3299` n `67`; fx avg `-0.027` n `6`; index avg `0.1982` n `23`; metal avg `0.1566` n `18`; unknown avg `-0.0653` n `418`
- 4h: commodity avg `-0.7074` n `12`; crypto_alt avg `1.2843` n `228`; crypto_major avg `1.1694` n `8`; equity avg `0.4026` n `67`; fx avg `0.0395` n `6`; index avg `0.0706` n `23`; metal avg `-0.6839` n `18`; unknown avg `0.7754` n `400`
- 24h: commodity avg `-1.5401` n `12`; crypto_alt avg `-0.5097` n `228`; crypto_major avg `0.316` n `8`; equity avg `1.0189` n `67`; fx avg `-0.0258` n `6`; index avg `1.0158` n `23`; metal avg `-0.6641` n `18`; unknown avg `0.7785` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
