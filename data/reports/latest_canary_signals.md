# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T19:22:31.480593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.2757` n `236`; crypto_major avg `0.3789` n `8`; equity avg `0.3287` n `151`; fx avg `0.0187` n `6`; index avg `0.0671` n `26`; metal avg `0.0776` n `20`; unknown avg `13.6489` n `1136`
- 1h: commodity avg `-0.0609` n `13`; crypto_alt avg `0.1615` n `236`; crypto_major avg `0.3733` n `8`; equity avg `-0.0061` n `151`; fx avg `0.0122` n `6`; index avg `-0.0046` n `26`; metal avg `0.0349` n `20`; unknown avg `10.4864` n `1132`
- 4h: commodity avg `0.0736` n `13`; crypto_alt avg `0.2231` n `236`; crypto_major avg `-0.2813` n `8`; equity avg `-1.1526` n `151`; fx avg `0.0215` n `6`; index avg `-0.1766` n `26`; metal avg `-0.0786` n `20`; unknown avg `0.1935` n `1124`
- 24h: commodity avg `-0.1284` n `13`; crypto_alt avg `-2.5711` n `236`; crypto_major avg `-2.0719` n `8`; equity avg `-3.7738` n `151`; fx avg `-0.1535` n `6`; index avg `-0.5258` n `26`; metal avg `-0.8062` n `20`; unknown avg `1269.4397` n `976`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0816`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0625`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0577`, n `666`, weak_sample_signal
