# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T11:37:30.027236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.08` n `13`; crypto_alt avg `0.0469` n `237`; crypto_major avg `0.027` n `8`; equity avg `-0.0677` n `151`; fx avg `0.0011` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0082` n `20`; unknown avg `-0.3456` n `1198`
- 1h: commodity avg `0.1345` n `13`; crypto_alt avg `0.0372` n `237`; crypto_major avg `0.004` n `8`; equity avg `-0.3039` n `151`; fx avg `-0.0047` n `6`; index avg `-0.0445` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.2911` n `1196`
- 4h: commodity avg `0.2403` n `13`; crypto_alt avg `-0.2939` n `237`; crypto_major avg `-0.1362` n `8`; equity avg `-0.697` n `151`; fx avg `-0.0062` n `6`; index avg `-0.0973` n `26`; metal avg `-0.0923` n `20`; unknown avg `1.1474` n `1180`
- 24h: commodity avg `0.3116` n `13`; crypto_alt avg `0.5434` n `237`; crypto_major avg `-0.3667` n `8`; equity avg `-2.0542` n `151`; fx avg `-0.0148` n `6`; index avg `-0.2823` n `26`; metal avg `-0.3028` n `20`; unknown avg `0.5213` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
