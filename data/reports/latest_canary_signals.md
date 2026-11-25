# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T13:37:22.548453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0799` n `13`; crypto_alt avg `-0.2782` n `239`; crypto_major avg `-0.5574` n `8`; equity avg `-0.4889` n `168`; fx avg `0.0024` n `6`; index avg `-0.0681` n `27`; metal avg `-0.1898` n `20`; unknown avg `0.036` n `1265`
- 1h: commodity avg `-0.0524` n `13`; crypto_alt avg `-0.4727` n `239`; crypto_major avg `-0.6945` n `8`; equity avg `-0.6321` n `168`; fx avg `-0.0117` n `6`; index avg `-0.0799` n `27`; metal avg `-0.3271` n `20`; unknown avg `-0.0725` n `1261`
- 4h: commodity avg `0.0777` n `13`; crypto_alt avg `-1.2312` n `239`; crypto_major avg `-0.7678` n `8`; equity avg `-1.0155` n `168`; fx avg `0.0071` n `6`; index avg `-0.1818` n `27`; metal avg `-0.3028` n `20`; unknown avg `141.4263` n `1187`
- 24h: commodity avg `0.2535` n `13`; crypto_alt avg `-2.1514` n `239`; crypto_major avg `-3.2708` n `8`; equity avg `-5.1685` n `168`; fx avg `-0.0372` n `6`; index avg `-0.4536` n `27`; metal avg `-1.2042` n `20`; unknown avg `650.5548` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
