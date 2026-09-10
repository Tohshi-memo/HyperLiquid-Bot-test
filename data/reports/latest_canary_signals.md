# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T17:22:32.863491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.1137` n `233`; crypto_major avg `0.1975` n `8`; equity avg `-0.0561` n `135`; fx avg `-0.0072` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.1422` n `796`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.7745` n `233`; crypto_major avg `0.5976` n `8`; equity avg `0.0525` n `135`; fx avg `-0.0128` n `6`; index avg `0.0228` n `26`; metal avg `0.0049` n `20`; unknown avg `1.161` n `788`
- 4h: commodity avg `0.3122` n `12`; crypto_alt avg `0.3719` n `233`; crypto_major avg `0.2835` n `8`; equity avg `0.57` n `135`; fx avg `0.0383` n `6`; index avg `0.0031` n `26`; metal avg `-0.0893` n `20`; unknown avg `-0.1487` n `760`
- 24h: commodity avg `0.968` n `12`; crypto_alt avg `-4.5299` n `233`; crypto_major avg `-3.5472` n `8`; equity avg `-1.8983` n `135`; fx avg `0.0828` n `6`; index avg `-0.2926` n `26`; metal avg `-1.2506` n `20`; unknown avg `-0.8135` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
