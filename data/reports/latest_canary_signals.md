# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T06:22:23.319665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.2431` n `228`; crypto_major avg `-0.1114` n `8`; equity avg `0.0227` n `67`; fx avg `-0.0049` n `6`; index avg `0.0166` n `23`; metal avg `0.0948` n `18`; unknown avg `-0.2264` n `417`
- 1h: commodity avg `-0.1511` n `12`; crypto_alt avg `-0.0881` n `228`; crypto_major avg `-0.0099` n `8`; equity avg `0.1033` n `67`; fx avg `-0.0266` n `6`; index avg `0.0006` n `23`; metal avg `0.038` n `18`; unknown avg `0.0208` n `397`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `0.6062` n `228`; crypto_major avg `0.413` n `8`; equity avg `0.1193` n `67`; fx avg `-0.0575` n `6`; index avg `0.0441` n `23`; metal avg `-0.0677` n `18`; unknown avg `0.0998` n `397`
- 24h: commodity avg `0.334` n `12`; crypto_alt avg `-0.2911` n `228`; crypto_major avg `-0.8966` n `8`; equity avg `-0.4049` n `67`; fx avg `-0.076` n `6`; index avg `0.0049` n `23`; metal avg `-0.097` n `18`; unknown avg `0.2548` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
