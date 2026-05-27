# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T19:22:20.082595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `0.0347` n `228`; crypto_major avg `0.0305` n `8`; equity avg `-0.0037` n `67`; fx avg `0.0029` n `6`; index avg `0.0161` n `23`; metal avg `-0.0293` n `18`; unknown avg `0.1075` n `419`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.7197` n `228`; crypto_major avg `0.3505` n `8`; equity avg `0.0394` n `67`; fx avg `0.0136` n `6`; index avg `0.0723` n `23`; metal avg `-0.0726` n `18`; unknown avg `0.2443` n `418`
- 4h: commodity avg `-0.716` n `12`; crypto_alt avg `-0.5894` n `228`; crypto_major avg `-0.4919` n `8`; equity avg `0.4033` n `67`; fx avg `0.0317` n `6`; index avg `0.3229` n `23`; metal avg `0.2513` n `18`; unknown avg `-0.1201` n `418`
- 24h: commodity avg `-1.4034` n `12`; crypto_alt avg `0.0347` n `228`; crypto_major avg `-0.2163` n `8`; equity avg `-0.0455` n `67`; fx avg `-0.0701` n `6`; index avg `-0.4423` n `23`; metal avg `-1.1569` n `18`; unknown avg `-0.2995` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
