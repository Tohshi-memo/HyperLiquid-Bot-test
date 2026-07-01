# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T19:52:25.511543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.2447` n `228`; crypto_major avg `-0.2636` n `8`; equity avg `-0.2705` n `88`; fx avg `0.0013` n `6`; index avg `-0.0569` n `25`; metal avg `-0.1512` n `20`; unknown avg `0.4695` n `763`
- 1h: commodity avg `-0.0806` n `12`; crypto_alt avg `-0.2206` n `228`; crypto_major avg `-0.3346` n `8`; equity avg `-0.0815` n `88`; fx avg `0.0028` n `6`; index avg `-0.036` n `25`; metal avg `-0.1508` n `20`; unknown avg `0.4769` n `763`
- 4h: commodity avg `-0.0667` n `12`; crypto_alt avg `-1.0144` n `228`; crypto_major avg `-0.5326` n `8`; equity avg `-0.7115` n `88`; fx avg `0.0035` n `6`; index avg `-0.1357` n `25`; metal avg `-0.3773` n `20`; unknown avg `-0.0259` n `761`
- 24h: commodity avg `-0.6315` n `12`; crypto_alt avg `1.1775` n `228`; crypto_major avg `1.1133` n `8`; equity avg `-1.3759` n `88`; fx avg `-0.0004` n `6`; index avg `-0.5166` n `25`; metal avg `0.0696` n `20`; unknown avg `0.4154` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
