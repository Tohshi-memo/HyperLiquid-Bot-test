# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T23:52:26.487470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.0069` n `228`; crypto_major avg `-0.039` n `8`; equity avg `0.0445` n `88`; fx avg `0.0071` n `6`; index avg `0.0015` n `23`; metal avg `0.0502` n `20`; unknown avg `0.0077` n `764`
- 1h: commodity avg `-0.1082` n `12`; crypto_alt avg `0.7313` n `228`; crypto_major avg `1.0108` n `8`; equity avg `0.1658` n `88`; fx avg `0.0016` n `6`; index avg `-0.017` n `23`; metal avg `0.0344` n `20`; unknown avg `0.7204` n `762`
- 4h: commodity avg `-0.5325` n `12`; crypto_alt avg `0.2553` n `228`; crypto_major avg `0.5139` n `8`; equity avg `0.4174` n `88`; fx avg `-0.0432` n `6`; index avg `0.1194` n `23`; metal avg `-0.1057` n `20`; unknown avg `0.8967` n `762`
- 24h: commodity avg `-0.3216` n `12`; crypto_alt avg `-0.219` n `228`; crypto_major avg `-0.2933` n `8`; equity avg `0.5085` n `88`; fx avg `-0.0859` n `6`; index avg `0.1257` n `23`; metal avg `-0.1204` n `20`; unknown avg `15.31` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
