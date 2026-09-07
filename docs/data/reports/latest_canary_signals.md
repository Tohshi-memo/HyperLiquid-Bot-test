# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T21:37:27.416148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.1519` n `232`; crypto_major avg `-0.0913` n `8`; equity avg `0.0144` n `134`; fx avg `0.001` n `6`; index avg `0.0022` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.0674` n `796`
- 1h: commodity avg `-0.0347` n `12`; crypto_alt avg `0.0389` n `232`; crypto_major avg `-0.0849` n `8`; equity avg `0.0823` n `134`; fx avg `-0.002` n `6`; index avg `0.0054` n `26`; metal avg `0.0016` n `20`; unknown avg `-0.1003` n `786`
- 4h: commodity avg `-0.0332` n `12`; crypto_alt avg `0.3945` n `232`; crypto_major avg `0.1004` n `8`; equity avg `0.1381` n `134`; fx avg `-0.006` n `6`; index avg `0.0224` n `26`; metal avg `0.0241` n `20`; unknown avg `0.1782` n `734`
- 24h: commodity avg `0.1548` n `12`; crypto_alt avg `-0.0566` n `232`; crypto_major avg `-1.365` n `8`; equity avg `0.5091` n `134`; fx avg `-0.1435` n `6`; index avg `0.0882` n `26`; metal avg `0.0332` n `20`; unknown avg `7800.4721` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
