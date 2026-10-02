# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T15:52:34.134497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7969` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5268` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1532` n `13`; crypto_alt avg `-0.0629` n `235`; crypto_major avg `0.0284` n `8`; equity avg `0.046` n `143`; fx avg `-0.0082` n `6`; index avg `0.019` n `26`; metal avg `-0.0908` n `20`; unknown avg `1.7117` n `984`
- 1h: commodity avg `0.2092` n `13`; crypto_alt avg `-0.4393` n `235`; crypto_major avg `-0.694` n `8`; equity avg `-0.578` n `143`; fx avg `-0.0252` n `6`; index avg `-0.0995` n `26`; metal avg `-0.3537` n `20`; unknown avg `9.8712` n `982`
- 4h: commodity avg `0.278` n `13`; crypto_alt avg `-0.2062` n `235`; crypto_major avg `-1.3975` n `8`; equity avg `0.3994` n `142`; fx avg `0.0626` n `6`; index avg `0.1293` n `26`; metal avg `-0.4451` n `20`; unknown avg `1.1977` n `934`
- 24h: commodity avg `-0.4972` n `13`; crypto_alt avg `2.2865` n `235`; crypto_major avg `1.15` n `8`; equity avg `1.9273` n `142`; fx avg `-0.1284` n `6`; index avg `0.5539` n `26`; metal avg `-0.2206` n `20`; unknown avg `102.3466` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
