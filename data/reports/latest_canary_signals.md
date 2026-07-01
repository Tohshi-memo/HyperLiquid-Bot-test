# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T14:22:32.635281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `0.613` n `228`; crypto_major avg `0.8009` n `8`; equity avg `0.1818` n `88`; fx avg `-0.0118` n `6`; index avg `0.0142` n `23`; metal avg `0.0549` n `20`; unknown avg `0.4265` n `765`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `1.1406` n `228`; crypto_major avg `1.5156` n `8`; equity avg `1.2042` n `88`; fx avg `0.0055` n `6`; index avg `0.0165` n `23`; metal avg `0.7558` n `20`; unknown avg `0.8087` n `765`
- 4h: commodity avg `-0.0773` n `12`; crypto_alt avg `1.3478` n `228`; crypto_major avg `1.548` n `8`; equity avg `0.1308` n `88`; fx avg `-0.0644` n `6`; index avg `-0.0506` n `23`; metal avg `1.337` n `20`; unknown avg `0.5505` n `765`
- 24h: commodity avg `-0.63` n `12`; crypto_alt avg `1.4741` n `228`; crypto_major avg `1.3056` n `8`; equity avg `0.1677` n `88`; fx avg `0.0387` n `6`; index avg `-0.2287` n `23`; metal avg `0.2543` n `20`; unknown avg `0.2597` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
