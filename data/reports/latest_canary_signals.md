# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T19:22:32.790379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `13`; crypto_alt avg `-0.2767` n `237`; crypto_major avg `-0.2176` n `8`; equity avg `-0.2124` n `151`; fx avg `0.0069` n `6`; index avg `-0.0413` n `26`; metal avg `-0.0423` n `20`; unknown avg `0.2931` n `1199`
- 1h: commodity avg `0.1936` n `13`; crypto_alt avg `-0.4657` n `237`; crypto_major avg `-0.3026` n `8`; equity avg `-0.2081` n `151`; fx avg `0.0123` n `6`; index avg `-0.0628` n `26`; metal avg `-0.074` n `20`; unknown avg `0.5885` n `1197`
- 4h: commodity avg `0.3707` n `13`; crypto_alt avg `0.1187` n `237`; crypto_major avg `0.2553` n `8`; equity avg `-0.1666` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0536` n `26`; metal avg `-0.0923` n `20`; unknown avg `4.3992` n `1177`
- 24h: commodity avg `-0.0465` n `13`; crypto_alt avg `2.1492` n `237`; crypto_major avg `1.34` n `8`; equity avg `-0.1153` n `151`; fx avg `0.0289` n `6`; index avg `-0.0553` n `26`; metal avg `-0.0439` n `20`; unknown avg `3.8732` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
