# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T05:52:29.599916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0436` n `13`; crypto_alt avg `-0.225` n `238`; crypto_major avg `-0.1258` n `8`; equity avg `-0.1747` n `155`; fx avg `-0.0087` n `6`; index avg `-0.0294` n `27`; metal avg `-0.0895` n `20`; unknown avg `12.1415` n `1238`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.4338` n `238`; crypto_major avg `0.2717` n `8`; equity avg `0.189` n `155`; fx avg `-0.0104` n `6`; index avg `0.068` n `27`; metal avg `-0.0591` n `20`; unknown avg `3.6369` n `1230`
- 4h: commodity avg `-0.1202` n `13`; crypto_alt avg `-0.2564` n `238`; crypto_major avg `0.3112` n `8`; equity avg `0.4389` n `155`; fx avg `0.0374` n `6`; index avg `0.1923` n `27`; metal avg `-0.2482` n `20`; unknown avg `3.2726` n `1196`
- 24h: commodity avg `-0.1502` n `13`; crypto_alt avg `-1.5951` n `238`; crypto_major avg `-0.929` n `8`; equity avg `-0.7402` n `154`; fx avg `0.0416` n `6`; index avg `0.0337` n `27`; metal avg `-0.2585` n `20`; unknown avg `33.5758` n `974`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
