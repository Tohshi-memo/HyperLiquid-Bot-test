# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T04:07:30.526849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `0.0796` n `230`; crypto_major avg `0.0486` n `8`; equity avg `0.0592` n `108`; fx avg `-0.02` n `6`; index avg `-0.0025` n `25`; metal avg `0.0578` n `20`; unknown avg `0.0629` n `781`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.1743` n `230`; crypto_major avg `-0.3977` n `8`; equity avg `0.2118` n `108`; fx avg `0.0015` n `6`; index avg `0.0138` n `25`; metal avg `-0.0013` n `20`; unknown avg `1.0888` n `781`
- 4h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.5608` n `230`; crypto_major avg `0.2763` n `8`; equity avg `0.6151` n `108`; fx avg `-0.0802` n `6`; index avg `0.0326` n `25`; metal avg `0.4044` n `20`; unknown avg `-0.193` n `781`
- 24h: commodity avg `-1.5229` n `12`; crypto_alt avg `0.3005` n `230`; crypto_major avg `0.5325` n `8`; equity avg `4.1478` n `108`; fx avg `-0.0514` n `6`; index avg `0.8728` n `25`; metal avg `1.1135` n `20`; unknown avg `0.4113` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
