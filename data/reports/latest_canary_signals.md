# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T21:07:26.272618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1152` n `233`; crypto_major avg `0.1786` n `8`; equity avg `0.0409` n `136`; fx avg `0.0039` n `6`; index avg `-0.0092` n `26`; metal avg `0.0149` n `20`; unknown avg `0.0556` n `822`
- 1h: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.2833` n `233`; crypto_major avg `-0.2002` n `8`; equity avg `0.0136` n `136`; fx avg `-0.0162` n `6`; index avg `-0.0131` n `26`; metal avg `0.0001` n `20`; unknown avg `0.5346` n `802`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `-1.1175` n `233`; crypto_major avg `-0.7894` n `8`; equity avg `-0.2884` n `136`; fx avg `-0.0071` n `6`; index avg `-0.0531` n `26`; metal avg `-0.04` n `20`; unknown avg `0.0194` n `726`
- 24h: commodity avg `-0.7781` n `12`; crypto_alt avg `0.0882` n `233`; crypto_major avg `0.9898` n `8`; equity avg `0.6515` n `136`; fx avg `-0.1705` n `6`; index avg `0.2834` n `26`; metal avg `0.2606` n `20`; unknown avg `1.3407` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
