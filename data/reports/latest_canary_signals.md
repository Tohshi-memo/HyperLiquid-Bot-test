# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T00:52:28.268796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0381` n `230`; crypto_major avg `0.0459` n `8`; equity avg `-0.0076` n `112`; fx avg `0.0014` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0105` n `783`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0452` n `230`; crypto_major avg `-0.0039` n `8`; equity avg `0.0125` n `112`; fx avg `0.0021` n `6`; index avg `-0.0087` n `25`; metal avg `0.0323` n `20`; unknown avg `-0.0219` n `783`
- 4h: commodity avg `-0.0639` n `12`; crypto_alt avg `-0.1783` n `230`; crypto_major avg `-0.1641` n `8`; equity avg `0.1188` n `112`; fx avg `0.0273` n `6`; index avg `-0.0267` n `25`; metal avg `0.1231` n `20`; unknown avg `-0.2435` n `782`
- 24h: commodity avg `-0.1444` n `12`; crypto_alt avg `-0.7487` n `230`; crypto_major avg `-0.1494` n `8`; equity avg `1.9764` n `112`; fx avg `-0.1041` n `6`; index avg `0.1081` n `25`; metal avg `0.6011` n `20`; unknown avg `-0.0939` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
