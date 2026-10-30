# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T07:42:38.867368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.01` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1287` n `13`; crypto_alt avg `-0.3419` n `238`; crypto_major avg `-0.6788` n `8`; equity avg `-0.0974` n `156`; fx avg `0.0168` n `6`; index avg `0.0125` n `27`; metal avg `-0.0359` n `20`; unknown avg `53.6951` n `1260`
- 1h: commodity avg `0.2574` n `13`; crypto_alt avg `-0.5732` n `238`; crypto_major avg `-0.9831` n `8`; equity avg `-0.3904` n `156`; fx avg `0.0125` n `6`; index avg `0.0269` n `27`; metal avg `-0.0951` n `20`; unknown avg `131.0674` n `1252`
- 4h: commodity avg `0.1203` n `13`; crypto_alt avg `1.0341` n `238`; crypto_major avg `0.0704` n `8`; equity avg `-0.0906` n `156`; fx avg `-0.0098` n `6`; index avg `0.1011` n `27`; metal avg `-0.2058` n `20`; unknown avg `2.2666` n `1216`
- 24h: commodity avg `0.0207` n `13`; crypto_alt avg `-3.1386` n `238`; crypto_major avg `-0.3375` n `8`; equity avg `-2.7415` n `155`; fx avg `0.0991` n `6`; index avg `-0.2717` n `27`; metal avg `-0.7189` n `20`; unknown avg `31.6979` n `978`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
