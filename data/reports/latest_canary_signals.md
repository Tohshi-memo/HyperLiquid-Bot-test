# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T06:22:27.392346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `13`; crypto_alt avg `-0.0625` n `238`; crypto_major avg `-0.0888` n `8`; equity avg `-0.0122` n `156`; fx avg `0.0085` n `6`; index avg `-0.0024` n `27`; metal avg `0.0016` n `20`; unknown avg `0.0441` n `1262`
- 1h: commodity avg `0.0147` n `13`; crypto_alt avg `0.293` n `238`; crypto_major avg `0.096` n `8`; equity avg `0.0617` n `156`; fx avg `0.0064` n `6`; index avg `0.0069` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.4429` n `1240`
- 4h: commodity avg `0.0726` n `13`; crypto_alt avg `0.6548` n `238`; crypto_major avg `0.1711` n `8`; equity avg `0.2624` n `156`; fx avg `0.0036` n `6`; index avg `0.0329` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.0808` n `1224`
- 24h: commodity avg `-0.031` n `13`; crypto_alt avg `0.558` n `238`; crypto_major avg `0.3947` n `8`; equity avg `0.3132` n `156`; fx avg `0.0063` n `6`; index avg `-0.0034` n `27`; metal avg `0.0434` n `20`; unknown avg `2.0706` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
