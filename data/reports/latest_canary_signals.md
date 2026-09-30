# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T11:07:37.933899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.4465` n `234`; crypto_major avg `-0.2191` n `8`; equity avg `-0.1894` n `142`; fx avg `-0.001` n `6`; index avg `-0.0392` n `26`; metal avg `-0.0444` n `20`; unknown avg `0.3874` n `961`
- 1h: commodity avg `0.1208` n `12`; crypto_alt avg `-0.2813` n `234`; crypto_major avg `0.0524` n `8`; equity avg `-0.2013` n `142`; fx avg `0.0127` n `6`; index avg `-0.0443` n `26`; metal avg `-0.0412` n `20`; unknown avg `0.8227` n `961`
- 4h: commodity avg `0.3294` n `12`; crypto_alt avg `1.153` n `234`; crypto_major avg `1.1571` n `8`; equity avg `-0.2115` n `142`; fx avg `0.0664` n `6`; index avg `-0.0766` n `26`; metal avg `-0.1539` n `20`; unknown avg `0.6026` n `945`
- 24h: commodity avg `-0.183` n `12`; crypto_alt avg `-0.2135` n `234`; crypto_major avg `-0.4509` n `8`; equity avg `-0.2578` n `142`; fx avg `0.0509` n `6`; index avg `-0.0604` n `26`; metal avg `0.0637` n `20`; unknown avg `2927.2021` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
