# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T07:07:31.326345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `12`; crypto_alt avg `-0.0571` n `228`; crypto_major avg `-0.0308` n `8`; equity avg `0.1164` n `67`; fx avg `0.0164` n `6`; index avg `0.0324` n `23`; metal avg `-0.0308` n `18`; unknown avg `-0.206` n `418`
- 1h: commodity avg `-0.3183` n `12`; crypto_alt avg `0.1498` n `228`; crypto_major avg `0.2058` n `8`; equity avg `0.2482` n `67`; fx avg `0.0235` n `6`; index avg `-0.026` n `23`; metal avg `-0.2739` n `18`; unknown avg `0.1345` n `418`
- 4h: commodity avg `-0.3744` n `12`; crypto_alt avg `0.206` n `228`; crypto_major avg `0.2376` n `8`; equity avg `-0.1811` n `67`; fx avg `0.0469` n `6`; index avg `-0.2591` n `23`; metal avg `-0.993` n `18`; unknown avg `0.0929` n `400`
- 24h: commodity avg `-0.8654` n `12`; crypto_alt avg `-0.7537` n `228`; crypto_major avg `-0.0664` n `8`; equity avg `0.6321` n `67`; fx avg `0.0319` n `6`; index avg `0.7256` n `23`; metal avg `-0.8395` n `18`; unknown avg `0.7446` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
