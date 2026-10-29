# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T04:37:34.653634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4385` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0206` n `13`; crypto_alt avg `0.1222` n `238`; crypto_major avg `0.2002` n `8`; equity avg `0.0165` n `155`; fx avg `0.0076` n `6`; index avg `0.0065` n `27`; metal avg `-0.0186` n `20`; unknown avg `0.1766` n `1228`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `0.2845` n `238`; crypto_major avg `0.4133` n `8`; equity avg `0.2721` n `155`; fx avg `0.0188` n `6`; index avg `0.0645` n `27`; metal avg `-0.0222` n `20`; unknown avg `0.1229` n `1214`
- 4h: commodity avg `-0.039` n `13`; crypto_alt avg `-2.4842` n `238`; crypto_major avg `-1.5677` n `8`; equity avg `-1.0576` n `155`; fx avg `0.0125` n `6`; index avg `-0.1292` n `27`; metal avg `-0.1909` n `20`; unknown avg `3.3189` n `1198`
- 24h: commodity avg `-0.1053` n `13`; crypto_alt avg `-2.3634` n `238`; crypto_major avg `-1.5477` n `8`; equity avg `-1.0251` n `154`; fx avg `0.0044` n `6`; index avg `-0.0495` n `27`; metal avg `-0.2547` n `20`; unknown avg `28.7496` n `978`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
