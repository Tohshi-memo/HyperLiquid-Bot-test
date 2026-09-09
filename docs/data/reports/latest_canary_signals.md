# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T14:52:30.346421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `-0.2126` n `233`; crypto_major avg `-0.2602` n `8`; equity avg `-0.0555` n `134`; fx avg `0.014` n `6`; index avg `0.0037` n `26`; metal avg `0.0119` n `20`; unknown avg `0.286` n `797`
- 1h: commodity avg `0.1486` n `12`; crypto_alt avg `-0.2507` n `233`; crypto_major avg `-0.4229` n `8`; equity avg `-0.0566` n `134`; fx avg `0.0085` n `6`; index avg `-0.0038` n `26`; metal avg `0.1275` n `20`; unknown avg `7.5474` n `775`
- 4h: commodity avg `0.091` n `12`; crypto_alt avg `0.0696` n `233`; crypto_major avg `-0.0078` n `8`; equity avg `0.5151` n `134`; fx avg `0.019` n `6`; index avg `0.0854` n `26`; metal avg `0.4997` n `20`; unknown avg `6.1893` n `766`
- 24h: commodity avg `0.4644` n `12`; crypto_alt avg `-0.291` n `232`; crypto_major avg `0.6178` n `8`; equity avg `0.0943` n `134`; fx avg `-0.0951` n `6`; index avg `-0.1004` n `26`; metal avg `0.5046` n `20`; unknown avg `6.7374` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
