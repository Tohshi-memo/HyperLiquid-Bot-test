# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T16:52:16.667959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0839` n `12`; crypto_alt avg `0.2047` n `228`; crypto_major avg `0.2933` n `8`; equity avg `0.0598` n `67`; fx avg `-0.0002` n `6`; index avg `0.0348` n `23`; metal avg `0.0316` n `18`; unknown avg `0.0756` n `418`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `-0.3297` n `228`; crypto_major avg `-0.1872` n `8`; equity avg `0.376` n `67`; fx avg `-0.0039` n `6`; index avg `0.3721` n `23`; metal avg `0.3627` n `18`; unknown avg `-0.6233` n `418`
- 4h: commodity avg `0.7303` n `12`; crypto_alt avg `-0.0523` n `228`; crypto_major avg `-0.4762` n `8`; equity avg `-0.7023` n `67`; fx avg `-0.05` n `6`; index avg `-0.7` n `23`; metal avg `0.0654` n `18`; unknown avg `-0.4576` n `418`
- 24h: commodity avg `-1.2719` n `12`; crypto_alt avg `-1.0028` n `228`; crypto_major avg `-0.8228` n `8`; equity avg `-0.2113` n `67`; fx avg `-0.0742` n `6`; index avg `-0.3661` n `23`; metal avg `-0.8192` n `18`; unknown avg `-0.7349` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
