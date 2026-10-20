# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T22:37:29.550319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `13`; crypto_alt avg `-0.0592` n `237`; crypto_major avg `-0.0467` n `8`; equity avg `-0.0708` n `151`; fx avg `-0.012` n `6`; index avg `0.0027` n `26`; metal avg `-0.0259` n `20`; unknown avg `0.0653` n `1159`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `0.1312` n `237`; crypto_major avg `0.2209` n `8`; equity avg `0.2438` n `151`; fx avg `-0.0043` n `6`; index avg `0.0432` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.2383` n `1157`
- 4h: commodity avg `0.0666` n `13`; crypto_alt avg `0.825` n `237`; crypto_major avg `0.9387` n `8`; equity avg `1.6751` n `151`; fx avg `-0.0078` n `6`; index avg `0.2105` n `26`; metal avg `0.0388` n `20`; unknown avg `3.081` n `1065`
- 24h: commodity avg `0.0083` n `13`; crypto_alt avg `2.4198` n `237`; crypto_major avg `1.8103` n `8`; equity avg `1.413` n `151`; fx avg `0.0272` n `6`; index avg `0.1521` n `26`; metal avg `0.098` n `20`; unknown avg `205.0694` n `1018`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
