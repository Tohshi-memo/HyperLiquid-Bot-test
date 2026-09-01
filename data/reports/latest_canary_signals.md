# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T11:22:26.306230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `0.0924` n `232`; crypto_major avg `0.0678` n `8`; equity avg `-0.0209` n `130`; fx avg `0.0034` n `6`; index avg `0.0027` n `26`; metal avg `-0.0319` n `20`; unknown avg `-0.1093` n `792`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.2807` n `232`; crypto_major avg `0.1008` n `8`; equity avg `-0.1914` n `130`; fx avg `0.0091` n `6`; index avg `-0.0363` n `26`; metal avg `-0.1136` n `20`; unknown avg `-0.1183` n `790`
- 4h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.8837` n `232`; crypto_major avg `-0.7092` n `8`; equity avg `-1.4819` n `130`; fx avg `0.0125` n `6`; index avg `-0.3069` n `26`; metal avg `-0.61` n `20`; unknown avg `-0.1757` n `790`
- 24h: commodity avg `0.2093` n `12`; crypto_alt avg `0.548` n `232`; crypto_major avg `-0.1523` n `8`; equity avg `-0.7078` n `130`; fx avg `0.1171` n `6`; index avg `-0.2721` n `26`; metal avg `-0.8721` n `20`; unknown avg `-0.1042` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0362`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0293`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0289`, n `668`, weak_sample_signal
