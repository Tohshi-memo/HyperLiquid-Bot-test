# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T08:07:14.831669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1271` n `12`; crypto_alt avg `0.1719` n `228`; crypto_major avg `0.138` n `8`; equity avg `0.2377` n `66`; fx avg `0.0051` n `6`; index avg `0.0385` n `23`; metal avg `0.1387` n `18`; unknown avg `-0.1426` n `384`
- 1h: commodity avg `-0.097` n `12`; crypto_alt avg `0.0799` n `228`; crypto_major avg `0.0127` n `8`; equity avg `0.1682` n `66`; fx avg `0.007` n `6`; index avg `0.0699` n `23`; metal avg `0.0696` n `18`; unknown avg `-0.0687` n `384`
- 4h: commodity avg `-0.2245` n `12`; crypto_alt avg `1.1185` n `228`; crypto_major avg `0.8142` n `8`; equity avg `0.7196` n `66`; fx avg `-0.0422` n `6`; index avg `0.2647` n `23`; metal avg `0.7995` n `18`; unknown avg `0.2832` n `374`
- 24h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.0516` n `228`; crypto_major avg `-0.1881` n `8`; equity avg `0.4819` n `66`; fx avg `-0.1618` n `6`; index avg `-0.4588` n `23`; metal avg `-1.1503` n `18`; unknown avg `0.1012` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
