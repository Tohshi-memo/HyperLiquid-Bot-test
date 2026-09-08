# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T02:22:34.443863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `0.1625` n `232`; crypto_major avg `0.1418` n `8`; equity avg `0.0962` n `134`; fx avg `-0.015` n `6`; index avg `0.0096` n `26`; metal avg `-0.0599` n `20`; unknown avg `0.6391` n `797`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.2195` n `232`; crypto_major avg `0.0669` n `8`; equity avg `0.2186` n `134`; fx avg `-0.0728` n `6`; index avg `0.0504` n `26`; metal avg `-0.0391` n `20`; unknown avg `0.0432` n `789`
- 4h: commodity avg `-0.1043` n `12`; crypto_alt avg `1.086` n `232`; crypto_major avg `0.5188` n `8`; equity avg `0.511` n `134`; fx avg `-0.2126` n `6`; index avg `0.1048` n `26`; metal avg `0.1333` n `20`; unknown avg `1.3847` n `783`
- 24h: commodity avg `0.1026` n `12`; crypto_alt avg `1.4937` n `232`; crypto_major avg `-0.48` n `8`; equity avg `0.8188` n `134`; fx avg `-0.3386` n `6`; index avg `0.1626` n `26`; metal avg `0.2787` n `20`; unknown avg `7693.0245` n `650`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
