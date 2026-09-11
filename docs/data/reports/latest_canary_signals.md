# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T23:52:26.404539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.1725` n `233`; crypto_major avg `0.1138` n `8`; equity avg `0.0182` n `136`; fx avg `-0.0054` n `6`; index avg `-0.0003` n `26`; metal avg `0.0083` n `20`; unknown avg `-0.1413` n `836`
- 1h: commodity avg `-0.0488` n `12`; crypto_alt avg `0.5207` n `233`; crypto_major avg `0.4124` n `8`; equity avg `0.0402` n `136`; fx avg `-0.0138` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0028` n `20`; unknown avg `1.1724` n `828`
- 4h: commodity avg `-0.1612` n `12`; crypto_alt avg `-0.2711` n `233`; crypto_major avg `-0.3205` n `8`; equity avg `0.0082` n `136`; fx avg `-0.0378` n `6`; index avg `-0.0109` n `26`; metal avg `0.0029` n `20`; unknown avg `3.6553` n `788`
- 24h: commodity avg `-0.8961` n `12`; crypto_alt avg `1.0678` n `233`; crypto_major avg `1.6202` n `8`; equity avg `1.0102` n `136`; fx avg `-0.2168` n `6`; index avg `0.3606` n `26`; metal avg `0.3029` n `20`; unknown avg `1.9849` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
