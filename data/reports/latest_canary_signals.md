# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T18:37:27.891008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0515` n `13`; crypto_alt avg `-0.0013` n `239`; crypto_major avg `0.1759` n `8`; equity avg `0.2464` n `164`; fx avg `0.0066` n `6`; index avg `0.0279` n `27`; metal avg `0.0705` n `20`; unknown avg `0.5795` n `1265`
- 1h: commodity avg `0.1477` n `13`; crypto_alt avg `-0.3147` n `239`; crypto_major avg `-0.054` n `8`; equity avg `-0.085` n `164`; fx avg `0.0109` n `6`; index avg `-0.006` n `27`; metal avg `0.0594` n `20`; unknown avg `0.6667` n `1263`
- 4h: commodity avg `-0.0792` n `13`; crypto_alt avg `-0.4124` n `239`; crypto_major avg `0.0195` n `8`; equity avg `0.8175` n `164`; fx avg `-0.0038` n `6`; index avg `0.0625` n `27`; metal avg `-0.046` n `20`; unknown avg `1.0294` n `1257`
- 24h: commodity avg `-0.5214` n `13`; crypto_alt avg `0.3377` n `239`; crypto_major avg `0.0331` n `8`; equity avg `0.5065` n `164`; fx avg `-0.1777` n `6`; index avg `0.0757` n `27`; metal avg `-1.1388` n `20`; unknown avg `0.3773` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
