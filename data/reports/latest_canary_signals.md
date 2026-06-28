# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T19:37:27.271530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0648` n `228`; crypto_major avg `-0.0333` n `8`; equity avg `0.0143` n `88`; fx avg `0.0219` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0013` n `20`; unknown avg `0.0016` n `764`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.0225` n `228`; crypto_major avg `-0.1292` n `8`; equity avg `-0.0316` n `88`; fx avg `-0.0004` n `6`; index avg `-0.0179` n `23`; metal avg `-0.0038` n `20`; unknown avg `-0.1221` n `764`
- 4h: commodity avg `0.0176` n `12`; crypto_alt avg `-0.8921` n `228`; crypto_major avg `-0.8496` n `8`; equity avg `-0.0956` n `88`; fx avg `-0.0318` n `6`; index avg `-0.0433` n `23`; metal avg `0.017` n `20`; unknown avg `-0.3202` n `764`
- 24h: commodity avg `0.3476` n `12`; crypto_alt avg `0.0138` n `228`; crypto_major avg `-0.7933` n `8`; equity avg `0.1377` n `88`; fx avg `-0.0355` n `6`; index avg `-0.0325` n `23`; metal avg `0.0125` n `20`; unknown avg `14.8823` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
