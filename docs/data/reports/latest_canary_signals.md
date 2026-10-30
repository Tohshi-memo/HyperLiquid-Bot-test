# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T03:07:33.186545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `0.1169` n `238`; crypto_major avg `0.2261` n `8`; equity avg `-0.0215` n `156`; fx avg `-0.0376` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0106` n `20`; unknown avg `1.0616` n `1254`
- 1h: commodity avg `-0.164` n `13`; crypto_alt avg `0.9546` n `238`; crypto_major avg `1.1861` n `8`; equity avg `0.4488` n `156`; fx avg `-0.0122` n `6`; index avg `0.0124` n `27`; metal avg `-0.1091` n `20`; unknown avg `2.802` n `1254`
- 4h: commodity avg `0.1696` n `13`; crypto_alt avg `-1.8015` n `238`; crypto_major avg `-0.773` n `8`; equity avg `-0.3641` n `156`; fx avg `-0.0441` n `6`; index avg `-0.1591` n `27`; metal avg `-0.3032` n `20`; unknown avg `2.5783` n `1238`
- 24h: commodity avg `-0.0295` n `13`; crypto_alt avg `-5.3891` n `238`; crypto_major avg `-1.2637` n `8`; equity avg `-2.9758` n `155`; fx avg `0.151` n `6`; index avg `-0.3347` n `27`; metal avg `-0.7` n `20`; unknown avg `29.6545` n `986`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
