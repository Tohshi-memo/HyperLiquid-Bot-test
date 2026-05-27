# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T18:07:22.236055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0554` n `12`; crypto_alt avg `-0.3119` n `228`; crypto_major avg `-0.1885` n `8`; equity avg `-0.0371` n `67`; fx avg `-0.0062` n `6`; index avg `-0.0117` n `23`; metal avg `-0.1042` n `18`; unknown avg `-0.0212` n `418`
- 1h: commodity avg `-0.1987` n `12`; crypto_alt avg `-0.6061` n `228`; crypto_major avg `-0.5684` n `8`; equity avg `0.0415` n `67`; fx avg `-0.0197` n `6`; index avg `0.1198` n `23`; metal avg `-0.0672` n `18`; unknown avg `-0.0271` n `418`
- 4h: commodity avg `0.0588` n `12`; crypto_alt avg `-0.5848` n `228`; crypto_major avg `-0.6127` n `8`; equity avg `-0.4214` n `67`; fx avg `0.0006` n `6`; index avg `-0.1843` n `23`; metal avg `-0.135` n `18`; unknown avg `-0.3584` n `418`
- 24h: commodity avg `-1.2149` n `12`; crypto_alt avg `-1.0349` n `228`; crypto_major avg `-1.0899` n `8`; equity avg `-0.394` n `67`; fx avg `-0.0694` n `6`; index avg `-0.5007` n `23`; metal avg `-0.7935` n `18`; unknown avg `-0.978` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
