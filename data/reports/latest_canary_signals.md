# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T18:37:29.377235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `13`; crypto_alt avg `-0.4489` n `238`; crypto_major avg `-0.2718` n `8`; equity avg `-0.1761` n `156`; fx avg `-0.0029` n `6`; index avg `-0.0111` n `27`; metal avg `0.0045` n `20`; unknown avg `-0.0518` n `1238`
- 1h: commodity avg `0.0225` n `13`; crypto_alt avg `-1.2013` n `238`; crypto_major avg `-0.6378` n `8`; equity avg `-0.5336` n `156`; fx avg `-0.022` n `6`; index avg `-0.0417` n `27`; metal avg `-0.0557` n `20`; unknown avg `0.4525` n `1232`
- 4h: commodity avg `0.3149` n `13`; crypto_alt avg `-0.9887` n `238`; crypto_major avg `-0.4046` n `8`; equity avg `-0.9418` n `156`; fx avg `0.06` n `6`; index avg `-0.0908` n `27`; metal avg `-0.1566` n `20`; unknown avg `41.9801` n `1226`
- 24h: commodity avg `-0.3724` n `13`; crypto_alt avg `-0.9614` n `238`; crypto_major avg `1.1006` n `8`; equity avg `-2.1101` n `155`; fx avg `-0.0004` n `6`; index avg `-0.2868` n `27`; metal avg `-0.675` n `20`; unknown avg `36.2604` n `946`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
