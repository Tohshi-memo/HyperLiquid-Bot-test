# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T18:52:31.899047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `13`; crypto_alt avg `-0.3379` n `234`; crypto_major avg `-0.3692` n `8`; equity avg `0.0043` n `142`; fx avg `0.0062` n `6`; index avg `0.0019` n `26`; metal avg `-0.027` n `20`; unknown avg `0.2312` n `975`
- 1h: commodity avg `0.1516` n `13`; crypto_alt avg `-0.3864` n `234`; crypto_major avg `-0.32` n `8`; equity avg `-0.1635` n `142`; fx avg `0.0432` n `6`; index avg `-0.019` n `26`; metal avg `-0.0225` n `20`; unknown avg `-0.2651` n `973`
- 4h: commodity avg `0.064` n `13`; crypto_alt avg `1.3068` n `234`; crypto_major avg `0.6583` n `8`; equity avg `1.1099` n `142`; fx avg `-0.0396` n `6`; index avg `0.2095` n `26`; metal avg `0.08` n `20`; unknown avg `1.6496` n `955`
- 24h: commodity avg `-0.0623` n `13`; crypto_alt avg `0.0149` n `234`; crypto_major avg `0.0131` n `8`; equity avg `1.0316` n `142`; fx avg `-0.0781` n `6`; index avg `0.1643` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.0` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
