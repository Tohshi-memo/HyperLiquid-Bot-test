# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T00:07:21.955799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0915` n `12`; crypto_alt avg `0.0843` n `228`; crypto_major avg `0.0269` n `8`; equity avg `0.0092` n `74`; fx avg `-0.0014` n `6`; index avg `0.0235` n `23`; metal avg `0.0282` n `18`; unknown avg `-0.0799` n `515`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `0.2686` n `228`; crypto_major avg `0.1846` n `8`; equity avg `0.2863` n `74`; fx avg `-0.0035` n `6`; index avg `0.0118` n `23`; metal avg `0.0641` n `18`; unknown avg `-0.0182` n `515`
- 4h: commodity avg `0.0737` n `12`; crypto_alt avg `1.1842` n `228`; crypto_major avg `0.8422` n `8`; equity avg `0.3916` n `74`; fx avg `-0.0408` n `6`; index avg `0.0841` n `23`; metal avg `0.0722` n `18`; unknown avg `0.0049` n `515`
- 24h: commodity avg `0.1961` n `12`; crypto_alt avg `-1.5789` n `228`; crypto_major avg `-1.7926` n `8`; equity avg `-0.34` n `74`; fx avg `0.0135` n `6`; index avg `-0.1098` n `23`; metal avg `-0.3097` n `18`; unknown avg `0.9367` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
