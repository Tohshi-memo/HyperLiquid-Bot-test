# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T21:22:29.833836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `0.0211` n `8`; equity avg `-0.0097` n `114`; fx avg `-0.002` n `6`; index avg `0.0048` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.0169` n `792`
- 1h: commodity avg `0.0307` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `0.1777` n `8`; equity avg `0.0596` n `114`; fx avg `-0.0046` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0274` n `20`; unknown avg `-0.0451` n `792`
- 4h: commodity avg `0.2543` n `12`; crypto_alt avg `-0.251` n `230`; crypto_major avg `-0.2001` n `8`; equity avg `-0.3585` n `114`; fx avg `-0.0087` n `6`; index avg `-0.0809` n `25`; metal avg `-0.0713` n `20`; unknown avg `-0.03` n `792`
- 24h: commodity avg `0.4256` n `12`; crypto_alt avg `0.2929` n `230`; crypto_major avg `1.0337` n `8`; equity avg `1.048` n `114`; fx avg `0.0025` n `6`; index avg `0.0625` n `25`; metal avg `0.1992` n `20`; unknown avg `0.2084` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
