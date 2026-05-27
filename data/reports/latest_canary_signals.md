# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T00:52:20.026518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0393` n `12`; crypto_alt avg `0.06` n `228`; crypto_major avg `0.1516` n `8`; equity avg `0.0606` n `67`; fx avg `0.0071` n `6`; index avg `0.0132` n `23`; metal avg `-0.034` n `18`; unknown avg `-0.0898` n `418`
- 1h: commodity avg `0.0552` n `12`; crypto_alt avg `0.6448` n `228`; crypto_major avg `0.4817` n `8`; equity avg `0.0629` n `67`; fx avg `-0.013` n `6`; index avg `0.0456` n `23`; metal avg `-0.0088` n `18`; unknown avg `1.0151` n `418`
- 4h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.324` n `228`; crypto_major avg `0.3537` n `8`; equity avg `0.2854` n `67`; fx avg `0.0031` n `6`; index avg `0.2297` n `23`; metal avg `0.32` n `18`; unknown avg `0.5785` n `418`
- 24h: commodity avg `0.2768` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.0837` n `8`; equity avg `0.6928` n `67`; fx avg `-0.1016` n `6`; index avg `1.0278` n `23`; metal avg `-0.0138` n `18`; unknown avg `1.6433` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
