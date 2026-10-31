# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T21:37:26.967365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `0.0008` n `238`; crypto_major avg `0.0447` n `8`; equity avg `0.0001` n `156`; fx avg `0.0` n `6`; index avg `0.0001` n `27`; metal avg `0.0024` n `20`; unknown avg `2.0202` n `1248`
- 1h: commodity avg `0.0284` n `13`; crypto_alt avg `0.1629` n `238`; crypto_major avg `0.0007` n `8`; equity avg `0.0126` n `156`; fx avg `-0.0023` n `6`; index avg `-0.0027` n `27`; metal avg `0.003` n `20`; unknown avg `1.5284` n `1222`
- 4h: commodity avg `0.0252` n `13`; crypto_alt avg `-0.38` n `238`; crypto_major avg `-0.0736` n `8`; equity avg `0.0245` n `156`; fx avg `-0.0053` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0095` n `20`; unknown avg `1.2907` n `1148`
- 24h: commodity avg `-0.1` n `13`; crypto_alt avg `0.0194` n `238`; crypto_major avg `0.0285` n `8`; equity avg `0.2373` n `156`; fx avg `0.0076` n `6`; index avg `-0.0496` n `27`; metal avg `0.0684` n `20`; unknown avg `1.6436` n `1071`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
