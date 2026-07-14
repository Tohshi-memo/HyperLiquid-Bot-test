# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T00:22:25.880686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.109` n `12`; crypto_alt avg `0.2618` n `230`; crypto_major avg `0.2218` n `8`; equity avg `0.4714` n `92`; fx avg `-0.0172` n `6`; index avg `0.127` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.444` n `766`
- 1h: commodity avg `0.242` n `12`; crypto_alt avg `0.4245` n `230`; crypto_major avg `0.3473` n `8`; equity avg `0.2126` n `92`; fx avg `-0.0037` n `6`; index avg `-0.0187` n `25`; metal avg `-0.0964` n `20`; unknown avg `0.1789` n `766`
- 4h: commodity avg `0.4221` n `12`; crypto_alt avg `0.2151` n `230`; crypto_major avg `0.4035` n `8`; equity avg `-0.0999` n `92`; fx avg `-0.0181` n `6`; index avg `-0.0944` n `25`; metal avg `-0.0935` n `20`; unknown avg `-0.0696` n `766`
- 24h: commodity avg `1.2726` n `12`; crypto_alt avg `-2.3201` n `230`; crypto_major avg `-2.91` n `8`; equity avg `-3.2205` n `92`; fx avg `-0.0878` n `6`; index avg `-0.6784` n `25`; metal avg `-0.5131` n `20`; unknown avg `-0.4298` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
