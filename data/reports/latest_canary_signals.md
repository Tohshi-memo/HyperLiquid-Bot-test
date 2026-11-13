# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T21:22:28.920158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0677` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0207` n `13`; crypto_alt avg `-0.2005` n `239`; crypto_major avg `-0.5125` n `8`; equity avg `-0.1846` n `162`; fx avg `-0.0108` n `6`; index avg `-0.0239` n `27`; metal avg `0.0382` n `20`; unknown avg `1.5187` n `1262`
- 1h: commodity avg `0.0862` n `13`; crypto_alt avg `-0.936` n `239`; crypto_major avg `-1.1313` n `8`; equity avg `-0.6112` n `162`; fx avg `-0.0052` n `6`; index avg `-0.0636` n `27`; metal avg `0.004` n `20`; unknown avg `8.9764` n `1224`
- 4h: commodity avg `0.1088` n `13`; crypto_alt avg `-0.0363` n `239`; crypto_major avg `-0.1729` n `8`; equity avg `0.2494` n `162`; fx avg `-0.0365` n `6`; index avg `0.0414` n `27`; metal avg `-0.0721` n `20`; unknown avg `2.6735` n `1214`
- 24h: commodity avg `-0.328` n `13`; crypto_alt avg `-0.9907` n `239`; crypto_major avg `-2.4493` n `8`; equity avg `-2.8155` n `162`; fx avg `-0.0777` n `6`; index avg `-0.2315` n `27`; metal avg `-0.2367` n `20`; unknown avg `1.5395` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
