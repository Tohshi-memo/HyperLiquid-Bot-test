# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T21:37:40.989990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `0.2365` n `235`; crypto_major avg `0.0884` n `8`; equity avg `0.0184` n `150`; fx avg `0.0039` n `6`; index avg `0.0088` n `26`; metal avg `0.0073` n `20`; unknown avg `0.2851` n `1076`
- 1h: commodity avg `-0.034` n `13`; crypto_alt avg `0.056` n `235`; crypto_major avg `-0.0531` n `8`; equity avg `0.0413` n `150`; fx avg `0.004` n `6`; index avg `0.0236` n `26`; metal avg `0.0163` n `20`; unknown avg `1.8523` n `1068`
- 4h: commodity avg `0.2454` n `13`; crypto_alt avg `-0.3526` n `235`; crypto_major avg `-0.1117` n `8`; equity avg `-0.2266` n `150`; fx avg `-0.0077` n `6`; index avg `-0.0406` n `26`; metal avg `0.0399` n `20`; unknown avg `0.9793` n `1006`
- 24h: commodity avg `0.3125` n `13`; crypto_alt avg `-1.3369` n `235`; crypto_major avg `-0.8808` n `8`; equity avg `0.3894` n `149`; fx avg `0.1132` n `6`; index avg `-0.0204` n `26`; metal avg `0.0512` n `20`; unknown avg `855.6463` n `930`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
