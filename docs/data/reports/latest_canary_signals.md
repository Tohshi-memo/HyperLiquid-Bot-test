# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T04:52:25.584170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `0.165` n `232`; crypto_major avg `0.0823` n `8`; equity avg `-0.0049` n `134`; fx avg `0.0098` n `6`; index avg `-0.0181` n `26`; metal avg `0.0063` n `20`; unknown avg `0.83` n `792`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.3391` n `232`; crypto_major avg `-0.2454` n `8`; equity avg `-0.0299` n `134`; fx avg `-0.0106` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.7603` n `768`
- 4h: commodity avg `-0.0336` n `12`; crypto_alt avg `0.1274` n `232`; crypto_major avg `0.5077` n `8`; equity avg `0.0749` n `134`; fx avg `0.0012` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0114` n `20`; unknown avg `1.4614` n `752`
- 24h: commodity avg `0.0833` n `12`; crypto_alt avg `2.992` n `232`; crypto_major avg `3.0798` n `8`; equity avg `0.4502` n `134`; fx avg `-0.0569` n `6`; index avg `0.0825` n `26`; metal avg `0.0274` n `20`; unknown avg `1.5517` n `680`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
