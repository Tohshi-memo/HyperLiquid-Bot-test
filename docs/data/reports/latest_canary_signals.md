# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T09:52:24.143643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0495` n `12`; crypto_alt avg `0.0558` n `228`; crypto_major avg `-0.0558` n `8`; equity avg `0.0811` n `67`; fx avg `-0.0061` n `6`; index avg `0.0199` n `23`; metal avg `0.0977` n `18`; unknown avg `-0.0166` n `397`
- 1h: commodity avg `-0.216` n `12`; crypto_alt avg `-0.0025` n `228`; crypto_major avg `0.0762` n `8`; equity avg `0.1869` n `67`; fx avg `-0.01` n `6`; index avg `0.0337` n `23`; metal avg `0.1622` n `18`; unknown avg `-0.1874` n `397`
- 4h: commodity avg `0.1581` n `12`; crypto_alt avg `0.2607` n `228`; crypto_major avg `0.3151` n `8`; equity avg `0.1541` n `67`; fx avg `0.0371` n `6`; index avg `0.111` n `23`; metal avg `0.3796` n `18`; unknown avg `0.3028` n `387`
- 24h: commodity avg `-0.0888` n `12`; crypto_alt avg `0.0529` n `228`; crypto_major avg `-0.2452` n `8`; equity avg `0.5599` n `67`; fx avg `-0.0041` n `6`; index avg `-0.0505` n `23`; metal avg `0.6344` n `18`; unknown avg `1.0333` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
