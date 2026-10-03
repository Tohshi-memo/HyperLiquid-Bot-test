# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T02:22:27.015204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.2479` n `235`; crypto_major avg `0.1191` n `8`; equity avg `0.023` n `143`; fx avg `0.0018` n `6`; index avg `0.0025` n `26`; metal avg `0.0104` n `20`; unknown avg `0.0752` n `984`
- 1h: commodity avg `-0.1131` n `13`; crypto_alt avg `0.0416` n `235`; crypto_major avg `-0.0346` n `8`; equity avg `0.057` n `143`; fx avg `0.0063` n `6`; index avg `0.019` n `26`; metal avg `0.0235` n `20`; unknown avg `-0.1495` n `982`
- 4h: commodity avg `-0.2093` n `13`; crypto_alt avg `1.5635` n `235`; crypto_major avg `0.8693` n `8`; equity avg `0.0958` n `143`; fx avg `0.0175` n `6`; index avg `0.0353` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.4091` n `976`
- 24h: commodity avg `0.0362` n `13`; crypto_alt avg `-0.3747` n `235`; crypto_major avg `-0.2993` n `8`; equity avg `0.7126` n `142`; fx avg `-0.1017` n `6`; index avg `0.2853` n `26`; metal avg `-0.1055` n `20`; unknown avg `-0.7035` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
