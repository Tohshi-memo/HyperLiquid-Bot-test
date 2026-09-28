# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T07:52:28.763930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `-0.2905` n `234`; crypto_major avg `-0.1525` n `8`; equity avg `-0.0364` n `141`; fx avg `0.0317` n `6`; index avg `0.0022` n `26`; metal avg `0.0097` n `20`; unknown avg `2.5386` n `962`
- 1h: commodity avg `0.1457` n `12`; crypto_alt avg `-0.9907` n `234`; crypto_major avg `-0.259` n `8`; equity avg `-0.0938` n `140`; fx avg `0.0325` n `6`; index avg `-0.0048` n `23`; metal avg `-0.2069` n `18`; unknown avg `10.7766` n `942`
- 4h: commodity avg `0.1074` n `12`; crypto_alt avg `-1.9654` n `234`; crypto_major avg `-0.9944` n `8`; equity avg `-0.824` n `141`; fx avg `0.0482` n `6`; index avg `-0.0664` n `26`; metal avg `-0.2869` n `20`; unknown avg `3.1953` n `930`
- 24h: commodity avg `-0.2742` n `12`; crypto_alt avg `-4.4868` n `234`; crypto_major avg `-3.086` n `8`; equity avg `-2.3385` n `141`; fx avg `0.0948` n `6`; index avg `-0.2287` n `26`; metal avg `-0.9779` n `20`; unknown avg `4.7711` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
