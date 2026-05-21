# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T07:07:15.300381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.1891` n `228`; crypto_major avg `0.2603` n `8`; equity avg `-0.121` n `66`; fx avg `-0.0031` n `6`; index avg `-0.0354` n `23`; metal avg `0.1117` n `18`; unknown avg `0.1554` n `385`
- 1h: commodity avg `0.2363` n `12`; crypto_alt avg `0.2272` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `-0.4386` n `66`; fx avg `-0.0272` n `6`; index avg `-0.1855` n `23`; metal avg `-0.3025` n `18`; unknown avg `-0.3245` n `385`
- 4h: commodity avg `0.1886` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `0.0297` n `8`; equity avg `-0.2577` n `66`; fx avg `0.0014` n `6`; index avg `-0.0469` n `23`; metal avg `-0.4238` n `18`; unknown avg `0.0711` n `374`
- 24h: commodity avg `-1.6858` n `12`; crypto_alt avg `2.368` n `228`; crypto_major avg `2.8363` n `8`; equity avg `1.5192` n `66`; fx avg `0.0803` n `6`; index avg `1.3557` n `23`; metal avg `0.207` n `18`; unknown avg `4.7049` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
