# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T02:37:31.354683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7685` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.0616` n `230`; crypto_major avg `-0.0162` n `8`; equity avg `0.0691` n `93`; fx avg `-0.004` n `6`; index avg `0.0081` n `25`; metal avg `0.0789` n `20`; unknown avg `-0.1196` n `767`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `-0.3127` n `230`; crypto_major avg `-0.2725` n `8`; equity avg `0.5913` n `93`; fx avg `0.0054` n `6`; index avg `0.0791` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.2558` n `767`
- 4h: commodity avg `0.097` n `12`; crypto_alt avg `-0.3355` n `230`; crypto_major avg `-0.7323` n `8`; equity avg `1.0362` n `93`; fx avg `0.0333` n `6`; index avg `0.1731` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.4044` n `765`
- 24h: commodity avg `0.2887` n `12`; crypto_alt avg `1.9089` n `230`; crypto_major avg `2.9191` n `8`; equity avg `2.8349` n `92`; fx avg `0.0528` n `6`; index avg `0.784` n `25`; metal avg `0.5234` n `20`; unknown avg `0.2227` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
