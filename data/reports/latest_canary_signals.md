# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T11:37:26.178181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `0.4285` n `239`; crypto_major avg `0.4928` n `8`; equity avg `0.6442` n `162`; fx avg `-0.0012` n `6`; index avg `0.0699` n `27`; metal avg `0.0569` n `20`; unknown avg `0.3708` n `1266`
- 1h: commodity avg `0.1062` n `13`; crypto_alt avg `0.9968` n `239`; crypto_major avg `0.9131` n `8`; equity avg `1.3294` n `162`; fx avg `0.0043` n `6`; index avg `0.1091` n `27`; metal avg `0.1098` n `20`; unknown avg `158.6719` n `1264`
- 4h: commodity avg `0.1981` n `13`; crypto_alt avg `0.1995` n `239`; crypto_major avg `0.0956` n `8`; equity avg `0.5032` n `162`; fx avg `-0.046` n `6`; index avg `0.0773` n `27`; metal avg `-0.0293` n `20`; unknown avg `201.9461` n `1238`
- 24h: commodity avg `-0.6954` n `13`; crypto_alt avg `1.1413` n `239`; crypto_major avg `1.0371` n `8`; equity avg `-1.8056` n `162`; fx avg `-0.0578` n `6`; index avg `-0.178` n `27`; metal avg `-0.1743` n `20`; unknown avg `57.7861` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
