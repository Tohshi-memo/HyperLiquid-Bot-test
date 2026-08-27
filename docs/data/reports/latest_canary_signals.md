# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T03:26:02.542738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.2098` n `231`; crypto_major avg `0.0934` n `8`; equity avg `0.1172` n `126`; fx avg `-0.0042` n `6`; index avg `0.0083` n `25`; metal avg `0.0356` n `20`; unknown avg `0.0597` n `793`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.078` n `231`; crypto_major avg `-0.0287` n `8`; equity avg `0.273` n `126`; fx avg `0.0277` n `6`; index avg `0.014` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0445` n `793`
- 4h: commodity avg `0.0412` n `12`; crypto_alt avg `-0.1316` n `231`; crypto_major avg `-0.0143` n `8`; equity avg `-0.0892` n `126`; fx avg `-0.0466` n `6`; index avg `-0.0803` n `25`; metal avg `0.1236` n `20`; unknown avg `0.3856` n `793`
- 24h: commodity avg `0.5163` n `12`; crypto_alt avg `0.2229` n `231`; crypto_major avg `0.4732` n `8`; equity avg `1.4368` n `126`; fx avg `-0.1224` n `6`; index avg `0.1954` n `25`; metal avg `-0.1884` n `20`; unknown avg `0.4399` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
