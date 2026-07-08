# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T07:52:32.018297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.185` n `229`; crypto_major avg `0.0363` n `8`; equity avg `0.0159` n `91`; fx avg `-0.0089` n `6`; index avg `0.0023` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.0625` n `763`
- 1h: commodity avg `-0.1403` n `12`; crypto_alt avg `-0.0988` n `229`; crypto_major avg `0.1395` n `8`; equity avg `0.2035` n `91`; fx avg `0.0324` n `6`; index avg `0.0129` n `25`; metal avg `-0.1144` n `20`; unknown avg `-0.0175` n `763`
- 4h: commodity avg `-0.0414` n `12`; crypto_alt avg `-0.2375` n `229`; crypto_major avg `-0.1624` n `8`; equity avg `-0.5583` n `91`; fx avg `-0.0759` n `6`; index avg `-0.2051` n `25`; metal avg `-0.098` n `20`; unknown avg `-0.2249` n `743`
- 24h: commodity avg `0.6104` n `12`; crypto_alt avg `-2.7775` n `229`; crypto_major avg `-2.1588` n `8`; equity avg `-1.5868` n `91`; fx avg `-0.2107` n `6`; index avg `-0.3436` n `25`; metal avg `-0.0672` n `20`; unknown avg `-0.6265` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
