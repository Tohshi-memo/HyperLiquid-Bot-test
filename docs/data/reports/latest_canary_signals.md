# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T15:07:33.230887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2267` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0198` n `13`; crypto_alt avg `0.2163` n `238`; crypto_major avg `0.1184` n `8`; equity avg `0.2647` n `155`; fx avg `0.0171` n `6`; index avg `0.0349` n `27`; metal avg `0.0403` n `20`; unknown avg `-0.0585` n `1232`
- 1h: commodity avg `0.1063` n `13`; crypto_alt avg `0.0697` n `238`; crypto_major avg `-0.0942` n `8`; equity avg `0.152` n `155`; fx avg `0.0357` n `6`; index avg `0.007` n `27`; metal avg `-0.0262` n `20`; unknown avg `0.0659` n `1190`
- 4h: commodity avg `0.1477` n `13`; crypto_alt avg `-1.0048` n `238`; crypto_major avg `-1.186` n `8`; equity avg `-0.618` n `155`; fx avg `0.1234` n `6`; index avg `0.0407` n `27`; metal avg `0.0059` n `20`; unknown avg `0.9753` n `1152`
- 24h: commodity avg `0.5624` n `13`; crypto_alt avg `0.5755` n `238`; crypto_major avg `0.544` n `8`; equity avg `1.5637` n `154`; fx avg `0.2171` n `6`; index avg `0.3061` n `27`; metal avg `-0.1414` n `20`; unknown avg `7.434` n `1068`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
