# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T16:22:33.618887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2147` n `12`; crypto_alt avg `0.6675` n `234`; crypto_major avg `0.574` n `8`; equity avg `0.3668` n `141`; fx avg `-0.0048` n `6`; index avg `0.0975` n `26`; metal avg `0.0966` n `20`; unknown avg `14.4711` n `962`
- 1h: commodity avg `-0.3665` n `12`; crypto_alt avg `1.6567` n `234`; crypto_major avg `1.3714` n `8`; equity avg `0.8233` n `141`; fx avg `-0.0336` n `6`; index avg `0.1492` n `26`; metal avg `0.1029` n `20`; unknown avg `13.0547` n `954`
- 4h: commodity avg `-0.3348` n `12`; crypto_alt avg `-0.8446` n `234`; crypto_major avg `0.0161` n `8`; equity avg `-0.664` n `141`; fx avg `0.0346` n `6`; index avg `-0.0728` n `26`; metal avg `-0.2156` n `20`; unknown avg `75.0674` n `904`
- 24h: commodity avg `-0.3599` n `12`; crypto_alt avg `-2.7996` n `234`; crypto_major avg `-1.2901` n `8`; equity avg `-2.999` n `141`; fx avg `0.0214` n `6`; index avg `-0.266` n `26`; metal avg `-0.9977` n `20`; unknown avg `21.063` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
