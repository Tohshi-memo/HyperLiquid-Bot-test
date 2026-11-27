# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T21:37:28.739797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.0294` n `239`; crypto_major avg `0.0299` n `8`; equity avg `-0.0668` n `168`; fx avg `0.0029` n `6`; index avg `0.0159` n `27`; metal avg `-0.0095` n `20`; unknown avg `1.633` n `1247`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `0.086` n `239`; crypto_major avg `0.0273` n `8`; equity avg `-0.0164` n `168`; fx avg `-0.0005` n `6`; index avg `0.0143` n `27`; metal avg `0.0202` n `20`; unknown avg `0.8588` n `1187`
- 4h: commodity avg `0.0461` n `13`; crypto_alt avg `0.4933` n `239`; crypto_major avg `0.2901` n `8`; equity avg `0.664` n `168`; fx avg `-0.0099` n `6`; index avg `0.0814` n `27`; metal avg `0.2235` n `20`; unknown avg `179.2695` n `1162`
- 24h: commodity avg `-0.4944` n `13`; crypto_alt avg `-0.0594` n `239`; crypto_major avg `-0.2962` n `8`; equity avg `3.0278` n `168`; fx avg `-0.1483` n `6`; index avg `0.3263` n `27`; metal avg `0.9311` n `20`; unknown avg `278.937` n `1001`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
