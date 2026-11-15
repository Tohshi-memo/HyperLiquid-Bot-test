# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T07:07:29.757613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2749` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.3674` n `239`; crypto_major avg `-0.2619` n `8`; equity avg `-0.0323` n `162`; fx avg `-0.0008` n `6`; index avg `-0.0039` n `27`; metal avg `0.0444` n `20`; unknown avg `-0.0007` n `1257`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `-0.1076` n `239`; crypto_major avg `-0.0577` n `8`; equity avg `0.0192` n `162`; fx avg `-0.0024` n `6`; index avg `-0.0004` n `27`; metal avg `0.0818` n `20`; unknown avg `166.1067` n `1259`
- 4h: commodity avg `0.0241` n `13`; crypto_alt avg `-0.6567` n `239`; crypto_major avg `-1.302` n `8`; equity avg `-0.2438` n `162`; fx avg `0.0095` n `6`; index avg `-0.0271` n `27`; metal avg `-0.0237` n `20`; unknown avg `0.5758` n `1223`
- 24h: commodity avg `0.0435` n `13`; crypto_alt avg `-5.531` n `239`; crypto_major avg `-5.1243` n `8`; equity avg `-1.0315` n `162`; fx avg `0.0525` n `6`; index avg `-0.0947` n `27`; metal avg `-0.4341` n `20`; unknown avg `46.7504` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
