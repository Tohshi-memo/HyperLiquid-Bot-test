# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T09:37:27.204402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.1867` n `228`; crypto_major avg `0.2392` n `8`; equity avg `0.2416` n `74`; fx avg `0.0172` n `6`; index avg `0.1367` n `23`; metal avg `0.1479` n `18`; unknown avg `0.4315` n `643`
- 1h: commodity avg `0.1214` n `12`; crypto_alt avg `0.7996` n `228`; crypto_major avg `0.709` n `8`; equity avg `0.5611` n `74`; fx avg `0.0031` n `6`; index avg `0.3516` n `23`; metal avg `0.2452` n `18`; unknown avg `0.8925` n `643`
- 4h: commodity avg `-0.8625` n `12`; crypto_alt avg `0.9687` n `228`; crypto_major avg `0.6643` n `8`; equity avg `0.4085` n `74`; fx avg `-0.0241` n `6`; index avg `0.2685` n `23`; metal avg `0.8182` n `18`; unknown avg `0.2218` n `515`
- 24h: commodity avg `-2.6499` n `12`; crypto_alt avg `2.1549` n `228`; crypto_major avg `2.236` n `8`; equity avg `3.0874` n `74`; fx avg `-0.0112` n `6`; index avg `1.7107` n `23`; metal avg `3.5474` n `18`; unknown avg `-0.6734` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
