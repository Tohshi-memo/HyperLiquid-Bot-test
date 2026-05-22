# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T08:22:17.725133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0645` n `12`; crypto_alt avg `0.2993` n `228`; crypto_major avg `0.3087` n `8`; equity avg `0.1861` n `67`; fx avg `0.0291` n `6`; index avg `0.071` n `23`; metal avg `-0.0057` n `18`; unknown avg `0.0617` n `386`
- 1h: commodity avg `0.2304` n `12`; crypto_alt avg `0.317` n `228`; crypto_major avg `0.3734` n `8`; equity avg `0.2005` n `67`; fx avg `0.0303` n `6`; index avg `0.0842` n `23`; metal avg `-0.0215` n `18`; unknown avg `0.2683` n `386`
- 4h: commodity avg `0.6907` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `-0.0332` n `8`; equity avg `0.0962` n `67`; fx avg `0.0362` n `6`; index avg `0.0899` n `23`; metal avg `-0.3014` n `18`; unknown avg `-0.0181` n `376`
- 24h: commodity avg `-0.1582` n `12`; crypto_alt avg `1.7812` n `228`; crypto_major avg `-0.189` n `8`; equity avg `1.4811` n `67`; fx avg `0.1225` n `6`; index avg `0.6891` n `23`; metal avg `0.405` n `18`; unknown avg `1.6619` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.038`, n `668`, weak_sample_signal
