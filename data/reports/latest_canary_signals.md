# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T13:22:28.903193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `13`; crypto_alt avg `0.0754` n `238`; crypto_major avg `0.0011` n `8`; equity avg `0.0084` n `156`; fx avg `0.0` n `6`; index avg `-0.0025` n `27`; metal avg `-0.0` n `20`; unknown avg `-0.0325` n `1263`
- 1h: commodity avg `-0.0337` n `13`; crypto_alt avg `0.6403` n `238`; crypto_major avg `0.2524` n `8`; equity avg `0.081` n `156`; fx avg `0.0054` n `6`; index avg `0.0042` n `27`; metal avg `0.0212` n `20`; unknown avg `-0.1273` n `1257`
- 4h: commodity avg `-0.0425` n `13`; crypto_alt avg `0.3431` n `238`; crypto_major avg `-0.0434` n `8`; equity avg `0.0057` n `156`; fx avg `-0.0034` n `6`; index avg `-0.0032` n `27`; metal avg `0.0291` n `20`; unknown avg `0.0383` n `1237`
- 24h: commodity avg `-0.0235` n `13`; crypto_alt avg `0.8386` n `238`; crypto_major avg `0.4607` n `8`; equity avg `0.6342` n `156`; fx avg `-0.0182` n `6`; index avg `0.0502` n `27`; metal avg `0.0769` n `20`; unknown avg `3.0855` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
