# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T12:37:26.789714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.0053` n `8`; equity avg `-0.0745` n `98`; fx avg `-0.008` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0561` n `20`; unknown avg `-0.0332` n `771`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `0.0956` n `230`; crypto_major avg `0.1169` n `8`; equity avg `-0.0388` n `98`; fx avg `-0.0014` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0493` n `20`; unknown avg `-0.0304` n `771`
- 4h: commodity avg `0.3653` n `12`; crypto_alt avg `0.0136` n `230`; crypto_major avg `-0.0285` n `8`; equity avg `-0.2443` n `98`; fx avg `-0.025` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0649` n `20`; unknown avg `0.0024` n `771`
- 24h: commodity avg `0.3534` n `12`; crypto_alt avg `1.7629` n `230`; crypto_major avg `2.0838` n `8`; equity avg `1.0387` n `98`; fx avg `-0.0737` n `6`; index avg `0.1449` n `25`; metal avg `0.6009` n `20`; unknown avg `0.0756` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0606`, n `666`, weak_sample_signal
