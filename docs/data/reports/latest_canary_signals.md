# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T10:52:36.730453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `0.038` n `230`; crypto_major avg `-0.0036` n `8`; equity avg `0.0419` n `102`; fx avg `0.0014` n `6`; index avg `0.0165` n `25`; metal avg `0.0283` n `20`; unknown avg `-0.0852` n `774`
- 1h: commodity avg `0.1077` n `12`; crypto_alt avg `-0.038` n `230`; crypto_major avg `-0.2038` n `8`; equity avg `-0.2767` n `102`; fx avg `-0.0155` n `6`; index avg `-0.0631` n `25`; metal avg `-0.051` n `20`; unknown avg `-0.091` n `774`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.2652` n `230`; crypto_major avg `-0.3677` n `8`; equity avg `-0.3396` n `102`; fx avg `-0.0151` n `6`; index avg `-0.0578` n `25`; metal avg `-0.225` n `20`; unknown avg `-0.0764` n `774`
- 24h: commodity avg `-0.4819` n `12`; crypto_alt avg `-3.6468` n `230`; crypto_major avg `-3.8403` n `8`; equity avg `-4.5186` n `102`; fx avg `-0.1873` n `6`; index avg `-0.9499` n `25`; metal avg `-0.698` n `20`; unknown avg `996.6832` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
