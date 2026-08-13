# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T21:37:24.380866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `0.0222` n `230`; crypto_major avg `-0.0033` n `8`; equity avg `0.0578` n `113`; fx avg `0.0047` n `6`; index avg `0.0007` n `25`; metal avg `-0.0155` n `20`; unknown avg `0.0066` n `787`
- 1h: commodity avg `0.0358` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `0.1329` n `113`; fx avg `0.0013` n `6`; index avg `0.0099` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.1119` n `787`
- 4h: commodity avg `-0.101` n `12`; crypto_alt avg `0.3416` n `230`; crypto_major avg `0.2772` n `8`; equity avg `-0.0121` n `113`; fx avg `0.0092` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0948` n `20`; unknown avg `0.0683` n `787`
- 24h: commodity avg `-0.4652` n `12`; crypto_alt avg `0.4664` n `230`; crypto_major avg `0.6294` n `8`; equity avg `1.644` n `113`; fx avg `0.0281` n `6`; index avg `0.3201` n `25`; metal avg `-0.4768` n `20`; unknown avg `0.0855` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
