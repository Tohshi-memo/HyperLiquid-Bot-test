# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T01:07:33.562262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `13`; crypto_alt avg `0.114` n `239`; crypto_major avg `0.1421` n `8`; equity avg `0.2678` n `162`; fx avg `0.0171` n `6`; index avg `0.0466` n `27`; metal avg `0.0364` n `20`; unknown avg `0.0318` n `1260`
- 1h: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.2207` n `239`; crypto_major avg `-0.0368` n `8`; equity avg `0.2187` n `162`; fx avg `0.0238` n `6`; index avg `0.0695` n `27`; metal avg `-0.0013` n `20`; unknown avg `-0.1092` n `1264`
- 4h: commodity avg `-0.0722` n `13`; crypto_alt avg `-0.2417` n `239`; crypto_major avg `-0.1042` n `8`; equity avg `0.0689` n `162`; fx avg `0.0462` n `6`; index avg `0.0367` n `27`; metal avg `0.0801` n `20`; unknown avg `7.675` n `1220`
- 24h: commodity avg `-0.981` n `13`; crypto_alt avg `-0.2959` n `239`; crypto_major avg `0.1075` n `8`; equity avg `-3.7517` n `162`; fx avg `-0.0547` n `6`; index avg `-0.3602` n `27`; metal avg `-0.5604` n `20`; unknown avg `498.0745` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
