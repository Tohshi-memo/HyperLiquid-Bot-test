# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T17:37:27.224181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.017` n `233`; crypto_major avg `0.0041` n `8`; equity avg `0.0026` n `136`; fx avg `-0.0006` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0078` n `20`; unknown avg `4.7024` n `838`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `-0.0568` n `233`; crypto_major avg `-0.0383` n `8`; equity avg `-0.046` n `136`; fx avg `-0.0004` n `6`; index avg `-0.0115` n `26`; metal avg `-0.005` n `20`; unknown avg `4.8164` n `796`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `0.3236` n `233`; crypto_major avg `-0.1031` n `8`; equity avg `0.0152` n `136`; fx avg `-0.002` n `6`; index avg `0.0063` n `26`; metal avg `0.0154` n `20`; unknown avg `3.0841` n `790`
- 24h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.525` n `233`; crypto_major avg `-0.5016` n `8`; equity avg `-0.3973` n `136`; fx avg `-0.0149` n `6`; index avg `-0.0231` n `26`; metal avg `-0.0681` n `20`; unknown avg `1.0059` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
