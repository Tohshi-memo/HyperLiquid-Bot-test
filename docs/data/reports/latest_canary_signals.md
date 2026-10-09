# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T06:22:28.771258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `13`; crypto_alt avg `0.0291` n `235`; crypto_major avg `0.0176` n `8`; equity avg `-0.0249` n `150`; fx avg `0.0103` n `6`; index avg `-0.004` n `26`; metal avg `-0.0318` n `20`; unknown avg `0.1415` n `1078`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `0.1683` n `235`; crypto_major avg `0.0303` n `8`; equity avg `0.1873` n `150`; fx avg `0.0209` n `6`; index avg `0.0123` n `26`; metal avg `0.0216` n `20`; unknown avg `0.0819` n `1046`
- 4h: commodity avg `-0.0259` n `13`; crypto_alt avg `1.1634` n `235`; crypto_major avg `0.643` n `8`; equity avg `0.5536` n `150`; fx avg `0.025` n `6`; index avg `0.0636` n `26`; metal avg `0.1148` n `20`; unknown avg `-0.3284` n `1040`
- 24h: commodity avg `0.1089` n `13`; crypto_alt avg `-0.7445` n `235`; crypto_major avg `-1.7685` n `8`; equity avg `-0.9174` n `150`; fx avg `0.1602` n `6`; index avg `-0.0562` n `26`; metal avg `0.392` n `20`; unknown avg `6.225` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
