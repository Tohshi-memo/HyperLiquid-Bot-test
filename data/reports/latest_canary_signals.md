# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T16:22:30.122866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8217` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `0.225` n `229`; crypto_major avg `0.2176` n `8`; equity avg `-0.0486` n `88`; fx avg `0.0065` n `6`; index avg `0.0086` n `25`; metal avg `-0.024` n `20`; unknown avg `0.2127` n `766`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `1.4421` n `229`; crypto_major avg `1.4007` n `8`; equity avg `0.2471` n `88`; fx avg `0.0252` n `6`; index avg `0.0789` n `25`; metal avg `-0.0375` n `20`; unknown avg `1.1761` n `765`
- 4h: commodity avg `0.0852` n `12`; crypto_alt avg `2.4681` n `229`; crypto_major avg `1.6954` n `8`; equity avg `0.7477` n `88`; fx avg `0.0469` n `6`; index avg `0.1313` n `25`; metal avg `-0.1263` n `20`; unknown avg `1.4299` n `765`
- 24h: commodity avg `-0.0491` n `12`; crypto_alt avg `1.3542` n `229`; crypto_major avg `0.8672` n `8`; equity avg `-0.029` n `88`; fx avg `0.2322` n `6`; index avg `0.1078` n `25`; metal avg `-0.3932` n `20`; unknown avg `0.8218` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
