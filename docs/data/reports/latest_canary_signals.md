# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T10:07:25.951544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.0592` n `8`; equity avg `-0.0202` n `114`; fx avg `-0.0005` n `6`; index avg `-0.0082` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0072` n `791`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `-0.1375` n `8`; equity avg `-0.0378` n `114`; fx avg `-0.0017` n `6`; index avg `-0.0091` n `25`; metal avg `0.0107` n `20`; unknown avg `0.0744` n `791`
- 4h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.3665` n `230`; crypto_major avg `0.0607` n `8`; equity avg `0.0245` n `114`; fx avg `0.0019` n `6`; index avg `0.0053` n `25`; metal avg `0.01` n `20`; unknown avg `2.3375` n `791`
- 24h: commodity avg `0.0776` n `12`; crypto_alt avg `0.0809` n `230`; crypto_major avg `0.1258` n `8`; equity avg `0.3889` n `114`; fx avg `-0.0043` n `6`; index avg `0.0604` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.0251` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
