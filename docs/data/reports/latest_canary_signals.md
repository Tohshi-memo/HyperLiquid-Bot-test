# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T21:52:30.125250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0285` n `13`; crypto_alt avg `0.0653` n `235`; crypto_major avg `0.0759` n `8`; equity avg `0.0143` n `151`; fx avg `0.0002` n `6`; index avg `-0.0121` n `26`; metal avg `0.0067` n `20`; unknown avg `70.8771` n `1135`
- 1h: commodity avg `-0.0695` n `13`; crypto_alt avg `0.1489` n `235`; crypto_major avg `0.0929` n `8`; equity avg `0.0626` n `151`; fx avg `-0.011` n `6`; index avg `-0.0013` n `26`; metal avg `0.0382` n `20`; unknown avg `70.5971` n `1127`
- 4h: commodity avg `0.1131` n `13`; crypto_alt avg `0.9487` n `235`; crypto_major avg `0.5283` n `8`; equity avg `0.6646` n `151`; fx avg `-0.0133` n `6`; index avg `0.0818` n `26`; metal avg `0.1318` n `20`; unknown avg `7.533` n `1075`
- 24h: commodity avg `0.7972` n `13`; crypto_alt avg `0.0607` n `235`; crypto_major avg `0.3326` n `8`; equity avg `-0.4832` n `151`; fx avg `0.1557` n `6`; index avg `-0.1369` n `26`; metal avg `-0.2486` n `20`; unknown avg `4.2971` n `1003`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1576`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.143`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0914`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
