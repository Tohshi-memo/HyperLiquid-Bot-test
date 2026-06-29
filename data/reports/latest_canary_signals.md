# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T02:07:31.672446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `12`; crypto_alt avg `-0.2746` n `228`; crypto_major avg `-0.3942` n `8`; equity avg `-0.1681` n `88`; fx avg `0.0096` n `6`; index avg `-0.0516` n `23`; metal avg `0.0477` n `20`; unknown avg `-0.0338` n `764`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `-0.2164` n `228`; crypto_major avg `-0.3799` n `8`; equity avg `-0.1661` n `88`; fx avg `0.0448` n `6`; index avg `-0.0461` n `23`; metal avg `-0.1068` n `20`; unknown avg `-0.1915` n `764`
- 4h: commodity avg `0.0794` n `12`; crypto_alt avg `-0.2696` n `228`; crypto_major avg `-0.5741` n `8`; equity avg `-0.6399` n `88`; fx avg `0.0812` n `6`; index avg `-0.2446` n `23`; metal avg `-0.2759` n `20`; unknown avg `1.3729` n `762`
- 24h: commodity avg `-0.4673` n `12`; crypto_alt avg `-0.5965` n `228`; crypto_major avg `-0.9261` n `8`; equity avg `-0.1709` n `88`; fx avg `0.0248` n `6`; index avg `-0.0714` n `23`; metal avg `-0.2519` n `20`; unknown avg `15.4846` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
