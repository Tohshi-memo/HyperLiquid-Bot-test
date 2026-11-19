# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T01:52:38.056706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0889` n `13`; crypto_alt avg `0.3149` n `239`; crypto_major avg `0.3042` n `8`; equity avg `0.3077` n `164`; fx avg `0.0171` n `6`; index avg `0.031` n `27`; metal avg `0.1055` n `20`; unknown avg `2.4082` n `1265`
- 1h: commodity avg `0.2263` n `13`; crypto_alt avg `-0.4389` n `239`; crypto_major avg `-0.5308` n `8`; equity avg `-0.7331` n `164`; fx avg `0.0033` n `6`; index avg `-0.1234` n `27`; metal avg `-0.0733` n `20`; unknown avg `3.7711` n `1263`
- 4h: commodity avg `0.1731` n `13`; crypto_alt avg `0.3676` n `239`; crypto_major avg `0.3235` n `8`; equity avg `0.8266` n `164`; fx avg `-0.0113` n `6`; index avg `0.0742` n `27`; metal avg `0.2333` n `20`; unknown avg `3.455` n `1251`
- 24h: commodity avg `0.1088` n `13`; crypto_alt avg `-0.576` n `239`; crypto_major avg `-1.6988` n `8`; equity avg `-0.666` n `164`; fx avg `-0.0991` n `6`; index avg `0.0368` n `27`; metal avg `-0.6738` n `20`; unknown avg `60.2682` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
