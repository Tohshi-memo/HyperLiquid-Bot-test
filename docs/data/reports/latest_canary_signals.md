# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T10:37:29.376522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `12`; crypto_alt avg `0.4255` n `232`; crypto_major avg `0.2896` n `8`; equity avg `0.0681` n `130`; fx avg `-0.0021` n `6`; index avg `0.0128` n `26`; metal avg `0.0068` n `20`; unknown avg `0.1091` n `792`
- 1h: commodity avg `-0.0662` n `12`; crypto_alt avg `0.6936` n `232`; crypto_major avg `0.4611` n `8`; equity avg `0.2499` n `130`; fx avg `-0.0089` n `6`; index avg `0.0609` n `26`; metal avg `0.1479` n `20`; unknown avg `0.4706` n `790`
- 4h: commodity avg `0.1416` n `12`; crypto_alt avg `-0.6836` n `232`; crypto_major avg `-0.6695` n `8`; equity avg `-1.2237` n `130`; fx avg `0.0255` n `6`; index avg `-0.2415` n `26`; metal avg `-0.4833` n `20`; unknown avg `0.0533` n `790`
- 24h: commodity avg `0.242` n `12`; crypto_alt avg `0.9242` n `232`; crypto_major avg `0.3196` n `8`; equity avg `-0.4603` n `130`; fx avg `0.0892` n `6`; index avg `-0.214` n `26`; metal avg `-0.6496` n `20`; unknown avg `0.1682` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0308`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
