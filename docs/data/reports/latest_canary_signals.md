# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T05:52:30.088773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `13`; crypto_alt avg `-0.1771` n `239`; crypto_major avg `-0.0888` n `8`; equity avg `-0.1432` n `161`; fx avg `0.0027` n `6`; index avg `-0.0097` n `27`; metal avg `0.0078` n `20`; unknown avg `37.2222` n `1262`
- 1h: commodity avg `0.0654` n `13`; crypto_alt avg `-0.3432` n `239`; crypto_major avg `-0.3582` n `8`; equity avg `-0.6376` n `161`; fx avg `-0.0161` n `6`; index avg `-0.0442` n `27`; metal avg `0.0128` n `20`; unknown avg `2.9635` n `1254`
- 4h: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.2128` n `239`; crypto_major avg `-0.2717` n `8`; equity avg `-1.3915` n `161`; fx avg `-0.1108` n `6`; index avg `-0.1098` n `27`; metal avg `-0.0136` n `20`; unknown avg `1.5875` n `1234`
- 24h: commodity avg `0.053` n `13`; crypto_alt avg `-1.9166` n `239`; crypto_major avg `-0.9675` n `8`; equity avg `-0.9125` n `161`; fx avg `-0.1876` n `6`; index avg `-0.1033` n `27`; metal avg `-0.59` n `20`; unknown avg `1.1774` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
