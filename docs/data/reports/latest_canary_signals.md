# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T23:07:25.413536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.085` n `230`; crypto_major avg `-0.0867` n `8`; equity avg `0.0492` n `113`; fx avg `0.0` n `6`; index avg `-0.0061` n `25`; metal avg `0.0156` n `20`; unknown avg `0.0365` n `786`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.0348` n `230`; crypto_major avg `-0.1029` n `8`; equity avg `0.0675` n `113`; fx avg `0.007` n `6`; index avg `-0.0111` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.1132` n `786`
- 4h: commodity avg `-0.0876` n `12`; crypto_alt avg `-0.9541` n `230`; crypto_major avg `-0.6222` n `8`; equity avg `-0.2562` n `113`; fx avg `-0.0029` n `6`; index avg `-0.0183` n `25`; metal avg `-0.1198` n `20`; unknown avg `-0.4102` n `786`
- 24h: commodity avg `-0.0278` n `12`; crypto_alt avg `-1.6063` n `230`; crypto_major avg `-0.5949` n `8`; equity avg `2.6761` n `113`; fx avg `0.0234` n `6`; index avg `0.3945` n `25`; metal avg `0.1143` n `20`; unknown avg `-0.0875` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2355`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
