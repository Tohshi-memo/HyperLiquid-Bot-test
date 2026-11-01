# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T14:07:28.375181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0841` n `238`; crypto_major avg `0.1742` n `8`; equity avg `-0.0234` n `156`; fx avg `0.0223` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0001` n `20`; unknown avg `0.0304` n `1257`
- 1h: commodity avg `0.0155` n `13`; crypto_alt avg `0.1239` n `238`; crypto_major avg `0.1402` n `8`; equity avg `-0.019` n `156`; fx avg `0.0131` n `6`; index avg `0.0108` n `27`; metal avg `-0.0059` n `20`; unknown avg `-0.0417` n `1257`
- 4h: commodity avg `-0.0028` n `13`; crypto_alt avg `0.2847` n `238`; crypto_major avg `0.0622` n `8`; equity avg `-0.0105` n `156`; fx avg `0.0109` n `6`; index avg `0.0186` n `27`; metal avg `0.0235` n `20`; unknown avg `-0.0927` n `1237`
- 24h: commodity avg `0.0247` n `13`; crypto_alt avg `0.778` n `238`; crypto_major avg `0.68` n `8`; equity avg `0.5547` n `156`; fx avg `-0.0052` n `6`; index avg `0.0599` n `27`; metal avg `0.0721` n `20`; unknown avg `1.0002` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
