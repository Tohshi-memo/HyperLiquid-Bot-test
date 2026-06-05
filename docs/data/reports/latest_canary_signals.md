# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T01:52:20.666176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0722` n `12`; crypto_alt avg `-0.176` n `228`; crypto_major avg `-0.1349` n `8`; equity avg `0.0836` n `74`; fx avg `0.0122` n `6`; index avg `-0.0167` n `23`; metal avg `-0.2102` n `18`; unknown avg `0.9666` n `424`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `-0.2689` n `228`; crypto_major avg `-0.0598` n `8`; equity avg `0.127` n `74`; fx avg `0.0803` n `6`; index avg `0.0396` n `23`; metal avg `-0.5326` n `18`; unknown avg `1.2209` n `424`
- 4h: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0206` n `228`; crypto_major avg `0.2022` n `8`; equity avg `-1.087` n `74`; fx avg `0.1512` n `6`; index avg `-0.9598` n `23`; metal avg `-1.0112` n `18`; unknown avg `-0.2521` n `424`
- 24h: commodity avg `-0.1708` n `12`; crypto_alt avg `-3.2508` n `228`; crypto_major avg `-1.3235` n `8`; equity avg `-0.7501` n `73`; fx avg `0.2193` n `6`; index avg `-0.4665` n `23`; metal avg `-0.2557` n `18`; unknown avg `-0.4067` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
