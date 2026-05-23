# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T07:39:54.052209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `-0.2852` n `228`; crypto_major avg `-0.0265` n `8`; equity avg `0.0167` n `67`; fx avg `0.0014` n `6`; index avg `-0.014` n `23`; metal avg `0.024` n `18`; unknown avg `0.9312` n `386`
- 1h: commodity avg `-0.0803` n `12`; crypto_alt avg `-0.3464` n `228`; crypto_major avg `-0.1216` n `8`; equity avg `-0.0616` n `67`; fx avg `0.0083` n `6`; index avg `-0.0214` n `23`; metal avg `0.07` n `18`; unknown avg `0.9292` n `386`
- 4h: commodity avg `-0.0788` n `12`; crypto_alt avg `-1.2239` n `228`; crypto_major avg `-0.6264` n `8`; equity avg `-0.1157` n `67`; fx avg `0.0168` n `6`; index avg `-0.1597` n `23`; metal avg `0.072` n `18`; unknown avg `0.515` n `376`
- 24h: commodity avg `-0.4818` n `12`; crypto_alt avg `-4.4628` n `228`; crypto_major avg `-2.8859` n `8`; equity avg `-1.9044` n `67`; fx avg `0.0873` n `6`; index avg `-0.1918` n `23`; metal avg `-0.3965` n `18`; unknown avg `-1.045` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
