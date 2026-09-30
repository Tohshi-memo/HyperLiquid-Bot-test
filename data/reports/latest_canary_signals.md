# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T02:37:36.586711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.0042` n `234`; crypto_major avg `-0.0324` n `8`; equity avg `-0.1358` n `142`; fx avg `0.0131` n `6`; index avg `-0.0358` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.0481` n `963`
- 1h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.3163` n `234`; crypto_major avg `0.0304` n `8`; equity avg `-0.3091` n `142`; fx avg `-0.0789` n `6`; index avg `-0.0489` n `26`; metal avg `0.0105` n `20`; unknown avg `3.1346` n `961`
- 4h: commodity avg `-0.02` n `12`; crypto_alt avg `0.0646` n `234`; crypto_major avg `-0.0712` n `8`; equity avg `-0.3822` n `142`; fx avg `-0.0796` n `6`; index avg `-0.0874` n `26`; metal avg `-0.0942` n `20`; unknown avg `4.3537` n `954`
- 24h: commodity avg `-0.9034` n `12`; crypto_alt avg `2.8059` n `234`; crypto_major avg `0.9951` n `8`; equity avg `0.763` n `142`; fx avg `-0.1879` n `6`; index avg `0.0743` n `26`; metal avg `0.1868` n `20`; unknown avg `3250.3143` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
