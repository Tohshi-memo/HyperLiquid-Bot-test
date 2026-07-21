# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T08:22:28.698366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `12`; crypto_alt avg `0.0287` n `230`; crypto_major avg `0.1371` n `8`; equity avg `0.0774` n `98`; fx avg `0.0113` n `6`; index avg `0.0154` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0012` n `771`
- 1h: commodity avg `-0.203` n `12`; crypto_alt avg `0.0536` n `230`; crypto_major avg `0.2789` n `8`; equity avg `0.3075` n `98`; fx avg `0.0346` n `6`; index avg `0.0281` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.0538` n `771`
- 4h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.4557` n `230`; crypto_major avg `0.7228` n `8`; equity avg `0.7029` n `98`; fx avg `0.0761` n `6`; index avg `0.0373` n `25`; metal avg `0.352` n `20`; unknown avg `0.0831` n `755`
- 24h: commodity avg `0.1269` n `12`; crypto_alt avg `2.522` n `230`; crypto_major avg `2.8666` n `8`; equity avg `1.768` n `98`; fx avg `-0.0689` n `6`; index avg `0.2976` n `25`; metal avg `0.5547` n `20`; unknown avg `0.21` n `753`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0743`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
