# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T06:22:35.276769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0949` n `230`; crypto_major avg `-0.1528` n `8`; equity avg `-0.0172` n `113`; fx avg `0.0281` n `6`; index avg `-0.0043` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.0155` n `787`
- 1h: commodity avg `0.1502` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `-0.1845` n `8`; equity avg `0.028` n `113`; fx avg `0.0074` n `6`; index avg `0.0292` n `25`; metal avg `0.148` n `20`; unknown avg `0.0227` n `755`
- 4h: commodity avg `0.2449` n `12`; crypto_alt avg `-0.4873` n `230`; crypto_major avg `-0.4747` n `8`; equity avg `-0.1664` n `113`; fx avg `0.0067` n `6`; index avg `0.003` n `25`; metal avg `0.1652` n `20`; unknown avg `-0.0782` n `755`
- 24h: commodity avg `-0.2535` n `12`; crypto_alt avg `-0.5343` n `230`; crypto_major avg `-0.7988` n `8`; equity avg `0.7758` n `113`; fx avg `-0.0047` n `6`; index avg `0.259` n `25`; metal avg `-0.302` n `20`; unknown avg `0.9022` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2359`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
