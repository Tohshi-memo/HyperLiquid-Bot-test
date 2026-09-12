# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T03:22:30.517870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.95` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.0323` n `233`; crypto_major avg `-0.1083` n `8`; equity avg `-0.017` n `136`; fx avg `0.0005` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.3631` n `838`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.0905` n `233`; crypto_major avg `-0.0827` n `8`; equity avg `-0.0193` n `136`; fx avg `-0.0045` n `6`; index avg `0.0023` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.2819` n `836`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `0.9725` n `233`; crypto_major avg `0.0953` n `8`; equity avg `0.0714` n `136`; fx avg `-0.0035` n `6`; index avg `0.0183` n `26`; metal avg `-0.0251` n `20`; unknown avg `-0.2956` n `824`
- 24h: commodity avg `-0.7314` n `12`; crypto_alt avg `1.718` n `233`; crypto_major avg `1.5027` n `8`; equity avg `1.2519` n `136`; fx avg `-0.1305` n `6`; index avg `0.3455` n `26`; metal avg `0.3227` n `20`; unknown avg `24.083` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
