# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T22:37:29.613934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0379` n `232`; crypto_major avg `-0.088` n `8`; equity avg `0.0197` n `134`; fx avg `-0.0025` n `6`; index avg `-0.0019` n `26`; metal avg `0.0023` n `20`; unknown avg `10.2969` n `794`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `0.0171` n `232`; crypto_major avg `-0.2748` n `8`; equity avg `0.0406` n `134`; fx avg `-0.0025` n `6`; index avg `0.0269` n `26`; metal avg `0.01` n `20`; unknown avg `1.0122` n `792`
- 4h: commodity avg `0.0626` n `12`; crypto_alt avg `0.4391` n `232`; crypto_major avg `-0.5774` n `8`; equity avg `0.0361` n `134`; fx avg `-0.0153` n `6`; index avg `0.0441` n `26`; metal avg `-0.0014` n `20`; unknown avg `21.055` n `770`
- 24h: commodity avg `0.1711` n `12`; crypto_alt avg `3.5029` n `232`; crypto_major avg `2.4669` n `8`; equity avg `0.2762` n `134`; fx avg `-0.0508` n `6`; index avg `0.0702` n `26`; metal avg `0.0587` n `20`; unknown avg `1281.2856` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
