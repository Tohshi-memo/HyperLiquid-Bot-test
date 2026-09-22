# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T15:22:35.607884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.2032` n `234`; crypto_major avg `0.1463` n `8`; equity avg `0.0828` n `140`; fx avg `-0.0005` n `6`; index avg `0.0085` n `26`; metal avg `0.0179` n `20`; unknown avg `0.364` n `942`
- 1h: commodity avg `0.1148` n `12`; crypto_alt avg `0.115` n `234`; crypto_major avg `0.1377` n `8`; equity avg `-0.3491` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0486` n `26`; metal avg `-0.0106` n `20`; unknown avg `2.3029` n `940`
- 4h: commodity avg `0.411` n `12`; crypto_alt avg `0.9085` n `234`; crypto_major avg `0.6778` n `8`; equity avg `0.6054` n `140`; fx avg `-0.012` n `6`; index avg `0.1014` n `26`; metal avg `0.1955` n `20`; unknown avg `4.5938` n `892`
- 24h: commodity avg `0.1075` n `12`; crypto_alt avg `1.1694` n `234`; crypto_major avg `1.3998` n `8`; equity avg `0.7752` n `140`; fx avg `-0.2987` n `6`; index avg `0.1658` n `26`; metal avg `0.0089` n `20`; unknown avg `8664.7697` n `842`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
