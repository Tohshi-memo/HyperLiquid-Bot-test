# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:22:29.911058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `0.0134` n `230`; crypto_major avg `0.0583` n `8`; equity avg `0.2978` n `120`; fx avg `0.0163` n `6`; index avg `0.021` n `25`; metal avg `0.0197` n `20`; unknown avg `-0.0022` n `789`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.0679` n `230`; crypto_major avg `0.1206` n `8`; equity avg `0.9527` n `120`; fx avg `0.0092` n `6`; index avg `0.1555` n `25`; metal avg `0.0063` n `20`; unknown avg `0.0208` n `789`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.0151` n `230`; crypto_major avg `0.0557` n `8`; equity avg `0.4055` n `120`; fx avg `0.0124` n `6`; index avg `0.1008` n `25`; metal avg `-0.0222` n `20`; unknown avg `-0.0672` n `757`
- 24h: commodity avg `0.3948` n `12`; crypto_alt avg `0.2278` n `230`; crypto_major avg `-0.0793` n `8`; equity avg `-2.5612` n `120`; fx avg `-0.1418` n `6`; index avg `-0.3563` n `25`; metal avg `-0.6263` n `20`; unknown avg `-0.2789` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
