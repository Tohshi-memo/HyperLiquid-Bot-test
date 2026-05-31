# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T07:22:19.838992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.138` n `228`; crypto_major avg `-0.1864` n `8`; equity avg `0.0182` n `69`; fx avg `0.0012` n `6`; index avg `-0.0821` n `23`; metal avg `-0.0114` n `18`; unknown avg `-0.1335` n `421`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.3161` n `228`; crypto_major avg `-0.4067` n `8`; equity avg `0.0533` n `69`; fx avg `0.0202` n `6`; index avg `-0.0683` n `23`; metal avg `0.0122` n `18`; unknown avg `0.1389` n `421`
- 4h: commodity avg `0.1711` n `12`; crypto_alt avg `-0.2955` n `228`; crypto_major avg `-0.3663` n `8`; equity avg `0.2305` n `69`; fx avg `0.0202` n `6`; index avg `-0.1224` n `23`; metal avg `0.0164` n `18`; unknown avg `-0.0328` n `401`
- 24h: commodity avg `0.1905` n `12`; crypto_alt avg `0.3043` n `228`; crypto_major avg `1.6568` n `8`; equity avg `1.0434` n `69`; fx avg `0.0602` n `6`; index avg `-0.1352` n `23`; metal avg `-0.0382` n `18`; unknown avg `0.6738` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
