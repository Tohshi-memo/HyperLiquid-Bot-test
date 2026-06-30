# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T18:07:27.472037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `-0.0819` n `228`; crypto_major avg `-0.0493` n `8`; equity avg `-0.0225` n `88`; fx avg `-0.0031` n `6`; index avg `0.0006` n `23`; metal avg `0.0133` n `20`; unknown avg `0.8183` n `765`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `-0.3124` n `228`; crypto_major avg `-0.3339` n `8`; equity avg `-0.0895` n `88`; fx avg `0.0037` n `6`; index avg `-0.0125` n `23`; metal avg `0.1095` n `20`; unknown avg `0.6771` n `765`
- 4h: commodity avg `-0.2186` n `12`; crypto_alt avg `-0.3402` n `228`; crypto_major avg `-0.4526` n `8`; equity avg `0.5622` n `88`; fx avg `0.0617` n `6`; index avg `0.1027` n `23`; metal avg `0.0327` n `20`; unknown avg `0.3982` n `765`
- 24h: commodity avg `0.0769` n `12`; crypto_alt avg `-2.7366` n `228`; crypto_major avg `-2.5996` n `8`; equity avg `1.2307` n `88`; fx avg `0.1416` n `6`; index avg `0.3355` n `23`; metal avg `0.2004` n `20`; unknown avg `9.2679` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
