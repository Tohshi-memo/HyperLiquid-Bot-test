# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T00:07:27.387768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `13`; crypto_alt avg `0.0925` n `235`; crypto_major avg `0.069` n `8`; equity avg `-0.0658` n `144`; fx avg `0.0103` n `6`; index avg `-0.0246` n `26`; metal avg `0.0018` n `20`; unknown avg `0.0544` n `1071`
- 1h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.0214` n `235`; crypto_major avg `-0.1837` n `8`; equity avg `-0.0419` n `144`; fx avg `0.0281` n `6`; index avg `-0.0288` n `26`; metal avg `-0.027` n `20`; unknown avg `0.4642` n `1071`
- 4h: commodity avg `-0.0011` n `13`; crypto_alt avg `0.3009` n `235`; crypto_major avg `0.1051` n `8`; equity avg `0.0428` n `144`; fx avg `0.0366` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0303` n `20`; unknown avg `-0.131` n `1019`
- 24h: commodity avg `-0.1334` n `13`; crypto_alt avg `0.4497` n `235`; crypto_major avg `0.1234` n `8`; equity avg `0.1211` n `144`; fx avg `-0.0413` n `6`; index avg `0.0898` n `26`; metal avg `0.0517` n `20`; unknown avg `625.9854` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
