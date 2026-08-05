# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T20:00:23.557481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0232` n `230`; crypto_major avg `-0.0926` n `8`; equity avg `-0.3175` n `108`; fx avg `0.0069` n `6`; index avg `-0.076` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.0235` n `782`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.1032` n `230`; crypto_major avg `-0.0858` n `8`; equity avg `-0.6364` n `108`; fx avg `0.016` n `6`; index avg `-0.1235` n `25`; metal avg `-0.0928` n `20`; unknown avg `-0.0807` n `782`
- 4h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.1942` n `230`; crypto_major avg `0.4582` n `8`; equity avg `-0.4783` n `108`; fx avg `0.0033` n `6`; index avg `-0.0738` n `25`; metal avg `0.1317` n `20`; unknown avg `-0.1531` n `782`
- 24h: commodity avg `-0.0811` n `12`; crypto_alt avg `0.5859` n `230`; crypto_major avg `0.8212` n `8`; equity avg `-0.9083` n `108`; fx avg `-0.0375` n `6`; index avg `-0.2076` n `25`; metal avg `0.7884` n `20`; unknown avg `0.7758` n `749`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
