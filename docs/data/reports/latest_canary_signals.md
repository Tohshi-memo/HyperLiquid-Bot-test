# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T17:52:29.191295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `13`; crypto_alt avg `-0.1129` n `237`; crypto_major avg `-0.0639` n `8`; equity avg `-0.2423` n `151`; fx avg `0.008` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0153` n `20`; unknown avg `-0.0832` n `1196`
- 1h: commodity avg `0.1811` n `13`; crypto_alt avg `-0.6823` n `237`; crypto_major avg `-0.2955` n `8`; equity avg `-0.4051` n `151`; fx avg `0.0204` n `6`; index avg `-0.0499` n `26`; metal avg `0.0317` n `20`; unknown avg `-0.0738` n `1194`
- 4h: commodity avg `0.408` n `13`; crypto_alt avg `-0.2962` n `237`; crypto_major avg `-0.4383` n `8`; equity avg `-0.6342` n `151`; fx avg `0.0121` n `6`; index avg `-0.0329` n `26`; metal avg `-0.021` n `20`; unknown avg `-0.011` n `1133`
- 24h: commodity avg `0.0467` n `13`; crypto_alt avg `1.1568` n `237`; crypto_major avg `1.2972` n `8`; equity avg `2.6081` n `151`; fx avg `-0.0113` n `6`; index avg `0.5258` n `26`; metal avg `0.1114` n `20`; unknown avg `2.4855` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
