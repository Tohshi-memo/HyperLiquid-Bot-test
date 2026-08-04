# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T13:52:33.790384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.1949` n `230`; crypto_major avg `-0.3209` n `8`; equity avg `0.0228` n `107`; fx avg `0.0069` n `6`; index avg `0.0962` n `25`; metal avg `0.0608` n `20`; unknown avg `-0.172` n `782`
- 1h: commodity avg `-0.3803` n `12`; crypto_alt avg `-0.1587` n `230`; crypto_major avg `-0.3346` n `8`; equity avg `0.6323` n `107`; fx avg `-0.0187` n `6`; index avg `0.2107` n `25`; metal avg `0.0458` n `20`; unknown avg `-0.1161` n `781`
- 4h: commodity avg `-1.4817` n `12`; crypto_alt avg `-0.0737` n `230`; crypto_major avg `0.3667` n `8`; equity avg `1.4877` n `107`; fx avg `-0.1137` n `6`; index avg `0.3663` n `25`; metal avg `0.622` n `20`; unknown avg `-0.1286` n `781`
- 24h: commodity avg `-0.8244` n `12`; crypto_alt avg `0.1013` n `230`; crypto_major avg `0.8208` n `8`; equity avg `5.512` n `107`; fx avg `0.0729` n `6`; index avg `0.9116` n `25`; metal avg `1.208` n `20`; unknown avg `0.6013` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
