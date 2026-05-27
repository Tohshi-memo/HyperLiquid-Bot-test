# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T07:37:17.209725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0669` n `12`; crypto_alt avg `0.172` n `228`; crypto_major avg `0.0831` n `8`; equity avg `0.0603` n `67`; fx avg `-0.0151` n `6`; index avg `0.0295` n `23`; metal avg `-0.0475` n `18`; unknown avg `-0.1734` n `418`
- 1h: commodity avg `-0.2928` n `12`; crypto_alt avg `0.0041` n `228`; crypto_major avg `0.1583` n `8`; equity avg `0.3057` n `67`; fx avg `0.016` n `6`; index avg `0.0779` n `23`; metal avg `-0.0714` n `18`; unknown avg `0.1061` n `418`
- 4h: commodity avg `-0.53` n `12`; crypto_alt avg `0.292` n `228`; crypto_major avg `0.6176` n `8`; equity avg `-0.0065` n `67`; fx avg `0.0338` n `6`; index avg `-0.1285` n `23`; metal avg `-0.84` n `18`; unknown avg `0.546` n `400`
- 24h: commodity avg `-1.2094` n `12`; crypto_alt avg `-0.2984` n `228`; crypto_major avg `0.3798` n `8`; equity avg `0.9606` n `67`; fx avg `-0.0042` n `6`; index avg `0.8931` n `23`; metal avg `-0.7634` n `18`; unknown avg `0.7984` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
