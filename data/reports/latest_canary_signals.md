# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T16:29:40.084855+00:00`
- Correlation status: `ready`
- Asset price records: `88`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `7`; crypto_alt avg `0.0719` n `223`; crypto_major avg `0.0232` n `7`; equity avg `0.0147` n `42`; fx avg `0.0003` n `4`; index avg `-0.0051` n `9`; metal avg `0.0068` n `7`; unknown avg `-0.143` n `313`
- 1h: commodity avg `-0.0098` n `7`; crypto_alt avg `0.2802` n `223`; crypto_major avg `0.1114` n `7`; equity avg `0.0665` n `42`; fx avg `0.0114` n `4`; index avg `0.009` n `9`; metal avg `-0.0011` n `7`; unknown avg `-0.0205` n `313`
- 4h: commodity avg `-0.0173` n `7`; crypto_alt avg `1.354` n `223`; crypto_major avg `0.4942` n `7`; equity avg `0.0641` n `42`; fx avg `0.0362` n `4`; index avg `0.0288` n `9`; metal avg `-0.0147` n `7`; unknown avg `0.05` n `313`
- 24h: commodity avg `0.6265` n `7`; crypto_alt avg `1.2061` n `223`; crypto_major avg `0.1583` n `7`; equity avg `0.3395` n `42`; fx avg `-0.0866` n `4`; index avg `0.1861` n `9`; metal avg `-0.6641` n `7`; unknown avg `0.5502` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5287`, n `84`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5257`, n `80`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5102`, n `84`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5055`, n `80`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4771`, n `80`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4753`, n `80`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4621`, n `80`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4528`, n `84`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4318`, n `84`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4274`, n `80`, moderate_sample_signal
