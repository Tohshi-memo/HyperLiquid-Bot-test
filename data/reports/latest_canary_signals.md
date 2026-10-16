# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T03:22:25.748005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `0.2504` n `236`; crypto_major avg `0.0793` n `8`; equity avg `0.1372` n `151`; fx avg `-0.0081` n `6`; index avg `0.0112` n `26`; metal avg `-0.0187` n `20`; unknown avg `-0.0166` n `1136`
- 1h: commodity avg `0.0359` n `13`; crypto_alt avg `0.0349` n `236`; crypto_major avg `0.0213` n `8`; equity avg `0.1629` n `151`; fx avg `-0.0085` n `6`; index avg `0.0179` n `26`; metal avg `0.1591` n `20`; unknown avg `0.1021` n `1134`
- 4h: commodity avg `-0.0876` n `13`; crypto_alt avg `0.3109` n `236`; crypto_major avg `0.2396` n `8`; equity avg `0.3812` n `151`; fx avg `0.0579` n `6`; index avg `0.0457` n `26`; metal avg `0.1814` n `20`; unknown avg `0.8284` n `1128`
- 24h: commodity avg `-0.0738` n `13`; crypto_alt avg `3.4621` n `236`; crypto_major avg `2.1169` n `8`; equity avg `2.3008` n `151`; fx avg `-0.0018` n `6`; index avg `0.4053` n `26`; metal avg `0.4368` n `20`; unknown avg `25.9445` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0897`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0686`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
