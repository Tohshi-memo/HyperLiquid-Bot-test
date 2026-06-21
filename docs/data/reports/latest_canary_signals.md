# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T14:07:31.572891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.016` n `228`; crypto_major avg `0.0538` n `8`; equity avg `0.0126` n `78`; fx avg `0.0172` n `6`; index avg `-0.0034` n `23`; metal avg `0.0147` n `18`; unknown avg `0.0363` n `702`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `0.03` n `228`; crypto_major avg `0.0747` n `8`; equity avg `-0.0576` n `78`; fx avg `0.1011` n `6`; index avg `0.0092` n `23`; metal avg `-0.0119` n `18`; unknown avg `0.0976` n `702`
- 4h: commodity avg `0.0508` n `12`; crypto_alt avg `-0.0498` n `228`; crypto_major avg `-0.2671` n `8`; equity avg `-0.0902` n `78`; fx avg `0.0336` n `6`; index avg `-0.0081` n `23`; metal avg `-0.0593` n `18`; unknown avg `0.119` n `702`
- 24h: commodity avg `-0.1684` n `12`; crypto_alt avg `2.7724` n `228`; crypto_major avg `0.9313` n `8`; equity avg `0.6774` n `78`; fx avg `0.0711` n `6`; index avg `0.0577` n `23`; metal avg `-0.0235` n `18`; unknown avg `1.0307` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
