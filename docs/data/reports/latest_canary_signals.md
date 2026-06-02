# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T03:22:19.875956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `0.049` n `228`; crypto_major avg `-0.0589` n `8`; equity avg `-0.0202` n `69`; fx avg `0.0025` n `6`; index avg `-0.0667` n `23`; metal avg `-0.1106` n `18`; unknown avg `0.0462` n `422`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.9926` n `228`; crypto_major avg `0.8716` n `8`; equity avg `0.1936` n `69`; fx avg `0.0181` n `6`; index avg `-0.0146` n `23`; metal avg `0.0455` n `18`; unknown avg `-0.3038` n `422`
- 4h: commodity avg `-0.2821` n `12`; crypto_alt avg `-0.4342` n `228`; crypto_major avg `-0.3248` n `8`; equity avg `-0.5536` n `69`; fx avg `0.0631` n `6`; index avg `-0.5822` n `23`; metal avg `0.0753` n `18`; unknown avg `-0.2801` n `422`
- 24h: commodity avg `-0.4104` n `12`; crypto_alt avg `-1.2469` n `228`; crypto_major avg `-1.2558` n `8`; equity avg `-0.9036` n `69`; fx avg `0.0059` n `6`; index avg `-0.8976` n `23`; metal avg `-0.1564` n `18`; unknown avg `1.4009` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
