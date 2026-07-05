# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T20:22:31.435504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.0413` n `229`; crypto_major avg `0.0038` n `8`; equity avg `0.0005` n `88`; fx avg `0.0121` n `6`; index avg `-0.0045` n `25`; metal avg `0.0106` n `20`; unknown avg `-0.0148` n `765`
- 1h: commodity avg `-0.0338` n `12`; crypto_alt avg `-0.0644` n `229`; crypto_major avg `0.0951` n `8`; equity avg `0.0435` n `88`; fx avg `0.0227` n `6`; index avg `-0.0013` n `25`; metal avg `0.0191` n `20`; unknown avg `0.121` n `765`
- 4h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.5057` n `229`; crypto_major avg `0.3629` n `8`; equity avg `0.1584` n `88`; fx avg `0.0303` n `6`; index avg `0.0119` n `25`; metal avg `0.0205` n `20`; unknown avg `0.8056` n `765`
- 24h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.7715` n `229`; crypto_major avg `-0.1685` n `8`; equity avg `0.3919` n `88`; fx avg `-0.0388` n `6`; index avg `0.0811` n `25`; metal avg `0.0631` n `20`; unknown avg `1.1186` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
