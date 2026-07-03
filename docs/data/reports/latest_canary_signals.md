# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T20:22:27.951055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.1601` n `229`; crypto_major avg `0.1064` n `8`; equity avg `-0.0432` n `88`; fx avg `-0.0029` n `6`; index avg `-0.007` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0135` n `765`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `0.2841` n `229`; crypto_major avg `0.2672` n `8`; equity avg `-0.2075` n `88`; fx avg `-0.0074` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0161` n `20`; unknown avg `0.0202` n `765`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.7783` n `229`; crypto_major avg `0.9416` n `8`; equity avg `-0.0526` n `88`; fx avg `-0.0148` n `6`; index avg `0.0102` n `25`; metal avg `0.0123` n `20`; unknown avg `1.1048` n `765`
- 24h: commodity avg `0.142` n `12`; crypto_alt avg `3.2821` n `229`; crypto_major avg `3.2675` n `8`; equity avg `1.6866` n `88`; fx avg `-0.0765` n `6`; index avg `0.4859` n `25`; metal avg `0.5254` n `20`; unknown avg `8.3854` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
