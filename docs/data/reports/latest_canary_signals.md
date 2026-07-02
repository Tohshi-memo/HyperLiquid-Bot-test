# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T00:52:27.483477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.0643` n `228`; crypto_major avg `0.0831` n `8`; equity avg `-0.0887` n `88`; fx avg `-0.0098` n `6`; index avg `-0.0337` n `25`; metal avg `0.0904` n `20`; unknown avg `-0.1163` n `763`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.0976` n `228`; crypto_major avg `-0.3157` n `8`; equity avg `-0.23` n `88`; fx avg `0.021` n `6`; index avg `-0.0763` n `25`; metal avg `0.1594` n `20`; unknown avg `0.3052` n `763`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-0.2785` n `228`; crypto_major avg `-0.567` n `8`; equity avg `-0.4232` n `88`; fx avg `0.0472` n `6`; index avg `-0.1358` n `25`; metal avg `0.1713` n `20`; unknown avg `83.5829` n `763`
- 24h: commodity avg `-0.6614` n `12`; crypto_alt avg `1.4093` n `228`; crypto_major avg `0.7714` n `8`; equity avg `-2.009` n `88`; fx avg `-0.0272` n `6`; index avg `-0.6462` n `25`; metal avg `0.5244` n `20`; unknown avg `86.7559` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
