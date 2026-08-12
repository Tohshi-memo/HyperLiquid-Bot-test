# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T10:17:14.456064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-0.009` n `230`; crypto_major avg `0.0056` n `8`; equity avg `0.0348` n `113`; fx avg `-0.0014` n `6`; index avg `0.0041` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0131` n `786`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.2159` n `230`; crypto_major avg `0.379` n `8`; equity avg `0.1079` n `113`; fx avg `-0.0142` n `6`; index avg `0.0057` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0409` n `786`
- 4h: commodity avg `-0.1425` n `12`; crypto_alt avg `-0.1434` n `230`; crypto_major avg `0.601` n `8`; equity avg `0.7628` n `113`; fx avg `-0.0222` n `6`; index avg `0.1208` n `25`; metal avg `0.2825` n `20`; unknown avg `-0.055` n `786`
- 24h: commodity avg `-0.1578` n `12`; crypto_alt avg `-0.8487` n `230`; crypto_major avg `1.0257` n `8`; equity avg `2.6427` n `113`; fx avg `-0.0024` n `6`; index avg `0.2566` n `25`; metal avg `0.2301` n `20`; unknown avg `-0.1755` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2395`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
