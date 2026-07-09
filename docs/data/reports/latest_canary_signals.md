# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T20:52:25.639104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.0403` n `229`; crypto_major avg `-0.1054` n `8`; equity avg `0.0051` n `91`; fx avg `-0.0025` n `6`; index avg `-0.0184` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0212` n `765`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.017` n `229`; crypto_major avg `0.041` n `8`; equity avg `0.0921` n `91`; fx avg `-0.0074` n `6`; index avg `-0.0057` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.1497` n `765`
- 4h: commodity avg `-0.0414` n `12`; crypto_alt avg `0.5796` n `229`; crypto_major avg `0.5553` n `8`; equity avg `-0.1837` n `91`; fx avg `-0.0406` n `6`; index avg `0.0296` n `25`; metal avg `-0.2956` n `20`; unknown avg `0.1191` n `765`
- 24h: commodity avg `-1.1893` n `12`; crypto_alt avg `1.4629` n `229`; crypto_major avg `0.7974` n `8`; equity avg `1.7728` n `91`; fx avg `0.034` n `6`; index avg `0.3577` n `25`; metal avg `0.6855` n `20`; unknown avg `-0.0269` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
