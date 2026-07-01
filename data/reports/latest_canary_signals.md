# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T09:07:36.689667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0658` n `12`; crypto_alt avg `0.4503` n `228`; crypto_major avg `0.4318` n `8`; equity avg `0.0315` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0082` n `23`; metal avg `-0.0646` n `20`; unknown avg `0.3394` n `765`
- 1h: commodity avg `-0.2542` n `12`; crypto_alt avg `0.4289` n `228`; crypto_major avg `0.2388` n `8`; equity avg `0.0608` n `88`; fx avg `-0.0128` n `6`; index avg `0.0037` n `23`; metal avg `0.0186` n `20`; unknown avg `0.3493` n `765`
- 4h: commodity avg `-0.3962` n `12`; crypto_alt avg `-0.6925` n `228`; crypto_major avg `-0.9145` n `8`; equity avg `-0.2903` n `88`; fx avg `0.0085` n `6`; index avg `-0.0787` n `23`; metal avg `-0.0457` n `20`; unknown avg `-0.133` n `743`
- 24h: commodity avg `-0.4573` n `12`; crypto_alt avg `-0.0814` n `228`; crypto_major avg `-0.1966` n `8`; equity avg `0.556` n `88`; fx avg `0.1021` n `6`; index avg `0.0073` n `23`; metal avg `-0.7193` n `20`; unknown avg `0.1907` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
