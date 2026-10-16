# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T06:07:37.350853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `13`; crypto_alt avg `-0.1956` n `236`; crypto_major avg `-0.2161` n `8`; equity avg `-0.2626` n `151`; fx avg `-0.0089` n `6`; index avg `-0.0582` n `26`; metal avg `-0.0494` n `20`; unknown avg `-0.0572` n `1110`
- 1h: commodity avg `-0.078` n `13`; crypto_alt avg `-0.1227` n `236`; crypto_major avg `-0.275` n `8`; equity avg `-0.4702` n `151`; fx avg `-0.0735` n `6`; index avg `-0.0793` n `26`; metal avg `-0.05` n `20`; unknown avg `-0.0489` n `1110`
- 4h: commodity avg `-0.099` n `13`; crypto_alt avg `0.512` n `236`; crypto_major avg `0.23` n `8`; equity avg `0.3883` n `151`; fx avg `-0.0645` n `6`; index avg `0.0584` n `26`; metal avg `0.1528` n `20`; unknown avg `0.027` n `1102`
- 24h: commodity avg `-0.0617` n `13`; crypto_alt avg `4.6139` n `236`; crypto_major avg `2.3604` n `8`; equity avg `2.2551` n `151`; fx avg `-0.0398` n `6`; index avg `0.3734` n `26`; metal avg `0.478` n `20`; unknown avg `26.0143` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `666`, weak_sample_signal
