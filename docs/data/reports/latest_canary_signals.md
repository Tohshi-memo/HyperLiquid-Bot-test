# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T07:37:27.109757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.756` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7489` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.288` n `239`; crypto_major avg `-0.5019` n `8`; equity avg `-0.0955` n `162`; fx avg `-0.0001` n `6`; index avg `-0.006` n `27`; metal avg `-0.014` n `20`; unknown avg `0.1828` n `1263`
- 1h: commodity avg `-0.0215` n `13`; crypto_alt avg `-0.4691` n `239`; crypto_major avg `-0.4534` n `8`; equity avg `-0.0265` n `162`; fx avg `-0.0063` n `6`; index avg `-0.0062` n `27`; metal avg `0.0687` n `20`; unknown avg `1.0137` n `1261`
- 4h: commodity avg `0.0128` n `13`; crypto_alt avg `-1.0007` n `239`; crypto_major avg `-1.7825` n `8`; equity avg `-0.3317` n `162`; fx avg `0.0071` n `6`; index avg `-0.0336` n `27`; metal avg `-0.0265` n `20`; unknown avg `0.936` n `1225`
- 24h: commodity avg `0.004` n `13`; crypto_alt avg `-5.367` n `239`; crypto_major avg `-5.1021` n `8`; equity avg `-1.0517` n `162`; fx avg `0.0393` n `6`; index avg `-0.104` n `27`; metal avg `-0.4218` n `20`; unknown avg `46.7766` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
