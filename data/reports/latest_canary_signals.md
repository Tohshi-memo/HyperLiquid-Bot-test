# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T05:52:30.489967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0728` n `12`; crypto_alt avg `0.1284` n `230`; crypto_major avg `0.1394` n `8`; equity avg `0.1902` n `98`; fx avg `0.0092` n `6`; index avg `0.0227` n `25`; metal avg `0.036` n `20`; unknown avg `0.394` n `771`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `0.3423` n `230`; crypto_major avg `0.3403` n `8`; equity avg `0.2077` n `98`; fx avg `-0.0029` n `6`; index avg `0.0162` n `25`; metal avg `0.1407` n `20`; unknown avg `-0.2886` n `771`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `0.9414` n `230`; crypto_major avg `0.8869` n `8`; equity avg `1.4021` n `98`; fx avg `-0.0418` n `6`; index avg `0.1914` n `25`; metal avg `0.3901` n `20`; unknown avg `0.9047` n `771`
- 24h: commodity avg `-0.3887` n `12`; crypto_alt avg `3.2882` n `230`; crypto_major avg `2.8365` n `8`; equity avg `1.6101` n `98`; fx avg `-0.1176` n `6`; index avg `0.3334` n `25`; metal avg `0.6558` n `20`; unknown avg `0.2684` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `667`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0821`, n `667`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `667`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `667`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `669`, weak_sample_signal
