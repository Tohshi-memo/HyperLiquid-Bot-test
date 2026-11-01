# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T00:52:26.881605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `-0.0579` n `238`; crypto_major avg `-0.0273` n `8`; equity avg `-0.004` n `156`; fx avg `0.0021` n `6`; index avg `0.002` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.06` n `1260`
- 1h: commodity avg `0.0764` n `13`; crypto_alt avg `0.0688` n `238`; crypto_major avg `0.1996` n `8`; equity avg `0.0042` n `156`; fx avg `0.0031` n `6`; index avg `-0.028` n `27`; metal avg `0.0017` n `20`; unknown avg `0.1345` n `1204`
- 4h: commodity avg `0.1176` n `13`; crypto_alt avg `-0.008` n `238`; crypto_major avg `0.1485` n `8`; equity avg `-0.0223` n `156`; fx avg `-0.003` n `6`; index avg `-0.0186` n `27`; metal avg `0.0142` n `20`; unknown avg `0.4526` n `1080`
- 24h: commodity avg `0.1154` n `13`; crypto_alt avg `-1.0357` n `238`; crypto_major avg `-0.4543` n `8`; equity avg `-0.039` n `156`; fx avg `0.0109` n `6`; index avg `-0.0857` n `27`; metal avg `0.0336` n `20`; unknown avg `0.9677` n `1008`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
