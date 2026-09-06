# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T06:07:28.271141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.2131` n `232`; crypto_major avg `-0.1682` n `8`; equity avg `0.0065` n `134`; fx avg `-0.0122` n `6`; index avg `0.0086` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.0793` n `774`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `0.0091` n `232`; crypto_major avg `0.1475` n `8`; equity avg `0.078` n `134`; fx avg `0.0018` n `6`; index avg `0.017` n `26`; metal avg `0.0097` n `20`; unknown avg `1.1059` n `772`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.2146` n `232`; crypto_major avg `0.5534` n `8`; equity avg `0.1323` n `134`; fx avg `0.0021` n `6`; index avg `0.0284` n `26`; metal avg `0.0028` n `20`; unknown avg `458.8911` n `730`
- 24h: commodity avg `0.1521` n `12`; crypto_alt avg `2.5575` n `232`; crypto_major avg `3.1736` n `8`; equity avg `0.4286` n `134`; fx avg `-0.0457` n `6`; index avg `0.0876` n `26`; metal avg `0.0207` n `20`; unknown avg `494.2841` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
