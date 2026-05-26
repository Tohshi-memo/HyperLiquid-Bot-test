# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T09:37:17.848675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.0872` n `228`; crypto_major avg `-0.1003` n `8`; equity avg `0.0358` n `67`; fx avg `0.008` n `6`; index avg `0.0664` n `23`; metal avg `-0.1285` n `18`; unknown avg `-0.0526` n `417`
- 1h: commodity avg `-0.0961` n `12`; crypto_alt avg `0.1467` n `228`; crypto_major avg `-0.1178` n `8`; equity avg `0.2167` n `67`; fx avg `0.0146` n `6`; index avg `0.1238` n `23`; metal avg `-0.0671` n `18`; unknown avg `-0.1431` n `417`
- 4h: commodity avg `0.5994` n `12`; crypto_alt avg `-0.3517` n `228`; crypto_major avg `-0.5483` n `8`; equity avg `0.1632` n `67`; fx avg `0.0254` n `6`; index avg `0.0765` n `23`; metal avg `-0.4392` n `18`; unknown avg `-0.2439` n `397`
- 24h: commodity avg `0.9791` n `12`; crypto_alt avg `-0.6991` n `228`; crypto_major avg `-1.7913` n `8`; equity avg `-0.4955` n `67`; fx avg `-0.0771` n `6`; index avg `0.0112` n `23`; metal avg `-0.7803` n `18`; unknown avg `-0.3331` n `387`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
