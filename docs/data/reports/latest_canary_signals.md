# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T17:37:39.302532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `0.12` n `230`; crypto_major avg `0.2744` n `8`; equity avg `0.1548` n `108`; fx avg `0.0021` n `6`; index avg `0.0251` n `25`; metal avg `0.0576` n `20`; unknown avg `-0.0772` n `782`
- 1h: commodity avg `-0.224` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `0.104` n `8`; equity avg `-0.0505` n `108`; fx avg `-0.0043` n `6`; index avg `-0.0067` n `25`; metal avg `0.0323` n `20`; unknown avg `-0.066` n `782`
- 4h: commodity avg `-0.2048` n `12`; crypto_alt avg `0.6851` n `230`; crypto_major avg `1.1648` n `8`; equity avg `0.1141` n `108`; fx avg `-0.0179` n `6`; index avg `-0.1103` n `25`; metal avg `0.2996` n `20`; unknown avg `0.3115` n `782`
- 24h: commodity avg `-0.1454` n `12`; crypto_alt avg `0.8006` n `230`; crypto_major avg `0.8302` n `8`; equity avg `-0.2311` n `108`; fx avg `0.0039` n `6`; index avg `-0.0266` n `25`; metal avg `0.6455` n `20`; unknown avg `0.7932` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
