# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T00:37:23.371296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.044` n `13`; crypto_alt avg `-0.0688` n `239`; crypto_major avg `0.0134` n `8`; equity avg `0.0368` n `168`; fx avg `-0.0225` n `6`; index avg `0.0016` n `27`; metal avg `0.0069` n `20`; unknown avg `0.8244` n `1263`
- 1h: commodity avg `0.0641` n `13`; crypto_alt avg `0.3838` n `239`; crypto_major avg `0.3848` n `8`; equity avg `0.0425` n `168`; fx avg `-0.0383` n `6`; index avg `-0.0079` n `27`; metal avg `0.0527` n `20`; unknown avg `0.7763` n `1247`
- 4h: commodity avg `0.0986` n `13`; crypto_alt avg `-0.2463` n `239`; crypto_major avg `-0.5124` n `8`; equity avg `-0.21` n `168`; fx avg `-0.0162` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0193` n `20`; unknown avg `66.6043` n `1143`
- 24h: commodity avg `0.1705` n `13`; crypto_alt avg `0.5497` n `239`; crypto_major avg `0.1708` n `8`; equity avg `-0.3715` n `168`; fx avg `-0.0146` n `6`; index avg `-0.054` n `27`; metal avg `-0.0202` n `20`; unknown avg `210.6274` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
