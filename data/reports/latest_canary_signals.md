# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T16:22:26.798275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.3254` n `228`; crypto_major avg `-0.3644` n `8`; equity avg `0.0139` n `88`; fx avg `-0.0029` n `6`; index avg `0.0165` n `23`; metal avg `0.0423` n `20`; unknown avg `-0.0931` n `765`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `0.0662` n `228`; crypto_major avg `0.0838` n `8`; equity avg `0.4034` n `88`; fx avg `-0.0209` n `6`; index avg `0.0667` n `23`; metal avg `0.0755` n `20`; unknown avg `0.0859` n `765`
- 4h: commodity avg `-0.1553` n `12`; crypto_alt avg `0.4833` n `228`; crypto_major avg `-0.1074` n `8`; equity avg `0.8139` n `88`; fx avg `0.0776` n `6`; index avg `0.2195` n `23`; metal avg `0.0583` n `20`; unknown avg `-0.3851` n `765`
- 24h: commodity avg `0.2132` n `12`; crypto_alt avg `-1.6382` n `228`; crypto_major avg `-0.9618` n `8`; equity avg `1.7704` n `88`; fx avg `0.1313` n `6`; index avg `0.3766` n `23`; metal avg `0.4201` n `20`; unknown avg `7.9405` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
