# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T22:22:27.619671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `0.0032` n `8`; equity avg `-0.046` n `96`; fx avg `0.0025` n `6`; index avg `-0.001` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.9203` n `770`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `0.0354` n `8`; equity avg `0.0226` n `96`; fx avg `0.0015` n `6`; index avg `-0.0059` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.011` n `770`
- 4h: commodity avg `0.022` n `12`; crypto_alt avg `0.2187` n `230`; crypto_major avg `0.3229` n `8`; equity avg `-0.0004` n `96`; fx avg `0.0096` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.2135` n `770`
- 24h: commodity avg `0.3494` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `0.7122` n `8`; equity avg `-0.1743` n `96`; fx avg `-0.0629` n `6`; index avg `0.0375` n `25`; metal avg `-0.0272` n `20`; unknown avg `0.1508` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
