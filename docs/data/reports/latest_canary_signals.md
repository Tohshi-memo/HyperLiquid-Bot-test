# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T18:52:45.007056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `12`; crypto_alt avg `-0.0514` n `230`; crypto_major avg `-0.1081` n `8`; equity avg `0.011` n `108`; fx avg `-0.0045` n `6`; index avg `0.0041` n `25`; metal avg `0.0219` n `20`; unknown avg `0.0055` n `782`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `-0.1592` n `230`; crypto_major avg `-0.1597` n `8`; equity avg `-0.1817` n `108`; fx avg `0.002` n `6`; index avg `-0.02` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0701` n `782`
- 4h: commodity avg `0.025` n `12`; crypto_alt avg `0.277` n `230`; crypto_major avg `0.58` n `8`; equity avg `0.1046` n `108`; fx avg `-0.0215` n `6`; index avg `-0.034` n `25`; metal avg `0.1401` n `20`; unknown avg `-0.0331` n `782`
- 24h: commodity avg `-0.1013` n `12`; crypto_alt avg `0.5869` n `230`; crypto_major avg `0.7945` n `8`; equity avg `-0.3947` n `108`; fx avg `-0.0338` n `6`; index avg `-0.0715` n `25`; metal avg `0.8112` n `20`; unknown avg `0.7564` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
