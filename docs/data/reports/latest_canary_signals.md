# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T05:37:16.389078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0919` n `12`; crypto_alt avg `0.308` n `228`; crypto_major avg `0.186` n `8`; equity avg `0.0503` n `67`; fx avg `-0.0125` n `6`; index avg `0.0073` n `23`; metal avg `0.1056` n `18`; unknown avg `-0.0269` n `407`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `0.4869` n `228`; crypto_major avg `0.3807` n `8`; equity avg `-0.051` n `67`; fx avg `-0.0109` n `6`; index avg `0.0245` n `23`; metal avg `0.1572` n `18`; unknown avg `0.0831` n `407`
- 4h: commodity avg `-0.0913` n `12`; crypto_alt avg `1.187` n `228`; crypto_major avg `0.7089` n `8`; equity avg `0.3043` n `67`; fx avg `-0.0219` n `6`; index avg `0.1303` n `23`; metal avg `0.065` n `18`; unknown avg `-0.3227` n `407`
- 24h: commodity avg `0.6179` n `12`; crypto_alt avg `-0.0789` n `228`; crypto_major avg `-0.8505` n `8`; equity avg `-0.591` n `67`; fx avg `-0.0401` n `6`; index avg `0.0265` n `23`; metal avg `-0.2309` n `18`; unknown avg `0.467` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
