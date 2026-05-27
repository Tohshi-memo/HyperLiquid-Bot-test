# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T10:52:20.915430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.0736` n `228`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0351` n `67`; fx avg `0.0002` n `6`; index avg `-0.0159` n `23`; metal avg `-0.6144` n `18`; unknown avg `-0.1942` n `418`
- 1h: commodity avg `0.238` n `12`; crypto_alt avg `0.1189` n `228`; crypto_major avg `-0.0644` n `8`; equity avg `-0.0205` n `67`; fx avg `-0.0261` n `6`; index avg `0.0196` n `23`; metal avg `-0.7924` n `18`; unknown avg `-0.0721` n `418`
- 4h: commodity avg `-0.3074` n `12`; crypto_alt avg `-0.4327` n `228`; crypto_major avg `0.001` n `8`; equity avg `0.586` n `67`; fx avg `-0.0593` n `6`; index avg `0.2437` n `23`; metal avg `-0.5352` n `18`; unknown avg `-0.5198` n `418`
- 24h: commodity avg `-0.9284` n `12`; crypto_alt avg `-2.3095` n `228`; crypto_major avg `-1.0257` n `8`; equity avg `0.5874` n `67`; fx avg `-0.0556` n `6`; index avg `0.6645` n `23`; metal avg `-1.2942` n `18`; unknown avg `0.1059` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
