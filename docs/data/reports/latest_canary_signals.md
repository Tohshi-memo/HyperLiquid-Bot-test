# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T01:22:31.296484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0006` n `228`; crypto_major avg `0.1343` n `8`; equity avg `0.1677` n `88`; fx avg `-0.0297` n `6`; index avg `0.0672` n `23`; metal avg `0.2589` n `20`; unknown avg `0.1232` n `765`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.6506` n `228`; crypto_major avg `-0.6062` n `8`; equity avg `-0.209` n `88`; fx avg `0.0036` n `6`; index avg `-0.0596` n `23`; metal avg `-0.4183` n `20`; unknown avg `1.4206` n `765`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.9564` n `228`; crypto_major avg `-1.0779` n `8`; equity avg `-0.3511` n `88`; fx avg `0.0665` n `6`; index avg `-0.1276` n `23`; metal avg `-0.4739` n `20`; unknown avg `0.2687` n `763`
- 24h: commodity avg `-0.2799` n `12`; crypto_alt avg `0.7826` n `228`; crypto_major avg `2.0292` n `8`; equity avg `1.9186` n `88`; fx avg `0.2276` n `6`; index avg `0.2152` n `23`; metal avg `-0.6813` n `20`; unknown avg `2.2093` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
