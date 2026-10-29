# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T17:52:33.281452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `13`; crypto_alt avg `-0.781` n `238`; crypto_major avg `-0.6689` n `8`; equity avg `-0.2887` n `156`; fx avg `-0.0117` n `6`; index avg `-0.0328` n `27`; metal avg `-0.0691` n `20`; unknown avg `0.0925` n `1238`
- 1h: commodity avg `0.0994` n `13`; crypto_alt avg `-1.0716` n `238`; crypto_major avg `-0.9692` n `8`; equity avg `-0.5791` n `156`; fx avg `-0.0019` n `6`; index avg `-0.0627` n `27`; metal avg `-0.0689` n `20`; unknown avg `8.1295` n `1232`
- 4h: commodity avg `0.3598` n `13`; crypto_alt avg `0.363` n `238`; crypto_major avg `0.5876` n `8`; equity avg `-0.0721` n `156`; fx avg `0.1464` n `6`; index avg `0.0152` n `27`; metal avg `-0.0249` n `20`; unknown avg `0.6522` n `1132`
- 24h: commodity avg `-0.5041` n `13`; crypto_alt avg `0.1581` n `238`; crypto_major avg `1.5054` n `8`; equity avg `-1.2001` n `155`; fx avg `0.0299` n `6`; index avg `-0.1889` n `27`; metal avg `-0.5254` n `20`; unknown avg `7.8848` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
