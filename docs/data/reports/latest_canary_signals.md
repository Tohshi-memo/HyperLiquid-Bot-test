# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T11:07:38.784754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `13`; crypto_alt avg `0.5948` n `239`; crypto_major avg `0.4873` n `8`; equity avg `0.2727` n `162`; fx avg `-0.0008` n `6`; index avg `0.0388` n `27`; metal avg `0.0305` n `20`; unknown avg `0.1678` n `1259`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `0.596` n `239`; crypto_major avg `0.8443` n `8`; equity avg `0.2738` n `162`; fx avg `-0.0001` n `6`; index avg `0.0284` n `27`; metal avg `0.1365` n `20`; unknown avg `0.597` n `1261`
- 4h: commodity avg `-0.1698` n `13`; crypto_alt avg `0.3431` n `239`; crypto_major avg `0.4288` n `8`; equity avg `-0.128` n `162`; fx avg `-0.0259` n `6`; index avg `0.0156` n `27`; metal avg `0.057` n `20`; unknown avg `70.4723` n `1215`
- 24h: commodity avg `-0.3507` n `13`; crypto_alt avg `-0.6722` n `239`; crypto_major avg `-0.6019` n `8`; equity avg `-0.7657` n `162`; fx avg `-0.065` n `6`; index avg `-0.0381` n `27`; metal avg `0.0546` n `20`; unknown avg `32.9528` n `1051`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
