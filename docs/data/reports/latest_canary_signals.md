# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T02:22:28.360339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0894` n `12`; crypto_alt avg `-0.2491` n `230`; crypto_major avg `-0.292` n `8`; equity avg `-0.2841` n `102`; fx avg `-0.0159` n `6`; index avg `-0.0337` n `25`; metal avg `-0.0376` n `20`; unknown avg `0.0328` n `779`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `-0.7174` n `230`; crypto_major avg `-0.8416` n `8`; equity avg `-1.0043` n `102`; fx avg `-0.035` n `6`; index avg `-0.2165` n `25`; metal avg `-0.0344` n `20`; unknown avg `1.6809` n `779`
- 4h: commodity avg `-0.306` n `12`; crypto_alt avg `-0.2759` n `230`; crypto_major avg `-0.7129` n `8`; equity avg `0.3171` n `102`; fx avg `0.1683` n `6`; index avg `0.1953` n `25`; metal avg `-0.2467` n `20`; unknown avg `0.5786` n `779`
- 24h: commodity avg `-0.1708` n `12`; crypto_alt avg `-0.2512` n `230`; crypto_major avg `0.3741` n `8`; equity avg `6.6611` n `102`; fx avg `-0.2137` n `6`; index avg `0.85` n `25`; metal avg `0.2796` n `20`; unknown avg `0.0612` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
