# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T00:07:31.521738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `0.1365` n `228`; crypto_major avg `0.0648` n `8`; equity avg `-0.0458` n `86`; fx avg `-0.002` n `6`; index avg `0.0046` n `23`; metal avg `-0.0861` n `20`; unknown avg `-0.065` n `749`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `0.3267` n `228`; crypto_major avg `0.3893` n `8`; equity avg `0.0595` n `86`; fx avg `0.0031` n `6`; index avg `0.0165` n `23`; metal avg `-0.1223` n `20`; unknown avg `1.7473` n `749`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `0.9708` n `228`; crypto_major avg `0.7572` n `8`; equity avg `-0.2393` n `86`; fx avg `-0.016` n `6`; index avg `-0.0487` n `23`; metal avg `-0.2016` n `20`; unknown avg `0.9385` n `749`
- 24h: commodity avg `0.3333` n `12`; crypto_alt avg `-1.322` n `228`; crypto_major avg `-1.3111` n `8`; equity avg `-2.5101` n `86`; fx avg `0.0353` n `6`; index avg `-0.1143` n `23`; metal avg `0.0921` n `20`; unknown avg `1.4833` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
