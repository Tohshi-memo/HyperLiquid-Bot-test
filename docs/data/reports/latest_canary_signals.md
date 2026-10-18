# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T02:52:28.729382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.0276` n `237`; crypto_major avg `0.0274` n `8`; equity avg `-0.0176` n `151`; fx avg `-0.0013` n `6`; index avg `-0.0014` n `26`; metal avg `0.008` n `20`; unknown avg `-0.0755` n `1193`
- 1h: commodity avg `0.0202` n `13`; crypto_alt avg `-0.3308` n `237`; crypto_major avg `0.036` n `8`; equity avg `-0.1329` n `151`; fx avg `-0.006` n `6`; index avg `-0.0256` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.2163` n `1191`
- 4h: commodity avg `0.0242` n `13`; crypto_alt avg `-0.1971` n `236`; crypto_major avg `0.4906` n `8`; equity avg `0.2039` n `151`; fx avg `-0.0057` n `6`; index avg `0.0309` n `26`; metal avg `0.0287` n `20`; unknown avg `-0.0271` n `1185`
- 24h: commodity avg `-0.0983` n `13`; crypto_alt avg `-2.2384` n `236`; crypto_major avg `-0.4135` n `8`; equity avg `-0.9219` n `151`; fx avg `-0.0386` n `6`; index avg `-0.1111` n `26`; metal avg `-0.0587` n `20`; unknown avg `3.5703` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.163`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1364`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0758`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
