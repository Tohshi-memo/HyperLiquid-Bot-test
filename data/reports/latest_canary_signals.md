# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T02:37:30.479187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `13`; crypto_alt avg `-0.1744` n `235`; crypto_major avg `-0.1494` n `8`; equity avg `-0.0174` n `151`; fx avg `-0.0081` n `6`; index avg `-0.0067` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.083` n `1135`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.2099` n `235`; crypto_major avg `0.1168` n `8`; equity avg `0.2815` n `151`; fx avg `-0.03` n `6`; index avg `0.0496` n `26`; metal avg `0.1547` n `20`; unknown avg `-0.1562` n `1133`
- 4h: commodity avg `0.0981` n `13`; crypto_alt avg `0.2165` n `235`; crypto_major avg `0.0946` n `8`; equity avg `0.0757` n `151`; fx avg `-0.0071` n `6`; index avg `0.0359` n `26`; metal avg `0.0284` n `20`; unknown avg `-0.1299` n `1127`
- 24h: commodity avg `1.062` n `13`; crypto_alt avg `1.1683` n `235`; crypto_major avg `0.5793` n `8`; equity avg `1.0364` n `151`; fx avg `0.108` n `6`; index avg `0.21` n `26`; metal avg `-0.2014` n `20`; unknown avg `0.5977` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1525`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1373`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.091`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
