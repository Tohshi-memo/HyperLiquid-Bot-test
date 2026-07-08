# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T09:52:25.672055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `-0.0399` n `229`; crypto_major avg `-0.068` n `8`; equity avg `0.1012` n `91`; fx avg `0.0045` n `6`; index avg `0.0086` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.0751` n `763`
- 1h: commodity avg `0.0529` n `12`; crypto_alt avg `-0.3681` n `229`; crypto_major avg `-0.1347` n `8`; equity avg `-0.3491` n `91`; fx avg `-0.0461` n `6`; index avg `-0.0987` n `25`; metal avg `-0.2417` n `20`; unknown avg `-0.1128` n `763`
- 4h: commodity avg `0.555` n `12`; crypto_alt avg `-1.1385` n `229`; crypto_major avg `-0.8129` n `8`; equity avg `-1.7966` n `91`; fx avg `0.0092` n `6`; index avg `-0.3973` n `25`; metal avg `-1.135` n `20`; unknown avg `-0.4711` n `745`
- 24h: commodity avg `1.4142` n `12`; crypto_alt avg `-3.8452` n `229`; crypto_major avg `-3.1932` n `8`; equity avg `-3.1937` n `91`; fx avg `-0.1485` n `6`; index avg `-0.7329` n `25`; metal avg `-1.2234` n `20`; unknown avg `-0.8613` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
