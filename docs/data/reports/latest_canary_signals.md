# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T01:37:29.303919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `13`; crypto_alt avg `-0.1208` n `238`; crypto_major avg `-0.0176` n `8`; equity avg `-0.1107` n `156`; fx avg `-0.0028` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0183` n `20`; unknown avg `-0.0363` n `1261`
- 1h: commodity avg `-0.1701` n `13`; crypto_alt avg `0.5922` n `238`; crypto_major avg `0.7729` n `8`; equity avg `0.4199` n `156`; fx avg `0.0222` n `6`; index avg `0.0646` n `27`; metal avg `0.003` n `20`; unknown avg `0.172` n `1253`
- 4h: commodity avg `-0.1304` n `13`; crypto_alt avg `0.1785` n `238`; crypto_major avg `0.6675` n `8`; equity avg `0.708` n `156`; fx avg `0.1454` n `6`; index avg `0.1811` n `27`; metal avg `0.0907` n `20`; unknown avg `-0.5745` n `1223`
- 24h: commodity avg `-0.1455` n `13`; crypto_alt avg `-0.4228` n `238`; crypto_major avg `0.4621` n `8`; equity avg `1.0392` n `156`; fx avg `0.1034` n `6`; index avg `0.2852` n `27`; metal avg `0.1134` n `20`; unknown avg `1.8336` n `1126`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
