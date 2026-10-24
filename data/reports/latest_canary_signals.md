# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T00:07:36.278718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `-0.003` n `237`; crypto_major avg `-0.0185` n `8`; equity avg `0.1076` n `152`; fx avg `0.0028` n `6`; index avg `0.0214` n `26`; metal avg `-0.0059` n `20`; unknown avg `1.0354` n `1222`
- 1h: commodity avg `-0.0404` n `13`; crypto_alt avg `1.0619` n `237`; crypto_major avg `0.5516` n `8`; equity avg `0.3264` n `152`; fx avg `-0.0286` n `6`; index avg `0.0407` n `26`; metal avg `0.0388` n `20`; unknown avg `1.3643` n `1218`
- 4h: commodity avg `0.0832` n `13`; crypto_alt avg `-0.926` n `237`; crypto_major avg `-0.4161` n `8`; equity avg `0.0415` n `152`; fx avg `0.0128` n `6`; index avg `0.0087` n `26`; metal avg `-0.0382` n `20`; unknown avg `-0.0195` n `1150`
- 24h: commodity avg `0.5445` n `13`; crypto_alt avg `-0.5203` n `237`; crypto_major avg `-0.1847` n `8`; equity avg `1.7218` n `152`; fx avg `-0.0357` n `6`; index avg `0.1778` n `26`; metal avg `-0.1506` n `20`; unknown avg `200.6272` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
