# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T21:52:53.324364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.032` n `228`; crypto_major avg `-0.0423` n `8`; equity avg `0.0385` n `88`; fx avg `0.0007` n `6`; index avg `0.0051` n `23`; metal avg `-0.0002` n `20`; unknown avg `4.8645` n `765`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.0253` n `228`; crypto_major avg `-0.2057` n `8`; equity avg `0.0601` n `88`; fx avg `-0.0033` n `6`; index avg `0.0101` n `23`; metal avg `-0.0226` n `20`; unknown avg `4.2296` n `765`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.2831` n `228`; crypto_major avg `0.0758` n `8`; equity avg `0.394` n `88`; fx avg `-0.013` n `6`; index avg `-0.0415` n `23`; metal avg `-0.2765` n `20`; unknown avg `5.4949` n `763`
- 24h: commodity avg `0.1362` n `12`; crypto_alt avg `-2.5365` n `228`; crypto_major avg `-2.7222` n `8`; equity avg `1.1786` n `88`; fx avg `0.1064` n `6`; index avg `0.2486` n `23`; metal avg `-0.0915` n `20`; unknown avg `12.0254` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
