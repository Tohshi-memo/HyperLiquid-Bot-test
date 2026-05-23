# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T07:37:18.818624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.2075` n `228`; crypto_major avg `0.0637` n `8`; equity avg `0.0184` n `67`; fx avg `0.0014` n `6`; index avg `-0.0122` n `23`; metal avg `0.0225` n `18`; unknown avg `-0.0551` n `386`
- 1h: commodity avg `-0.0885` n `12`; crypto_alt avg `-0.2691` n `228`; crypto_major avg `-0.0315` n `8`; equity avg `-0.0599` n `67`; fx avg `0.0083` n `6`; index avg `-0.0196` n `23`; metal avg `0.0685` n `18`; unknown avg `-0.0602` n `386`
- 4h: commodity avg `-0.0869` n `12`; crypto_alt avg `-1.1483` n `228`; crypto_major avg `-0.5368` n `8`; equity avg `-0.1139` n `67`; fx avg `0.0168` n `6`; index avg `-0.1579` n `23`; metal avg `0.0706` n `18`; unknown avg `-0.4942` n `376`
- 24h: commodity avg `-0.4897` n `12`; crypto_alt avg `-4.3918` n `228`; crypto_major avg `-2.7989` n `8`; equity avg `-1.9032` n `67`; fx avg `0.0873` n `6`; index avg `-0.19` n `23`; metal avg `-0.398` n `18`; unknown avg `-2.008` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
