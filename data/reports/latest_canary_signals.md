# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T13:29:59.902566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2034` n `12`; crypto_alt avg `-0.1902` n `229`; crypto_major avg `-0.2292` n `8`; equity avg `-0.1635` n `91`; fx avg `-0.0013` n `6`; index avg `-0.0211` n `25`; metal avg `-0.027` n `20`; unknown avg `0.0379` n `763`
- 1h: commodity avg `0.2186` n `12`; crypto_alt avg `-0.6859` n `229`; crypto_major avg `-0.8071` n `8`; equity avg `-0.4156` n `91`; fx avg `0.0185` n `6`; index avg `-0.0599` n `25`; metal avg `-0.1268` n `20`; unknown avg `0.1077` n `763`
- 4h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.0148` n `229`; crypto_major avg `-0.1189` n `8`; equity avg `-0.3965` n `91`; fx avg `-0.0845` n `6`; index avg `-0.0275` n `25`; metal avg `0.275` n `20`; unknown avg `-0.142` n `761`
- 24h: commodity avg `0.3157` n `12`; crypto_alt avg `1.6924` n `229`; crypto_major avg `1.5497` n `8`; equity avg `-1.2987` n `90`; fx avg `-0.1871` n `6`; index avg `-0.3621` n `25`; metal avg `0.1853` n `20`; unknown avg `-0.2269` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
