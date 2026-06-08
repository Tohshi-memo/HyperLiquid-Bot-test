# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T17:37:26.085486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0909` n `12`; crypto_alt avg `0.0541` n `228`; crypto_major avg `-0.0204` n `8`; equity avg `0.0668` n `74`; fx avg `-0.0093` n `6`; index avg `0.0143` n `23`; metal avg `0.0214` n `18`; unknown avg `0.0829` n `517`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.1309` n `228`; crypto_major avg `-0.3235` n `8`; equity avg `-0.2759` n `74`; fx avg `-0.0067` n `6`; index avg `-0.2303` n `23`; metal avg `-0.1442` n `18`; unknown avg `0.0434` n `517`
- 4h: commodity avg `0.1932` n `12`; crypto_alt avg `0.1794` n `228`; crypto_major avg `0.0917` n `8`; equity avg `0.9113` n `74`; fx avg `-0.0304` n `6`; index avg `-0.0804` n `23`; metal avg `-0.3986` n `18`; unknown avg `-0.2542` n `517`
- 24h: commodity avg `-0.6307` n `12`; crypto_alt avg `1.7104` n `228`; crypto_major avg `2.3718` n `8`; equity avg `1.9059` n `74`; fx avg `-0.2961` n `6`; index avg `0.8293` n `23`; metal avg `-0.0927` n `18`; unknown avg `-2.0439` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
