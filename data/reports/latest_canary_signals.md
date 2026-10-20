# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T02:52:25.747664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `13`; crypto_alt avg `0.4191` n `237`; crypto_major avg `0.2879` n `8`; equity avg `0.2112` n `151`; fx avg `0.0144` n `6`; index avg `0.0347` n `26`; metal avg `0.0362` n `20`; unknown avg `1.2379` n `1198`
- 1h: commodity avg `-0.0216` n `13`; crypto_alt avg `0.2841` n `237`; crypto_major avg `0.1597` n `8`; equity avg `0.327` n `151`; fx avg `0.0278` n `6`; index avg `0.031` n `26`; metal avg `0.1096` n `20`; unknown avg `1.0407` n `1196`
- 4h: commodity avg `0.0742` n `13`; crypto_alt avg `0.0814` n `237`; crypto_major avg `-0.1933` n `8`; equity avg `-0.3561` n `151`; fx avg `0.015` n `6`; index avg `-0.1011` n `26`; metal avg `0.0449` n `20`; unknown avg `0.3689` n `1189`
- 24h: commodity avg `0.1927` n `13`; crypto_alt avg `-0.0038` n `237`; crypto_major avg `-0.5542` n `8`; equity avg `-0.5032` n `151`; fx avg `0.0168` n `6`; index avg `-0.059` n `26`; metal avg `-0.2157` n `20`; unknown avg `5.2771` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
