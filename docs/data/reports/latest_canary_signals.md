# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T18:07:35.012495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `-0.0809` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `-0.2347` n `96`; fx avg `0.006` n `6`; index avg `-0.0292` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0168` n `769`
- 1h: commodity avg `0.1234` n `12`; crypto_alt avg `-0.1598` n `230`; crypto_major avg `-0.0897` n `8`; equity avg `-0.4924` n `96`; fx avg `-0.0205` n `6`; index avg `-0.1287` n `25`; metal avg `-0.0464` n `20`; unknown avg `0.1321` n `769`
- 4h: commodity avg `0.2586` n `12`; crypto_alt avg `0.3042` n `230`; crypto_major avg `0.4374` n `8`; equity avg `0.9365` n `96`; fx avg `0.0783` n `6`; index avg `0.1101` n `25`; metal avg `0.1575` n `20`; unknown avg `0.1977` n `769`
- 24h: commodity avg `0.9007` n `12`; crypto_alt avg `-1.046` n `230`; crypto_major avg `-1.1769` n `8`; equity avg `-0.6916` n `94`; fx avg `0.0925` n `6`; index avg `-0.1941` n `25`; metal avg `-0.0768` n `20`; unknown avg `-0.0478` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
