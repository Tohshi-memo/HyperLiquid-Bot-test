# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T23:07:37.941222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.039` n `13`; crypto_alt avg `-0.0798` n `236`; crypto_major avg `-0.0839` n `8`; equity avg `-0.1239` n `151`; fx avg `0.0023` n `6`; index avg `-0.0202` n `26`; metal avg `-0.0636` n `20`; unknown avg `-0.2076` n `1134`
- 1h: commodity avg `-0.0561` n `13`; crypto_alt avg `-0.0422` n `236`; crypto_major avg `0.0123` n `8`; equity avg `-0.7197` n `151`; fx avg `0.0566` n `6`; index avg `-0.0882` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.4352` n `1134`
- 4h: commodity avg `0.0543` n `13`; crypto_alt avg `0.5597` n `236`; crypto_major avg `0.2085` n `8`; equity avg `-0.9912` n `151`; fx avg `0.0523` n `6`; index avg `-0.1006` n `26`; metal avg `0.0167` n `20`; unknown avg `0.9857` n `998`
- 24h: commodity avg `-0.1467` n `13`; crypto_alt avg `-2.0123` n `236`; crypto_major avg `-1.9164` n `8`; equity avg `-5.2644` n `151`; fx avg `-0.1182` n `6`; index avg `-0.6846` n `26`; metal avg `-0.8373` n `20`; unknown avg `1392.314` n `890`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0872`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0867`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0541`, n `666`, weak_sample_signal
