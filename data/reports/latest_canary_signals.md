# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T21:07:28.034977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `12`; crypto_alt avg `0.0305` n `234`; crypto_major avg `0.1424` n `8`; equity avg `-0.0001` n `140`; fx avg `0.0307` n `6`; index avg `-0.0074` n `26`; metal avg `-0.009` n `20`; unknown avg `0.2096` n `940`
- 1h: commodity avg `-0.0624` n `12`; crypto_alt avg `0.377` n `234`; crypto_major avg `0.0631` n `8`; equity avg `-0.0124` n `140`; fx avg `0.0537` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0301` n `20`; unknown avg `15.2639` n `916`
- 4h: commodity avg `-0.1236` n `12`; crypto_alt avg `1.4443` n `234`; crypto_major avg `1.1541` n `8`; equity avg `0.7833` n `140`; fx avg `0.0799` n `6`; index avg `0.1552` n `26`; metal avg `-0.0832` n `20`; unknown avg `6.0643` n `878`
- 24h: commodity avg `-0.1104` n `12`; crypto_alt avg `7.1386` n `234`; crypto_major avg `7.2719` n `8`; equity avg `1.3144` n `140`; fx avg `0.2703` n `6`; index avg `0.0508` n `26`; metal avg `0.3566` n `20`; unknown avg `8.3243` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
