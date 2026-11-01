# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T11:37:25.859073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.0535` n `238`; crypto_major avg `-0.0604` n `8`; equity avg `-0.0212` n `156`; fx avg `-0.0026` n `6`; index avg `-0.0021` n `27`; metal avg `0.0111` n `20`; unknown avg `-0.0755` n `1263`
- 1h: commodity avg `-0.0183` n `13`; crypto_alt avg `-0.0674` n `238`; crypto_major avg `-0.116` n `8`; equity avg `-0.0719` n `156`; fx avg `-0.0007` n `6`; index avg `0.0049` n `27`; metal avg `0.0059` n `20`; unknown avg `0.0126` n `1257`
- 4h: commodity avg `-0.0433` n `13`; crypto_alt avg `-0.0889` n `238`; crypto_major avg `0.1878` n `8`; equity avg `0.1286` n `156`; fx avg `-0.0126` n `6`; index avg `0.0099` n `27`; metal avg `0.0304` n `20`; unknown avg `0.0391` n `1227`
- 24h: commodity avg `-0.068` n `13`; crypto_alt avg `0.5479` n `238`; crypto_major avg `0.3678` n `8`; equity avg `0.4949` n `156`; fx avg `-0.0086` n `6`; index avg `0.0328` n `27`; metal avg `0.0832` n `20`; unknown avg `3.6747` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
