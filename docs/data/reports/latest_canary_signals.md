# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T14:22:30.347447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.2869` n `234`; crypto_major avg `0.0927` n `8`; equity avg `0.46` n `141`; fx avg `-0.018` n `6`; index avg `0.0463` n `26`; metal avg `0.0762` n `20`; unknown avg `203.1389` n `963`
- 1h: commodity avg `0.1096` n `12`; crypto_alt avg `-0.0706` n `234`; crypto_major avg `-0.4689` n `8`; equity avg `0.3847` n `141`; fx avg `-0.02` n `6`; index avg `-0.0054` n `26`; metal avg `0.082` n `20`; unknown avg `238.7125` n `961`
- 4h: commodity avg `-0.2417` n `12`; crypto_alt avg `0.8992` n `234`; crypto_major avg `0.4027` n `8`; equity avg `0.7521` n `141`; fx avg `-0.0365` n `6`; index avg `0.054` n `26`; metal avg `0.0674` n `20`; unknown avg `4.0411` n `955`
- 24h: commodity avg `-0.6693` n `12`; crypto_alt avg `1.8663` n `234`; crypto_major avg `0.7485` n `8`; equity avg `0.8098` n `141`; fx avg `-0.1267` n `6`; index avg `0.0287` n `26`; metal avg `-0.0495` n `20`; unknown avg `17.0627` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
