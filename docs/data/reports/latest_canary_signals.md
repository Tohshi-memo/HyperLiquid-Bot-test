# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T23:52:29.116294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.15` n `237`; crypto_major avg `-0.1558` n `8`; equity avg `-0.1835` n `151`; fx avg `-0.0088` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.021` n `1198`
- 1h: commodity avg `0.0114` n `13`; crypto_alt avg `-0.005` n `237`; crypto_major avg `-0.0635` n `8`; equity avg `-0.1886` n `151`; fx avg `0.0045` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0207` n `20`; unknown avg `0.487` n `1195`
- 4h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.8221` n `237`; crypto_major avg `0.7063` n `8`; equity avg `-0.0135` n `151`; fx avg `-0.0047` n `6`; index avg `0.0229` n `26`; metal avg `-0.0782` n `20`; unknown avg `4.2202` n `1114`
- 24h: commodity avg `0.1149` n `13`; crypto_alt avg `0.5924` n `237`; crypto_major avg `0.3185` n `8`; equity avg `1.0732` n `151`; fx avg `-0.0246` n `6`; index avg `0.2411` n `26`; metal avg `-0.2325` n `20`; unknown avg `4.86` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
