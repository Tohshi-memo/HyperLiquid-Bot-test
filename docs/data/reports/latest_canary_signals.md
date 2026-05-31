# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T19:22:23.246258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0066` n `228`; crypto_major avg `0.0175` n `8`; equity avg `0.0385` n `69`; fx avg `0.0028` n `6`; index avg `0.0851` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.0003` n `421`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.0617` n `228`; crypto_major avg `-0.0189` n `8`; equity avg `0.016` n `69`; fx avg `-0.0049` n `6`; index avg `0.1146` n `23`; metal avg `0.0147` n `18`; unknown avg `0.1063` n `421`
- 4h: commodity avg `0.1486` n `12`; crypto_alt avg `-0.2958` n `228`; crypto_major avg `-0.5649` n `8`; equity avg `0.121` n `69`; fx avg `-0.0113` n `6`; index avg `0.3559` n `23`; metal avg `-0.0263` n `18`; unknown avg `-0.1298` n `421`
- 24h: commodity avg `0.6123` n `12`; crypto_alt avg `-1.4616` n `228`; crypto_major avg `-0.91` n `8`; equity avg `0.8435` n `69`; fx avg `-0.0187` n `6`; index avg `0.2227` n `23`; metal avg `-0.1278` n `18`; unknown avg `0.1139` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2442`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
