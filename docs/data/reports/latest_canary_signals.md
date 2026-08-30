# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T02:22:20.476236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.1225` n `231`; crypto_major avg `0.0763` n `8`; equity avg `0.0228` n `128`; fx avg `-0.0006` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0855` n `793`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `0.0781` n `231`; crypto_major avg `0.0444` n `8`; equity avg `0.0273` n `128`; fx avg `-0.0013` n `6`; index avg `-0.0051` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.2343` n `793`
- 4h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0231` n `231`; crypto_major avg `0.0952` n `8`; equity avg `0.0592` n `128`; fx avg `0.0157` n `6`; index avg `0.0204` n `26`; metal avg `0.0012` n `20`; unknown avg `3.546` n `789`
- 24h: commodity avg `0.0043` n `12`; crypto_alt avg `0.372` n `231`; crypto_major avg `0.9773` n `8`; equity avg `0.4021` n `128`; fx avg `-0.0083` n `6`; index avg `0.0836` n `26`; metal avg `0.0949` n `20`; unknown avg `0.0598` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
