# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T04:52:16.645684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `0.0773` n `228`; crypto_major avg `0.0906` n `8`; equity avg `0.0995` n `66`; fx avg `-0.0034` n `6`; index avg `0.0286` n `23`; metal avg `0.0287` n `18`; unknown avg `0.6291` n `384`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.0184` n `228`; crypto_major avg `-0.0552` n `8`; equity avg `0.1822` n `66`; fx avg `0.001` n `6`; index avg `0.094` n `23`; metal avg `0.1352` n `18`; unknown avg `0.5337` n `384`
- 4h: commodity avg `-0.1319` n `12`; crypto_alt avg `0.3226` n `228`; crypto_major avg `0.34` n `8`; equity avg `0.5005` n `66`; fx avg `0.0636` n `6`; index avg `0.354` n `23`; metal avg `-0.273` n `18`; unknown avg `1.202` n `384`
- 24h: commodity avg `-2.2541` n `12`; crypto_alt avg `3.6445` n `228`; crypto_major avg `3.8557` n `8`; equity avg `2.6555` n `66`; fx avg `0.0139` n `6`; index avg `1.8543` n `23`; metal avg `1.5491` n `18`; unknown avg `6.1411` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
