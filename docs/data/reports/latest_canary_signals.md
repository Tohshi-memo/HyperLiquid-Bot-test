# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T09:07:30.288546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.0911` n `230`; crypto_major avg `0.0663` n `8`; equity avg `-0.055` n `114`; fx avg `0.0024` n `6`; index avg `-0.0047` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.0466` n `792`
- 1h: commodity avg `0.0881` n `12`; crypto_alt avg `-0.2012` n `230`; crypto_major avg `-0.1641` n `8`; equity avg `-0.0061` n `114`; fx avg `-0.0033` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0474` n `20`; unknown avg `-0.0894` n `792`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.271` n `230`; crypto_major avg `-0.0667` n `8`; equity avg `0.4303` n `114`; fx avg `-0.0081` n `6`; index avg `0.057` n `25`; metal avg `-0.0096` n `20`; unknown avg `-0.0205` n `776`
- 24h: commodity avg `-0.119` n `12`; crypto_alt avg `-0.1665` n `230`; crypto_major avg `0.4647` n `8`; equity avg `1.173` n `114`; fx avg `-0.0383` n `6`; index avg `0.1294` n `25`; metal avg `0.1576` n `20`; unknown avg `0.0523` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
