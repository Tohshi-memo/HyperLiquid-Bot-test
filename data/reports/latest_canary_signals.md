# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T01:52:26.252795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1383` n `12`; crypto_alt avg `0.165` n `228`; crypto_major avg `0.1617` n `8`; equity avg `-0.1045` n `74`; fx avg `0.0166` n `6`; index avg `-0.0429` n `23`; metal avg `-0.2141` n `18`; unknown avg `0.0565` n `547`
- 1h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.1914` n `228`; crypto_major avg `0.1849` n `8`; equity avg `0.0704` n `74`; fx avg `0.049` n `6`; index avg `0.0182` n `23`; metal avg `-0.201` n `18`; unknown avg `-0.004` n `547`
- 4h: commodity avg `0.065` n `12`; crypto_alt avg `0.1041` n `228`; crypto_major avg `-0.3111` n `8`; equity avg `-0.049` n `74`; fx avg `0.0422` n `6`; index avg `-0.09` n `23`; metal avg `-1.0387` n `18`; unknown avg `-0.3821` n `547`
- 24h: commodity avg `-0.4975` n `12`; crypto_alt avg `0.061` n `228`; crypto_major avg `-2.0317` n `8`; equity avg `-2.0653` n `74`; fx avg `0.1181` n `6`; index avg `-0.936` n `23`; metal avg `-2.5469` n `18`; unknown avg `-0.3577` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0378`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.037`, n `668`, weak_sample_signal
