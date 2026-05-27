# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T18:37:21.881578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `-0.0735` n `8`; equity avg `0.048` n `67`; fx avg `0.0006` n `6`; index avg `0.0598` n `23`; metal avg `-0.096` n `18`; unknown avg `0.31` n `418`
- 1h: commodity avg `-0.3054` n `12`; crypto_alt avg `-0.3959` n `228`; crypto_major avg `-0.1195` n `8`; equity avg `0.1759` n `67`; fx avg `-0.0033` n `6`; index avg `0.1113` n `23`; metal avg `0.0095` n `18`; unknown avg `0.1116` n `418`
- 4h: commodity avg `-0.4564` n `12`; crypto_alt avg `-0.3031` n `228`; crypto_major avg `-0.2914` n `8`; equity avg `0.09` n `67`; fx avg `-0.034` n `6`; index avg `0.3346` n `23`; metal avg `0.04` n `18`; unknown avg `-0.388` n `418`
- 24h: commodity avg `-1.4168` n `12`; crypto_alt avg `-1.089` n `228`; crypto_major avg `-1.0059` n `8`; equity avg `-0.2843` n `67`; fx avg `-0.0782` n `6`; index avg `-0.4861` n `23`; metal avg `-0.8999` n `18`; unknown avg `-0.2313` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
