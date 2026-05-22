# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T08:07:17.328623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0815` n `12`; crypto_alt avg `-0.1085` n `228`; crypto_major avg `-0.0897` n `8`; equity avg `0.0224` n `67`; fx avg `0.0048` n `6`; index avg `0.032` n `23`; metal avg `0.2009` n `18`; unknown avg `-0.1861` n `386`
- 1h: commodity avg `0.1649` n `12`; crypto_alt avg `0.5407` n `228`; crypto_major avg `0.3265` n `8`; equity avg `0.0592` n `67`; fx avg `0.0079` n `6`; index avg `0.0336` n `23`; metal avg `0.0509` n `18`; unknown avg `0.247` n `386`
- 4h: commodity avg `0.5479` n `12`; crypto_alt avg `-0.213` n `228`; crypto_major avg `-0.3499` n `8`; equity avg `-0.043` n `67`; fx avg `0.0039` n `6`; index avg `0.0259` n `23`; metal avg `-0.26` n `18`; unknown avg `-0.1751` n `376`
- 24h: commodity avg `-0.3211` n `12`; crypto_alt avg `1.4359` n `228`; crypto_major avg `-0.4378` n `8`; equity avg `1.4118` n `67`; fx avg `0.1294` n `6`; index avg `0.7216` n `23`; metal avg `0.7164` n `18`; unknown avg `1.5297` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0404`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
