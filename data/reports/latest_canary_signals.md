# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T20:37:30.552265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.0092` n `230`; crypto_major avg `0.0445` n `8`; equity avg `0.0742` n `113`; fx avg `0.0032` n `6`; index avg `0.0134` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0202` n `787`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `0.0142` n `230`; crypto_major avg `0.0676` n `8`; equity avg `0.043` n `113`; fx avg `0.0031` n `6`; index avg `0.0128` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0225` n `787`
- 4h: commodity avg `-0.2742` n `12`; crypto_alt avg `0.129` n `230`; crypto_major avg `0.4247` n `8`; equity avg `0.1032` n `113`; fx avg `0.0122` n `6`; index avg `0.0162` n `25`; metal avg `-0.1016` n `20`; unknown avg `0.195` n `787`
- 24h: commodity avg `-0.4728` n `12`; crypto_alt avg `-0.4687` n `230`; crypto_major avg `0.2231` n `8`; equity avg `1.6412` n `113`; fx avg `0.0144` n `6`; index avg `0.3269` n `25`; metal avg `-0.5052` n `20`; unknown avg `0.0023` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.245`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
