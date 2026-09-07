# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T19:52:24.718870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0835` n `232`; crypto_major avg `0.0554` n `8`; equity avg `0.0221` n `134`; fx avg `0.0042` n `6`; index avg `-0.0018` n `26`; metal avg `0.0076` n `20`; unknown avg `0.6424` n `796`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `0.4379` n `232`; crypto_major avg `0.2827` n `8`; equity avg `0.0829` n `134`; fx avg `0.0038` n `6`; index avg `0.0087` n `26`; metal avg `0.0182` n `20`; unknown avg `-0.387` n `794`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `1.1091` n `232`; crypto_major avg `0.8548` n `8`; equity avg `0.3245` n `134`; fx avg `-0.0142` n `6`; index avg `0.0514` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.1448` n `768`
- 24h: commodity avg `0.1836` n `12`; crypto_alt avg `0.6562` n `232`; crypto_major avg `-0.5052` n `8`; equity avg `0.459` n `134`; fx avg `-0.1297` n `6`; index avg `0.0858` n `26`; metal avg `0.0081` n `20`; unknown avg `0.9055` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
