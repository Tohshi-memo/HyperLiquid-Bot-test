# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T18:52:38.940863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.071` n `13`; crypto_alt avg `0.195` n `238`; crypto_major avg `0.1384` n `8`; equity avg `0.0584` n `156`; fx avg `0.005` n `6`; index avg `0.0118` n `27`; metal avg `0.016` n `20`; unknown avg `7.3109` n `1238`
- 1h: commodity avg `-0.0337` n `13`; crypto_alt avg `-0.2315` n `238`; crypto_major avg `0.171` n `8`; equity avg `-0.1891` n `156`; fx avg `-0.0054` n `6`; index avg `0.0028` n `27`; metal avg `0.0295` n `20`; unknown avg `1.268` n `1232`
- 4h: commodity avg `0.3347` n `13`; crypto_alt avg `-0.455` n `238`; crypto_major avg `0.0962` n `8`; equity avg `-0.5327` n `156`; fx avg `0.0392` n `6`; index avg `-0.0155` n `27`; metal avg `-0.1046` n `20`; unknown avg `1.4348` n `1226`
- 24h: commodity avg `-0.4736` n `13`; crypto_alt avg `-0.5309` n `238`; crypto_major avg `1.4805` n `8`; equity avg `-1.7446` n `155`; fx avg `0.0228` n `6`; index avg `-0.1974` n `27`; metal avg `-0.5036` n `20`; unknown avg `35.8899` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
