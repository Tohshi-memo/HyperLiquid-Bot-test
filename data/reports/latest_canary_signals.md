# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T04:52:28.438082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `0.3005` n `237`; crypto_major avg `0.3082` n `8`; equity avg `0.0518` n `151`; fx avg `-0.0113` n `6`; index avg `0.0034` n `26`; metal avg `0.0177` n `20`; unknown avg `6.7444` n `1192`
- 1h: commodity avg `0.0219` n `13`; crypto_alt avg `0.1647` n `237`; crypto_major avg `0.3588` n `8`; equity avg `-0.0143` n `151`; fx avg `-0.0167` n `6`; index avg `-0.0054` n `26`; metal avg `0.0202` n `20`; unknown avg `10.4297` n `1184`
- 4h: commodity avg `-0.0457` n `13`; crypto_alt avg `0.1893` n `237`; crypto_major avg `0.5651` n `8`; equity avg `0.9478` n `151`; fx avg `-0.025` n `6`; index avg `0.1827` n `26`; metal avg `0.1551` n `20`; unknown avg `5.9637` n `1184`
- 24h: commodity avg `-0.4634` n `13`; crypto_alt avg `-0.0648` n `237`; crypto_major avg `1.043` n `8`; equity avg `2.728` n `151`; fx avg `-0.007` n `6`; index avg `0.4995` n `26`; metal avg `0.3397` n `20`; unknown avg `3.1985` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.198`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
