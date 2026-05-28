# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T12:22:21.876508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0751` n `12`; crypto_alt avg `-0.244` n `228`; crypto_major avg `-0.2958` n `8`; equity avg `-0.1191` n `67`; fx avg `0.0042` n `6`; index avg `-0.0257` n `23`; metal avg `-0.1348` n `18`; unknown avg `0.0113` n `419`
- 1h: commodity avg `0.1155` n `12`; crypto_alt avg `-0.3324` n `228`; crypto_major avg `-0.2999` n `8`; equity avg `0.0919` n `67`; fx avg `0.0519` n `6`; index avg `0.0694` n `23`; metal avg `-0.2872` n `18`; unknown avg `-0.2426` n `419`
- 4h: commodity avg `0.4196` n `12`; crypto_alt avg `-0.8856` n `228`; crypto_major avg `-0.447` n `8`; equity avg `-0.2866` n `67`; fx avg `0.0237` n `6`; index avg `-0.1392` n `23`; metal avg `-0.6305` n `18`; unknown avg `-0.3221` n `419`
- 24h: commodity avg `1.3856` n `12`; crypto_alt avg `-6.1624` n `228`; crypto_major avg `-4.6061` n `8`; equity avg `-2.0079` n `67`; fx avg `-0.0463` n `6`; index avg `-1.3219` n `23`; metal avg `-1.9839` n `18`; unknown avg `-2.1546` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
