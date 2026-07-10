# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T08:52:30.631496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.0155` n `229`; crypto_major avg `-0.0535` n `8`; equity avg `0.0959` n `91`; fx avg `-0.0251` n `6`; index avg `0.0224` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.0008` n `765`
- 1h: commodity avg `0.1255` n `12`; crypto_alt avg `0.2895` n `229`; crypto_major avg `0.4644` n `8`; equity avg `0.0527` n `91`; fx avg `-0.0155` n `6`; index avg `0.0109` n `25`; metal avg `-0.1039` n `20`; unknown avg `0.1065` n `765`
- 4h: commodity avg `-0.0865` n `12`; crypto_alt avg `0.1052` n `229`; crypto_major avg `0.176` n `8`; equity avg `-0.734` n `91`; fx avg `-0.1089` n `6`; index avg `-0.1301` n `25`; metal avg `-0.2143` n `20`; unknown avg `1.1672` n `733`
- 24h: commodity avg `-0.8301` n `12`; crypto_alt avg `0.8215` n `229`; crypto_major avg `1.2597` n `8`; equity avg `0.2014` n `91`; fx avg `-0.143` n `6`; index avg `0.1716` n `25`; metal avg `0.0605` n `20`; unknown avg `0.0385` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
