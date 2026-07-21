# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T06:52:32.848191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0351` n `230`; crypto_major avg `-0.1062` n `8`; equity avg `0.0484` n `98`; fx avg `0.0125` n `6`; index avg `-0.0002` n `25`; metal avg `0.0611` n `20`; unknown avg `-0.0006` n `771`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `0.1679` n `8`; equity avg `0.1969` n `98`; fx avg `0.0285` n `6`; index avg `0.027` n `25`; metal avg `0.2065` n `20`; unknown avg `-0.0553` n `755`
- 4h: commodity avg `0.0186` n `12`; crypto_alt avg `1.0246` n `230`; crypto_major avg `0.9201` n `8`; equity avg `1.392` n `98`; fx avg `0.004` n `6`; index avg `0.1696` n `25`; metal avg `0.4828` n `20`; unknown avg `0.1161` n `755`
- 24h: commodity avg `-0.2989` n `12`; crypto_alt avg `3.2562` n `230`; crypto_major avg `3.2452` n `8`; equity avg `1.8707` n `98`; fx avg `-0.0839` n `6`; index avg `0.3759` n `25`; metal avg `0.8272` n `20`; unknown avg `0.2207` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
