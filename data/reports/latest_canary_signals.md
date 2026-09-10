# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T06:22:31.634449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.4161` n `233`; crypto_major avg `-0.3138` n `8`; equity avg `-0.1242` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0657` n `20`; unknown avg `0.1946` n `797`
- 1h: commodity avg `-0.1147` n `12`; crypto_alt avg `-0.3542` n `233`; crypto_major avg `-0.2853` n `8`; equity avg `-0.078` n `134`; fx avg `0.0116` n `6`; index avg `0.0195` n `26`; metal avg `-0.0321` n `20`; unknown avg `-0.035` n `773`
- 4h: commodity avg `-0.1709` n `12`; crypto_alt avg `0.4774` n `233`; crypto_major avg `0.136` n `8`; equity avg `0.2834` n `134`; fx avg `0.0084` n `6`; index avg `0.1156` n `26`; metal avg `0.016` n `20`; unknown avg `123.9157` n `767`
- 24h: commodity avg `-0.1051` n `12`; crypto_alt avg `-4.1225` n `233`; crypto_major avg `-2.9846` n `8`; equity avg `-1.187` n `134`; fx avg `0.069` n `6`; index avg `-0.1166` n `26`; metal avg `0.268` n `20`; unknown avg `0.1275` n `670`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
