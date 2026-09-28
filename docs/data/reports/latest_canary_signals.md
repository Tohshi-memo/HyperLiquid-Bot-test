# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T03:52:33.729229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4337` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `0.2043` n `234`; crypto_major avg `0.0248` n `8`; equity avg `0.1188` n `141`; fx avg `-0.0097` n `6`; index avg `0.0209` n `26`; metal avg `0.035` n `20`; unknown avg `0.0572` n `962`
- 1h: commodity avg `0.053` n `12`; crypto_alt avg `-0.641` n `234`; crypto_major avg `-0.1756` n `8`; equity avg `-0.09` n `141`; fx avg `-0.0099` n `6`; index avg `-0.0014` n `26`; metal avg `0.0227` n `20`; unknown avg `0.0424` n `954`
- 4h: commodity avg `0.0493` n `12`; crypto_alt avg `-2.3693` n `234`; crypto_major avg `-1.5535` n `8`; equity avg `-1.3739` n `141`; fx avg `0.0805` n `6`; index avg `-0.1198` n `26`; metal avg `-0.5298` n `20`; unknown avg `130.6309` n `936`
- 24h: commodity avg `-0.384` n `12`; crypto_alt avg `-1.1995` n `234`; crypto_major avg `-1.3403` n `8`; equity avg `-1.4458` n `141`; fx avg `0.0517` n `6`; index avg `-0.1469` n `26`; metal avg `-0.6897` n `20`; unknown avg `12.9493` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
