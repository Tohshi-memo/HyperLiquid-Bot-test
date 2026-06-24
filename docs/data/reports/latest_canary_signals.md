# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T14:22:28.995499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3647` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1154` n `12`; crypto_alt avg `-0.247` n `228`; crypto_major avg `-0.3417` n `8`; equity avg `-0.2972` n `86`; fx avg `-0.0175` n `6`; index avg `-0.0178` n `23`; metal avg `0.009` n `20`; unknown avg `-0.0657` n `764`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.0521` n `228`; crypto_major avg `-0.3024` n `8`; equity avg `-1.2485` n `86`; fx avg `-0.0094` n `6`; index avg `-0.0567` n `23`; metal avg `0.3579` n `20`; unknown avg `-0.1105` n `764`
- 4h: commodity avg `-0.3834` n `12`; crypto_alt avg `-1.2121` n `228`; crypto_major avg `-1.4596` n `8`; equity avg `-1.7982` n `86`; fx avg `-0.0473` n `6`; index avg `-0.0949` n `23`; metal avg `-0.7109` n `20`; unknown avg `0.2952` n `764`
- 24h: commodity avg `-0.5011` n `12`; crypto_alt avg `-2.0429` n `228`; crypto_major avg `-1.9698` n `8`; equity avg `1.554` n `86`; fx avg `-0.0189` n `6`; index avg `-0.1385` n `23`; metal avg `-1.4183` n `20`; unknown avg `-0.4591` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
