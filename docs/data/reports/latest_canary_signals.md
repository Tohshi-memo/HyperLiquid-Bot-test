# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T00:07:15.149861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1097` n `12`; crypto_alt avg `0.0748` n `228`; crypto_major avg `0.0952` n `8`; equity avg `0.0097` n `66`; fx avg `0.0002` n `6`; index avg `-0.0636` n `23`; metal avg `-0.1023` n `18`; unknown avg `-0.0036` n `384`
- 1h: commodity avg `0.3267` n `12`; crypto_alt avg `0.1465` n `228`; crypto_major avg `0.3624` n `8`; equity avg `-0.0635` n `66`; fx avg `0.0327` n `6`; index avg `-0.0405` n `23`; metal avg `-0.0056` n `18`; unknown avg `2.3244` n `384`
- 4h: commodity avg `0.1476` n `12`; crypto_alt avg `-0.1222` n `228`; crypto_major avg `0.4798` n `8`; equity avg `-0.2466` n `66`; fx avg `0.0314` n `6`; index avg `-0.2628` n `23`; metal avg `-0.2061` n `18`; unknown avg `2.2908` n `384`
- 24h: commodity avg `-2.1646` n `12`; crypto_alt avg `2.8491` n `228`; crypto_major avg `2.8288` n `8`; equity avg `1.7222` n `66`; fx avg `-0.0724` n `6`; index avg `1.064` n `23`; metal avg `1.3551` n `18`; unknown avg `3.7508` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
