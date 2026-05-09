# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T04:07:14.122983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `0.3073` n `228`; crypto_major avg `0.3872` n `8`; equity avg `0.0125` n `65`; fx avg `0.0` n `5`; index avg `0.0469` n `23`; metal avg `-0.0088` n `18`; unknown avg `0.824` n `375`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.029` n `228`; crypto_major avg `0.3663` n `8`; equity avg `-0.0259` n `65`; fx avg `0.0002` n `5`; index avg `0.0652` n `23`; metal avg `-0.0778` n `18`; unknown avg `0.232` n `375`
- 4h: commodity avg `0.1899` n `12`; crypto_alt avg `1.2232` n `228`; crypto_major avg `1.1898` n `8`; equity avg `0.1504` n `65`; fx avg `-0.014` n `5`; index avg `0.0481` n `23`; metal avg `0.2549` n `18`; unknown avg `0.5917` n `375`
- 24h: commodity avg `-0.231` n `12`; crypto_alt avg `4.5179` n `228`; crypto_major avg `3.0898` n `8`; equity avg `3.7466` n `65`; fx avg `0.0685` n `5`; index avg `1.4386` n `23`; metal avg `0.1934` n `18`; unknown avg `1.7369` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
