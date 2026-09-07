# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T20:07:28.868024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.3319` n `232`; crypto_major avg `-0.2517` n `8`; equity avg `-0.0053` n `134`; fx avg `-0.0015` n `6`; index avg `0.0006` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.1729` n `764`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `0.2619` n `232`; crypto_major avg `0.1825` n `8`; equity avg `0.0709` n `134`; fx avg `-0.0079` n `6`; index avg `-0.002` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.4722` n `764`
- 4h: commodity avg `-0.0609` n `12`; crypto_alt avg `0.5638` n `232`; crypto_major avg `0.4521` n `8`; equity avg `0.3415` n `134`; fx avg `-0.0166` n `6`; index avg `0.0581` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.1385` n `738`
- 24h: commodity avg `0.1646` n `12`; crypto_alt avg `0.368` n `232`; crypto_major avg `-0.7059` n `8`; equity avg `0.4475` n `134`; fx avg `-0.1281` n `6`; index avg `0.0891` n `26`; metal avg `0.0042` n `20`; unknown avg `7956.4952` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
