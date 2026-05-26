# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T07:52:16.967248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `0.3629` n `228`; crypto_major avg `0.2269` n `8`; equity avg `0.0703` n `67`; fx avg `-0.0067` n `6`; index avg `0.0727` n `23`; metal avg `0.1331` n `18`; unknown avg `-0.0135` n `417`
- 1h: commodity avg `0.6147` n `12`; crypto_alt avg `-0.4256` n `228`; crypto_major avg `-0.3065` n `8`; equity avg `-0.2435` n `67`; fx avg `0.0106` n `6`; index avg `-0.04` n `23`; metal avg `-0.0873` n `18`; unknown avg `0.1004` n `417`
- 4h: commodity avg `0.6275` n `12`; crypto_alt avg `0.5938` n `228`; crypto_major avg `0.2433` n `8`; equity avg `-0.2037` n `67`; fx avg `-0.033` n `6`; index avg `-0.0025` n `23`; metal avg `-0.3196` n `18`; unknown avg `0.3427` n `397`
- 24h: commodity avg `0.7753` n `12`; crypto_alt avg `-0.6753` n `228`; crypto_major avg `-1.3798` n `8`; equity avg `-0.7289` n `67`; fx avg `-0.104` n `6`; index avg `-0.0929` n `23`; metal avg `-0.5511` n `18`; unknown avg `0.1313` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
