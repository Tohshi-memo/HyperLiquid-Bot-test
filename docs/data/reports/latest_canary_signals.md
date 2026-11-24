# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T11:52:28.792890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.3495` n `239`; crypto_major avg `0.5775` n `8`; equity avg `0.5106` n `166`; fx avg `0.0208` n `6`; index avg `0.0586` n `27`; metal avg `0.0769` n `20`; unknown avg `159.2973` n `1266`
- 1h: commodity avg `0.0339` n `13`; crypto_alt avg `0.3085` n `239`; crypto_major avg `0.9502` n `8`; equity avg `0.7076` n `166`; fx avg `0.0392` n `6`; index avg `0.0716` n `27`; metal avg `0.1846` n `20`; unknown avg `1.372` n `1260`
- 4h: commodity avg `0.0785` n `13`; crypto_alt avg `-1.5425` n `239`; crypto_major avg `-0.6072` n `8`; equity avg `-1.9752` n `166`; fx avg `0.1231` n `6`; index avg `-0.2596` n `27`; metal avg `-0.0811` n `20`; unknown avg `0.4231` n `1200`
- 24h: commodity avg `-0.4785` n `13`; crypto_alt avg `-1.3706` n `239`; crypto_major avg `-1.2391` n `8`; equity avg `1.2986` n `166`; fx avg `-0.0454` n `6`; index avg `0.28` n `27`; metal avg `-0.2869` n `20`; unknown avg `-0.1205` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
