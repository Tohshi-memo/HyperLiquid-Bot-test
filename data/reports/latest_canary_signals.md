# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T13:37:37.507146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.0124` n `229`; crypto_major avg `0.0202` n `8`; equity avg `0.2468` n `91`; fx avg `-0.008` n `6`; index avg `0.0906` n `25`; metal avg `0.0243` n `20`; unknown avg `0.1672` n `765`
- 1h: commodity avg `-0.2922` n `12`; crypto_alt avg `-0.1793` n `229`; crypto_major avg `-0.0621` n `8`; equity avg `0.2917` n `91`; fx avg `-0.0299` n `6`; index avg `0.0964` n `25`; metal avg `0.0624` n `20`; unknown avg `0.1215` n `765`
- 4h: commodity avg `-0.2074` n `12`; crypto_alt avg `-0.0289` n `229`; crypto_major avg `-0.2036` n `8`; equity avg `0.7425` n `91`; fx avg `-0.0391` n `6`; index avg `0.2725` n `25`; metal avg `0.2086` n `20`; unknown avg `0.2464` n `764`
- 24h: commodity avg `-0.569` n `12`; crypto_alt avg `1.2111` n `229`; crypto_major avg `0.4444` n `8`; equity avg `2.463` n `91`; fx avg `0.1` n `6`; index avg `0.4994` n `25`; metal avg `0.7156` n `20`; unknown avg `0.8435` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0604`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0595`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0585`, n `669`, weak_sample_signal
