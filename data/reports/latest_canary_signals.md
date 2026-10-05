# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T13:07:27.954746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0787` n `13`; crypto_alt avg `0.1564` n `235`; crypto_major avg `0.0955` n `8`; equity avg `0.0699` n `144`; fx avg `0.01` n `6`; index avg `0.0117` n `26`; metal avg `0.0278` n `20`; unknown avg `0.4866` n `1077`
- 1h: commodity avg `-0.0539` n `13`; crypto_alt avg `-0.1799` n `235`; crypto_major avg `-0.1707` n `8`; equity avg `-0.0245` n `144`; fx avg `0.0062` n `6`; index avg `-0.029` n `26`; metal avg `-0.0334` n `20`; unknown avg `1.1119` n `1077`
- 4h: commodity avg `-0.231` n `13`; crypto_alt avg `-0.1898` n `235`; crypto_major avg `-0.3819` n `8`; equity avg `-0.1345` n `144`; fx avg `0.0338` n `6`; index avg `-0.006` n `26`; metal avg `-0.0856` n `20`; unknown avg `45.8754` n `1071`
- 24h: commodity avg `-0.2848` n `13`; crypto_alt avg `0.9394` n `235`; crypto_major avg `0.8746` n `8`; equity avg `0.0668` n `144`; fx avg `-0.0323` n `6`; index avg `-0.0613` n `26`; metal avg `0.2669` n `20`; unknown avg `0.7772` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
