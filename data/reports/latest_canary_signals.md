# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T01:22:38.650551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0525` n `12`; crypto_alt avg `-0.1492` n `230`; crypto_major avg `-0.0667` n `8`; equity avg `-0.4391` n `102`; fx avg `-0.001` n `6`; index avg `-0.1224` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.1772` n `777`
- 1h: commodity avg `0.1826` n `12`; crypto_alt avg `-0.518` n `230`; crypto_major avg `-0.1781` n `8`; equity avg `-1.269` n `102`; fx avg `-0.0279` n `6`; index avg `-0.2376` n `25`; metal avg `-0.0897` n `20`; unknown avg `-0.0945` n `777`
- 4h: commodity avg `0.6092` n `12`; crypto_alt avg `-0.3644` n `230`; crypto_major avg `0.0073` n `8`; equity avg `-0.2891` n `102`; fx avg `-0.0115` n `6`; index avg `-0.0345` n `25`; metal avg `-0.0618` n `20`; unknown avg `0.002` n `776`
- 24h: commodity avg `-0.095` n `12`; crypto_alt avg `0.3082` n `230`; crypto_major avg `0.9113` n `8`; equity avg `-1.521` n `102`; fx avg `-0.1581` n `6`; index avg `-0.1286` n `25`; metal avg `-0.1671` n `20`; unknown avg `-0.0675` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
