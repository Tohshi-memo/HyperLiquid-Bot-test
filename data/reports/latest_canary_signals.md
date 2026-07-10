# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T12:37:28.446001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0655` n `12`; crypto_alt avg `-0.0112` n `229`; crypto_major avg `-0.0404` n `8`; equity avg `0.0355` n `91`; fx avg `0.0035` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0356` n `20`; unknown avg `-0.0361` n `766`
- 1h: commodity avg `-0.097` n `12`; crypto_alt avg `0.0128` n `229`; crypto_major avg `0.0266` n `8`; equity avg `-0.0063` n `91`; fx avg `-0.0058` n `6`; index avg `-0.0042` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.0907` n `766`
- 4h: commodity avg `0.0232` n `12`; crypto_alt avg `0.1548` n `229`; crypto_major avg `0.0764` n `8`; equity avg `0.6059` n `91`; fx avg `0.004` n `6`; index avg `0.0934` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.0549` n `765`
- 24h: commodity avg `-0.9067` n `12`; crypto_alt avg `1.0433` n `229`; crypto_major avg `1.721` n `8`; equity avg `0.2976` n `91`; fx avg `-0.1105` n `6`; index avg `0.087` n `25`; metal avg `-0.0786` n `20`; unknown avg `-0.0597` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
