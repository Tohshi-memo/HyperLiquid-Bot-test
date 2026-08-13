# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T21:52:25.815176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.0297` n `230`; crypto_major avg `-0.0783` n `8`; equity avg `-0.012` n `113`; fx avg `-0.0005` n `6`; index avg `-0.0108` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.1013` n `787`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.2668` n `230`; crypto_major avg `-0.0269` n `8`; equity avg `0.1064` n `113`; fx avg `0.0011` n `6`; index avg `-0.002` n `25`; metal avg `0.0404` n `20`; unknown avg `0.0644` n `787`
- 4h: commodity avg `-0.0839` n `12`; crypto_alt avg `0.3236` n `230`; crypto_major avg `0.1991` n `8`; equity avg `0.0261` n `113`; fx avg `0.0132` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0974` n `20`; unknown avg `0.1443` n `787`
- 24h: commodity avg `-0.4396` n `12`; crypto_alt avg `0.6549` n `230`; crypto_major avg `0.5428` n `8`; equity avg `1.6482` n `113`; fx avg `0.0231` n `6`; index avg `0.3057` n `25`; metal avg `-0.474` n `20`; unknown avg `0.235` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2408`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
