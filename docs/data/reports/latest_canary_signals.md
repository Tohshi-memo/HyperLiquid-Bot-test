# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T00:52:27.502723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.1642` n `234`; crypto_major avg `0.0697` n `8`; equity avg `-0.0806` n `140`; fx avg `-0.0017` n `6`; index avg `-0.0259` n `26`; metal avg `0.0111` n `20`; unknown avg `0.032` n `919`
- 1h: commodity avg `-0.0575` n `12`; crypto_alt avg `0.2511` n `234`; crypto_major avg `0.0452` n `8`; equity avg `-0.1942` n `140`; fx avg `0.0448` n `6`; index avg `-0.0674` n `26`; metal avg `0.0949` n `20`; unknown avg `-0.1279` n `911`
- 4h: commodity avg `-0.0489` n `12`; crypto_alt avg `0.7633` n `234`; crypto_major avg `0.3693` n `8`; equity avg `-0.1991` n `140`; fx avg `0.063` n `6`; index avg `-0.0929` n `26`; metal avg `0.1604` n `20`; unknown avg `-0.0536` n `815`
- 24h: commodity avg `-0.0532` n `12`; crypto_alt avg `3.5877` n `234`; crypto_major avg `2.0018` n `8`; equity avg `1.4647` n `138`; fx avg `0.0716` n `6`; index avg `0.201` n `26`; metal avg `0.617` n `20`; unknown avg `1.3248` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
