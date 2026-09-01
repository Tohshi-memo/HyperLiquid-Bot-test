# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T07:07:29.644443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0803` n `12`; crypto_alt avg `0.0585` n `232`; crypto_major avg `-0.0742` n `8`; equity avg `0.0145` n `130`; fx avg `0.0003` n `6`; index avg `0.0072` n `26`; metal avg `0.0` n `20`; unknown avg `0.0507` n `790`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0571` n `232`; crypto_major avg `-0.3011` n `8`; equity avg `-0.1702` n `130`; fx avg `-0.0032` n `6`; index avg `-0.0231` n `26`; metal avg `-0.0768` n `20`; unknown avg `0.0803` n `788`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.5671` n `232`; crypto_major avg `0.3006` n `8`; equity avg `0.3003` n `130`; fx avg `0.0228` n `6`; index avg `0.0516` n `26`; metal avg `-0.0253` n `20`; unknown avg `0.0879` n `770`
- 24h: commodity avg `0.5063` n `12`; crypto_alt avg `1.569` n `232`; crypto_major avg `1.2331` n `8`; equity avg `0.4753` n `130`; fx avg `0.0555` n `6`; index avg `-0.0006` n `26`; metal avg `-0.1885` n `20`; unknown avg `0.2311` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
