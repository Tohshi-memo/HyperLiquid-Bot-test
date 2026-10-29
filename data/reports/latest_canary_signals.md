# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T11:52:25.716054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9648` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.082` n `13`; crypto_alt avg `0.1103` n `238`; crypto_major avg `0.2728` n `8`; equity avg `-0.1281` n `155`; fx avg `0.0023` n `6`; index avg `-0.0152` n `27`; metal avg `-0.0894` n `20`; unknown avg `0.184` n `1239`
- 1h: commodity avg `0.1137` n `13`; crypto_alt avg `-0.1347` n `238`; crypto_major avg `0.1382` n `8`; equity avg `-0.2706` n `155`; fx avg `-0.0008` n `6`; index avg `-0.0667` n `27`; metal avg `-0.1616` n `20`; unknown avg `-0.1523` n `1233`
- 4h: commodity avg `-0.0471` n `13`; crypto_alt avg `1.4849` n `238`; crypto_major avg `1.8124` n `8`; equity avg `0.3402` n `155`; fx avg `0.0396` n `6`; index avg `0.0534` n `27`; metal avg `-0.1524` n `20`; unknown avg `2.4824` n `1120`
- 24h: commodity avg `-0.1921` n `13`; crypto_alt avg `-1.9422` n `238`; crypto_major avg `-0.602` n `8`; equity avg `-1.6029` n `155`; fx avg `0.0511` n `6`; index avg `-0.0776` n `27`; metal avg `-0.5473` n `20`; unknown avg `13.5665` n `982`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
