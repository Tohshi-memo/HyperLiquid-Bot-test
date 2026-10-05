# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T14:52:31.759435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0732` n `13`; crypto_alt avg `-0.1253` n `235`; crypto_major avg `-0.1072` n `8`; equity avg `0.1413` n `144`; fx avg `0.0206` n `6`; index avg `0.0102` n `26`; metal avg `0.0694` n `20`; unknown avg `1.0609` n `1077`
- 1h: commodity avg `0.129` n `13`; crypto_alt avg `-0.9039` n `235`; crypto_major avg `-0.7187` n `8`; equity avg `0.2944` n `144`; fx avg `-0.0008` n `6`; index avg `0.0661` n `26`; metal avg `0.0264` n `20`; unknown avg `1.1751` n `1013`
- 4h: commodity avg `-0.0881` n `13`; crypto_alt avg `-1.1369` n `235`; crypto_major avg `-0.659` n `8`; equity avg `0.1251` n `144`; fx avg `-0.0369` n `6`; index avg `0.1254` n `26`; metal avg `-0.0379` n `20`; unknown avg `0.8695` n `1007`
- 24h: commodity avg `-0.1061` n `13`; crypto_alt avg `-0.3005` n `235`; crypto_major avg `0.3898` n `8`; equity avg `0.1634` n `144`; fx avg `-0.102` n `6`; index avg `0.0492` n `26`; metal avg `0.1894` n `20`; unknown avg `-0.5524` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
