# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T08:32:31.259580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0201` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0013` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0519` n `228`; crypto_major avg `0.0445` n `8`; equity avg `0.0832` n `67`; fx avg `0.0037` n `6`; index avg `-0.009` n `23`; metal avg `-0.0311` n `18`; unknown avg `-0.1162` n `418`
- 1h: commodity avg `-0.3187` n `12`; crypto_alt avg `0.2701` n `228`; crypto_major avg `0.1404` n `8`; equity avg `0.3534` n `67`; fx avg `-0.0082` n `6`; index avg `0.1598` n `23`; metal avg `0.1732` n `18`; unknown avg `-0.0038` n `418`
- 4h: commodity avg `-0.6667` n `12`; crypto_alt avg `1.535` n `228`; crypto_major avg `1.3346` n `8`; equity avg `0.6517` n `67`; fx avg `0.0362` n `6`; index avg `0.1244` n `23`; metal avg `-0.6855` n `18`; unknown avg `0.4769` n `400`
- 24h: commodity avg `-1.665` n `12`; crypto_alt avg `-0.4061` n `228`; crypto_major avg `0.3326` n `8`; equity avg `1.0823` n `67`; fx avg `-0.0286` n `6`; index avg `0.9783` n `23`; metal avg `-0.5573` n `18`; unknown avg `0.5707` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
