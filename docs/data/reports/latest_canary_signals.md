# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T23:22:30.315671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `0.0673` n `235`; crypto_major avg `0.0096` n `8`; equity avg `-0.1178` n `151`; fx avg `-0.003` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0314` n `20`; unknown avg `-0.1783` n `1135`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `-0.0915` n `235`; crypto_major avg `-0.1683` n `8`; equity avg `-0.1887` n `151`; fx avg `0.0093` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0508` n `20`; unknown avg `-0.0559` n `1133`
- 4h: commodity avg `0.0766` n `13`; crypto_alt avg `-0.2436` n `235`; crypto_major avg `-0.3194` n `8`; equity avg `0.1737` n `151`; fx avg `-0.005` n `6`; index avg `-0.0159` n `26`; metal avg `-0.0601` n `20`; unknown avg `-0.1459` n `1019`
- 24h: commodity avg `0.7779` n `13`; crypto_alt avg `0.2907` n `235`; crypto_major avg `0.8065` n `8`; equity avg `-0.3559` n `151`; fx avg `0.1776` n `6`; index avg `-0.1405` n `26`; metal avg `-0.3414` n `20`; unknown avg `-0.037` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1568`, n `667`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0922`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.092`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0853`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `667`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0808`, n `669`, weak_sample_signal
