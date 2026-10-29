# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T19:22:33.322508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `0.0759` n `238`; crypto_major avg `-0.0027` n `8`; equity avg `0.0082` n `156`; fx avg `0.0083` n `6`; index avg `0.0054` n `27`; metal avg `-0.0035` n `20`; unknown avg `161.6276` n `1238`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.4906` n `238`; crypto_major avg `-0.3961` n `8`; equity avg `-0.1894` n `156`; fx avg `0.0019` n `6`; index avg `0.0069` n `27`; metal avg `0.0287` n `20`; unknown avg `1.9108` n `1232`
- 4h: commodity avg `0.328` n `13`; crypto_alt avg `-1.3094` n `238`; crypto_major avg `-0.8918` n `8`; equity avg `-1.0767` n `156`; fx avg `0.0061` n `6`; index avg `-0.0751` n `27`; metal avg `-0.0462` n `20`; unknown avg `3.0648` n `1228`
- 24h: commodity avg `-0.4881` n `13`; crypto_alt avg `-1.1466` n `238`; crypto_major avg `1.0117` n `8`; equity avg `-1.8011` n `155`; fx avg `0.0301` n `6`; index avg `-0.1832` n `27`; metal avg `-0.5735` n `20`; unknown avg `10.5481` n `946`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
