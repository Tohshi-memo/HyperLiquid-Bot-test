# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T17:52:31.936150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `12`; crypto_alt avg `0.1403` n `234`; crypto_major avg `0.0405` n `8`; equity avg `0.1` n `141`; fx avg `0.0047` n `6`; index avg `0.0125` n `26`; metal avg `0.0032` n `20`; unknown avg `0.3032` n `963`
- 1h: commodity avg `-0.152` n `12`; crypto_alt avg `0.3267` n `234`; crypto_major avg `0.3109` n `8`; equity avg `0.1911` n `141`; fx avg `0.0133` n `6`; index avg `0.0361` n `26`; metal avg `0.0942` n `20`; unknown avg `4.0308` n `960`
- 4h: commodity avg `-0.3374` n `12`; crypto_alt avg `-0.1929` n `234`; crypto_major avg `0.0576` n `8`; equity avg `-0.0193` n `141`; fx avg `0.027` n `6`; index avg `0.0081` n `26`; metal avg `-0.0392` n `20`; unknown avg `130.912` n `904`
- 24h: commodity avg `-0.5035` n `12`; crypto_alt avg `-2.8959` n `234`; crypto_major avg `-1.283` n `8`; equity avg `-2.9677` n `141`; fx avg `0.0466` n `6`; index avg `-0.2569` n `26`; metal avg `-0.9385` n `20`; unknown avg `24.7532` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
