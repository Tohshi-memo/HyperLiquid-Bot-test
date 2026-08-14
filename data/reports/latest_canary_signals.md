# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T11:12:19.206090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0578` n `12`; crypto_alt avg `-0.1364` n `230`; crypto_major avg `-0.1226` n `8`; equity avg `0.2032` n `113`; fx avg `-0.0017` n `6`; index avg `0.0269` n `25`; metal avg `-0.0202` n `20`; unknown avg `2.5434` n `787`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.0838` n `230`; crypto_major avg `-0.1664` n `8`; equity avg `0.1565` n `113`; fx avg `0.0093` n `6`; index avg `0.0135` n `25`; metal avg `-0.0608` n `20`; unknown avg `2.6228` n `787`
- 4h: commodity avg `-0.1924` n `12`; crypto_alt avg `-0.3348` n `230`; crypto_major avg `-0.221` n `8`; equity avg `0.6419` n `113`; fx avg `-0.0257` n `6`; index avg `0.0898` n `25`; metal avg `0.0879` n `20`; unknown avg `1.4955` n `787`
- 24h: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.8586` n `230`; crypto_major avg `-0.8023` n `8`; equity avg `1.9223` n `113`; fx avg `-0.0538` n `6`; index avg `0.3641` n `25`; metal avg `-0.2552` n `20`; unknown avg `1.0543` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
