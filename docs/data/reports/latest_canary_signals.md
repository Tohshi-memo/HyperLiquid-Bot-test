# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T16:22:25.791160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `12`; crypto_alt avg `-0.1171` n `228`; crypto_major avg `0.13` n `8`; equity avg `0.0126` n `67`; fx avg `0.0224` n `6`; index avg `0.0747` n `23`; metal avg `0.0511` n `18`; unknown avg `0.7608` n `418`
- 1h: commodity avg `-0.126` n `12`; crypto_alt avg `-0.4462` n `228`; crypto_major avg `-0.3615` n `8`; equity avg `-0.126` n `67`; fx avg `0.0255` n `6`; index avg `0.0481` n `23`; metal avg `-0.0348` n `18`; unknown avg `0.9037` n `418`
- 4h: commodity avg `0.754` n `12`; crypto_alt avg `-0.9511` n `228`; crypto_major avg `-0.5436` n `8`; equity avg `-0.1346` n `67`; fx avg `0.0001` n `6`; index avg `0.3428` n `23`; metal avg `-0.2473` n `18`; unknown avg `-0.0104` n `415`
- 24h: commodity avg `0.9914` n `12`; crypto_alt avg `-1.2496` n `228`; crypto_major avg `-0.9302` n `8`; equity avg `-0.4432` n `67`; fx avg `-0.1263` n `6`; index avg `0.3855` n `23`; metal avg `-1.1964` n `18`; unknown avg `-0.4339` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
