# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T09:37:26.726715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `13`; crypto_alt avg `0.0808` n `238`; crypto_major avg `0.0509` n `8`; equity avg `0.0044` n `156`; fx avg `0.0049` n `6`; index avg `0.0044` n `27`; metal avg `0.0057` n `20`; unknown avg `0.1566` n `1262`
- 1h: commodity avg `-0.014` n `13`; crypto_alt avg `0.2657` n `238`; crypto_major avg `0.3574` n `8`; equity avg `0.0678` n `156`; fx avg `-0.007` n `6`; index avg `-0.005` n `27`; metal avg `0.0333` n `20`; unknown avg `0.1262` n `1256`
- 4h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.0667` n `238`; crypto_major avg `-0.1518` n `8`; equity avg `-0.0194` n `156`; fx avg `0.012` n `6`; index avg `-0.0078` n `27`; metal avg `0.011` n `20`; unknown avg `0.7245` n `1212`
- 24h: commodity avg `-0.1959` n `13`; crypto_alt avg `0.9009` n `238`; crypto_major avg `-0.772` n `8`; equity avg `-1.9837` n `156`; fx avg `-0.0925` n `6`; index avg `-0.185` n `27`; metal avg `-0.4996` n `20`; unknown avg `4.5736` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
