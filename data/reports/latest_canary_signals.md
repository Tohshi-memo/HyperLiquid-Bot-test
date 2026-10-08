# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T19:22:32.294347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `13`; crypto_alt avg `0.2824` n `235`; crypto_major avg `0.3143` n `8`; equity avg `0.2047` n `150`; fx avg `-0.0036` n `6`; index avg `0.0251` n `26`; metal avg `0.0137` n `20`; unknown avg `0.2407` n `1077`
- 1h: commodity avg `-0.2118` n `13`; crypto_alt avg `0.6624` n `235`; crypto_major avg `0.5197` n `8`; equity avg `-0.1652` n `150`; fx avg `0.0019` n `6`; index avg `-0.0031` n `26`; metal avg `0.0362` n `20`; unknown avg `2.6829` n `1075`
- 4h: commodity avg `-0.1178` n `13`; crypto_alt avg `-0.7854` n `235`; crypto_major avg `-0.5588` n `8`; equity avg `-1.1351` n `150`; fx avg `-0.0251` n `6`; index avg `-0.1267` n `26`; metal avg `0.0874` n `20`; unknown avg `0.8625` n `1069`
- 24h: commodity avg `0.8144` n `13`; crypto_alt avg `-3.3455` n `235`; crypto_major avg `-4.2267` n `8`; equity avg `-2.9609` n `150`; fx avg `0.0558` n `6`; index avg `-0.3839` n `26`; metal avg `-0.0027` n `20`; unknown avg `23.422` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
