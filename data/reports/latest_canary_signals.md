# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T04:37:22.864066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0443` n `12`; crypto_alt avg `0.1511` n `228`; crypto_major avg `0.0413` n `8`; equity avg `0.085` n `69`; fx avg `0.0017` n `6`; index avg `0.0098` n `23`; metal avg `0.0771` n `18`; unknown avg `42.0317` n `422`
- 1h: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.0218` n `228`; crypto_major avg `-0.2353` n `8`; equity avg `0.3269` n `69`; fx avg `0.0269` n `6`; index avg `0.1171` n `23`; metal avg `0.2639` n `18`; unknown avg `7.1208` n `422`
- 4h: commodity avg `-0.2209` n `12`; crypto_alt avg `0.0484` n `228`; crypto_major avg `-0.3556` n `8`; equity avg `0.39` n `69`; fx avg `0.0744` n `6`; index avg `-0.2046` n `23`; metal avg `0.4252` n `18`; unknown avg `0.8665` n `422`
- 24h: commodity avg `-0.6189` n `12`; crypto_alt avg `-0.3877` n `228`; crypto_major avg `-0.8147` n `8`; equity avg `-0.373` n `69`; fx avg `0.0617` n `6`; index avg `-0.8124` n `23`; metal avg `0.2539` n `18`; unknown avg `2.3114` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
