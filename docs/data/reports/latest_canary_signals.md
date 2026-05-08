# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T15:22:24.848280+00:00`
- Correlation status: `ready`
- Asset price records: `657`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.147` n `12`; crypto_alt avg `-0.136` n `228`; crypto_major avg `-0.2162` n `8`; equity avg `-0.05` n `65`; fx avg `0.0085` n `5`; index avg `-0.0636` n `23`; metal avg `-0.3695` n `18`; unknown avg `-0.1509` n `375`
- 1h: commodity avg `0.228` n `12`; crypto_alt avg `-0.0933` n `228`; crypto_major avg `-0.3492` n `8`; equity avg `0.0234` n `65`; fx avg `-0.0142` n `5`; index avg `-0.0754` n `23`; metal avg `-0.302` n `18`; unknown avg `-0.1238` n `375`
- 4h: commodity avg `0.4971` n `12`; crypto_alt avg `0.3573` n `228`; crypto_major avg `-0.1199` n `8`; equity avg `1.1742` n `65`; fx avg `-0.0253` n `5`; index avg `0.4447` n `23`; metal avg `-0.4098` n `18`; unknown avg `0.173` n `375`
- 24h: commodity avg `1.7937` n `12`; crypto_alt avg `2.6071` n `228`; crypto_major avg `-0.0371` n `8`; equity avg `1.2304` n `65`; fx avg `0.2008` n `5`; index avg `0.2943` n `23`; metal avg `-1.0214` n `18`; unknown avg `0.1977` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1232`, n `649`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `649`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `653`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `649`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0963`, n `649`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `653`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `653`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `653`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `653`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `653`, weak_sample_signal
