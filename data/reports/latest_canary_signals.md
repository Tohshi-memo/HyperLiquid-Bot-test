# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T11:22:29.736290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.0645` n `228`; crypto_major avg `0.1422` n `8`; equity avg `0.0224` n `88`; fx avg `-0.0086` n `6`; index avg `0.0206` n `23`; metal avg `0.2308` n `20`; unknown avg `0.0005` n `765`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `0.0519` n `228`; crypto_major avg `-0.2919` n `8`; equity avg `0.182` n `88`; fx avg `0.0019` n `6`; index avg `0.0527` n `23`; metal avg `0.4544` n `20`; unknown avg `0.3008` n `765`
- 4h: commodity avg `-0.1465` n `12`; crypto_alt avg `0.4686` n `228`; crypto_major avg `-0.469` n `8`; equity avg `0.3733` n `88`; fx avg `0.0428` n `6`; index avg `0.0892` n `23`; metal avg `0.5619` n `20`; unknown avg `0.2544` n `765`
- 24h: commodity avg `-0.3622` n `12`; crypto_alt avg `0.2443` n `228`; crypto_major avg `-0.7885` n `8`; equity avg `0.6219` n `88`; fx avg `0.138` n `6`; index avg `0.0324` n `23`; metal avg `-0.4128` n `20`; unknown avg `0.0941` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
