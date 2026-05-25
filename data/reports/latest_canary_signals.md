# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T13:07:17.293633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1422` n `12`; crypto_alt avg `0.0819` n `228`; crypto_major avg `-0.0233` n `8`; equity avg `-0.0312` n `67`; fx avg `-0.0037` n `6`; index avg `0.0164` n `23`; metal avg `-0.0173` n `18`; unknown avg `0.1019` n `405`
- 1h: commodity avg `0.5069` n `12`; crypto_alt avg `0.3124` n `228`; crypto_major avg `0.1233` n `8`; equity avg `-0.0907` n `67`; fx avg `0.0049` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.1722` n `405`
- 4h: commodity avg `0.3788` n `12`; crypto_alt avg `0.1033` n `228`; crypto_major avg `-0.0548` n `8`; equity avg `0.1266` n `67`; fx avg `0.0338` n `6`; index avg `0.0764` n `23`; metal avg `0.0337` n `18`; unknown avg `-0.3719` n `397`
- 24h: commodity avg `0.3267` n `12`; crypto_alt avg `0.8039` n `228`; crypto_major avg `-0.1879` n `8`; equity avg `0.3653` n `67`; fx avg `0.019` n `6`; index avg `0.1409` n `23`; metal avg `0.6556` n `18`; unknown avg `0.1424` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
