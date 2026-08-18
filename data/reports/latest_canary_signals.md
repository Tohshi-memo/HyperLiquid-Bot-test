# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T04:52:30.010206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0535` n `230`; crypto_major avg `-0.0384` n `8`; equity avg `-0.0454` n `114`; fx avg `0.0047` n `6`; index avg `-0.0106` n `25`; metal avg `0.0294` n `20`; unknown avg `0.0741` n `793`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `0.1553` n `230`; crypto_major avg `0.1005` n `8`; equity avg `0.0523` n `114`; fx avg `0.0241` n `6`; index avg `0.0119` n `25`; metal avg `0.0243` n `20`; unknown avg `0.2297` n `793`
- 4h: commodity avg `0.0795` n `12`; crypto_alt avg `-0.9851` n `230`; crypto_major avg `-0.4312` n `8`; equity avg `-1.5601` n `114`; fx avg `0.0159` n `6`; index avg `-0.294` n `25`; metal avg `-0.2902` n `20`; unknown avg `0.2689` n `793`
- 24h: commodity avg `0.6558` n `12`; crypto_alt avg `-1.4437` n `230`; crypto_major avg `0.0479` n `8`; equity avg `-0.9833` n `114`; fx avg `0.0154` n `6`; index avg `-0.2828` n `25`; metal avg `-0.1716` n `20`; unknown avg `0.089` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
