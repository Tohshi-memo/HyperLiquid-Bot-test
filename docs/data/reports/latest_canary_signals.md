# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T18:07:24.448155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `0.0103` n `232`; crypto_major avg `-0.0677` n `8`; equity avg `0.0226` n `134`; fx avg `0.0011` n `6`; index avg `0.0046` n `26`; metal avg `-0.0112` n `20`; unknown avg `1.0852` n `774`
- 1h: commodity avg `0.0832` n `12`; crypto_alt avg `0.0093` n `232`; crypto_major avg `0.0129` n `8`; equity avg `0.0798` n `134`; fx avg `-0.0007` n `6`; index avg `0.0066` n `26`; metal avg `-0.0214` n `20`; unknown avg `-0.3754` n `774`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.5116` n `232`; crypto_major avg `-0.4169` n `8`; equity avg `0.1719` n `134`; fx avg `-0.05` n `6`; index avg `0.0405` n `26`; metal avg `0.0447` n `20`; unknown avg `-0.6505` n `768`
- 24h: commodity avg `0.1873` n `12`; crypto_alt avg `0.3257` n `232`; crypto_major avg `-0.8736` n `8`; equity avg `0.5124` n `134`; fx avg `-0.1121` n `6`; index avg `0.0872` n `26`; metal avg `-0.014` n `20`; unknown avg `1.2465` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
