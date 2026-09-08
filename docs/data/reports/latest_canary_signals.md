# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T13:22:26.636507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.2256` n `232`; crypto_major avg `-0.2432` n `8`; equity avg `0.0441` n `134`; fx avg `0.0241` n `6`; index avg `0.0092` n `26`; metal avg `-0.0141` n `20`; unknown avg `1.2408` n `797`
- 1h: commodity avg `-0.2528` n `12`; crypto_alt avg `0.0872` n `232`; crypto_major avg `0.0389` n `8`; equity avg `0.3061` n `134`; fx avg `0.0077` n `6`; index avg `0.0997` n `26`; metal avg `0.1942` n `20`; unknown avg `1.053` n `789`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `-0.2991` n `232`; crypto_major avg `-0.2204` n `8`; equity avg `0.7053` n `134`; fx avg `0.0` n `6`; index avg `0.1342` n `26`; metal avg `0.1297` n `20`; unknown avg `1.0474` n `789`
- 24h: commodity avg `0.0391` n `12`; crypto_alt avg `-1.2221` n `232`; crypto_major avg `-1.8669` n `8`; equity avg `0.2198` n `134`; fx avg `-0.1078` n `6`; index avg `0.0224` n `26`; metal avg `0.2067` n `20`; unknown avg `1.4183` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
