# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T18:32:28.426472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `0.0011` n `8`; equity avg `0.0545` n `114`; fx avg `-0.0104` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0614` n `20`; unknown avg `0.0896` n `792`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `0.1532` n `8`; equity avg `-0.0451` n `114`; fx avg `-0.0153` n `6`; index avg `-0.0234` n `25`; metal avg `-0.0572` n `20`; unknown avg `-0.0623` n `792`
- 4h: commodity avg `0.3875` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `0.3376` n `8`; equity avg `0.1323` n `114`; fx avg `0.016` n `6`; index avg `-0.0803` n `25`; metal avg `-0.1517` n `20`; unknown avg `0.1233` n `792`
- 24h: commodity avg `0.3342` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.9932` n `8`; equity avg `1.3152` n `114`; fx avg `0.0119` n `6`; index avg `0.1085` n `25`; metal avg `0.1442` n `20`; unknown avg `0.2353` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1665`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1528`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0998`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0845`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0834`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `669`, weak_sample_signal
