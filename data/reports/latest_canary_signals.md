# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T05:21:24.405386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.0582` n `232`; crypto_major avg `-0.1103` n `8`; equity avg `-0.1077` n `130`; fx avg `0.0059` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0456` n `20`; unknown avg `-0.1408` n `792`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `-0.0648` n `232`; crypto_major avg `-0.1225` n `8`; equity avg `-0.144` n `130`; fx avg `-0.0178` n `6`; index avg `-0.03` n `26`; metal avg `-0.0495` n `20`; unknown avg `-0.3924` n `790`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `0.3326` n `232`; crypto_major avg `0.1705` n `8`; equity avg `-0.0977` n `130`; fx avg `-0.008` n `6`; index avg `-0.0416` n `26`; metal avg `-0.1487` n `20`; unknown avg `-0.2204` n `790`
- 24h: commodity avg `0.3432` n `12`; crypto_alt avg `1.5084` n `232`; crypto_major avg `1.3154` n `8`; equity avg `0.6473` n `130`; fx avg `-0.0093` n `6`; index avg `-0.0113` n `26`; metal avg `-0.1609` n `20`; unknown avg `0.3198` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
