# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T03:52:29.786317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.0056` n `238`; crypto_major avg `-0.1514` n `8`; equity avg `0.0084` n `156`; fx avg `0.0094` n `6`; index avg `0.0009` n `27`; metal avg `-0.0028` n `20`; unknown avg `0.2055` n `1258`
- 1h: commodity avg `0.0512` n `13`; crypto_alt avg `-0.1997` n `238`; crypto_major avg `-0.4095` n `8`; equity avg `0.0129` n `156`; fx avg `0.0168` n `6`; index avg `-0.0321` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.1215` n `1242`
- 4h: commodity avg `0.0361` n `13`; crypto_alt avg `-0.5738` n `238`; crypto_major avg `-0.3375` n `8`; equity avg `0.0625` n `156`; fx avg `0.0091` n `6`; index avg `-0.0329` n `27`; metal avg `-0.0072` n `20`; unknown avg `-0.4979` n `1230`
- 24h: commodity avg `0.0224` n `13`; crypto_alt avg `2.3667` n `238`; crypto_major avg `-1.0333` n `8`; equity avg `-2.4989` n `156`; fx avg `-0.0891` n `6`; index avg `-0.1515` n `27`; metal avg `-0.617` n `20`; unknown avg `2.9845` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
