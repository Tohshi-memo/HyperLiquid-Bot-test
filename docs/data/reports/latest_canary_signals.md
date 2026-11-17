# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T07:37:32.158105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.102` n `13`; crypto_alt avg `0.0364` n `239`; crypto_major avg `-0.0443` n `8`; equity avg `-0.0236` n `162`; fx avg `-0.0093` n `6`; index avg `0.0031` n `27`; metal avg `-0.0113` n `20`; unknown avg `0.1422` n `1264`
- 1h: commodity avg `0.0673` n `13`; crypto_alt avg `0.5803` n `239`; crypto_major avg `0.4933` n `8`; equity avg `0.377` n `162`; fx avg `-0.0086` n `6`; index avg `0.0184` n `27`; metal avg `-0.0014` n `20`; unknown avg `15.7118` n `1216`
- 4h: commodity avg `0.1034` n `13`; crypto_alt avg `-0.3276` n `239`; crypto_major avg `-0.3936` n `8`; equity avg `-1.1775` n `162`; fx avg `-0.0259` n `6`; index avg `-0.1135` n `27`; metal avg `-0.0326` n `20`; unknown avg `0.1195` n `1188`
- 24h: commodity avg `-1.0411` n `13`; crypto_alt avg `0.6906` n `239`; crypto_major avg `0.7444` n `8`; equity avg `-2.5857` n `162`; fx avg `-0.0286` n `6`; index avg `-0.2633` n `27`; metal avg `-0.0583` n `20`; unknown avg `229.5887` n `1101`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
