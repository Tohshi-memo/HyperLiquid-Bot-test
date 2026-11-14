# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T08:52:23.890531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.0176` n `239`; crypto_major avg `-0.0979` n `8`; equity avg `-0.0614` n `162`; fx avg `-0.1586` n `6`; index avg `0.0016` n `27`; metal avg `0.0017` n `20`; unknown avg `-0.0202` n `1259`
- 1h: commodity avg `-0.0298` n `13`; crypto_alt avg `-0.1007` n `239`; crypto_major avg `-0.0946` n `8`; equity avg `0.0223` n `162`; fx avg `0.0178` n `6`; index avg `0.0081` n `27`; metal avg `0.006` n `20`; unknown avg `0.3522` n `1242`
- 4h: commodity avg `0.0233` n `13`; crypto_alt avg `-0.8546` n `239`; crypto_major avg `-0.2724` n `8`; equity avg `0.1155` n `162`; fx avg `0.0143` n `6`; index avg `0.0139` n `27`; metal avg `0.0305` n `20`; unknown avg `1.4866` n `1212`
- 24h: commodity avg `-0.2195` n `13`; crypto_alt avg `-2.9515` n `239`; crypto_major avg `-3.2137` n `8`; equity avg `-2.3373` n `162`; fx avg `-0.1464` n `6`; index avg `-0.1709` n `27`; metal avg `-0.3302` n `20`; unknown avg `57.4329` n `1058`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
