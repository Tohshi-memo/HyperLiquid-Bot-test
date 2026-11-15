# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T10:07:26.735077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6836` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.512` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.0087` n `239`; crypto_major avg `0.2528` n `8`; equity avg `0.0254` n `162`; fx avg `0.0015` n `6`; index avg `-0.001` n `27`; metal avg `0.0072` n `20`; unknown avg `-0.1457` n `1257`
- 1h: commodity avg `-0.035` n `13`; crypto_alt avg `0.059` n `239`; crypto_major avg `0.1941` n `8`; equity avg `-0.0496` n `162`; fx avg `0.0001` n `6`; index avg `-0.0091` n `27`; metal avg `0.0049` n `20`; unknown avg `0.0813` n `1259`
- 4h: commodity avg `-0.0662` n `13`; crypto_alt avg `0.8968` n `239`; crypto_major avg `1.8839` n `8`; equity avg `0.3719` n `162`; fx avg `-0.0202` n `6`; index avg `0.0415` n `27`; metal avg `0.2003` n `20`; unknown avg `166.2848` n `1243`
- 24h: commodity avg `0.0021` n `13`; crypto_alt avg `-4.3356` n `239`; crypto_major avg `-3.2151` n `8`; equity avg `-0.7506` n `162`; fx avg `0.0323` n `6`; index avg `-0.0675` n `27`; metal avg `-0.3449` n `20`; unknown avg `44.4236` n `1120`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
