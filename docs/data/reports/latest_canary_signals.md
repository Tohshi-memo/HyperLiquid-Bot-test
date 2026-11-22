# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T05:52:25.080081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.7333` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7105` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `0.3518` n `239`; crypto_major avg `0.3065` n `8`; equity avg `0.1295` n `166`; fx avg `0.0095` n `6`; index avg `0.0098` n `27`; metal avg `0.0341` n `20`; unknown avg `158.3982` n `1263`
- 1h: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.0339` n `239`; crypto_major avg `-0.4003` n `8`; equity avg `-0.0052` n `166`; fx avg `0.0112` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0031` n `20`; unknown avg `168.7405` n `1261`
- 4h: commodity avg `-0.0927` n `13`; crypto_alt avg `-1.0449` n `239`; crypto_major avg `-1.8331` n `8`; equity avg `-0.5638` n `166`; fx avg `0.0101` n `6`; index avg `-0.0998` n `27`; metal avg `-0.1226` n `20`; unknown avg `23.7175` n `1255`
- 24h: commodity avg `-0.0094` n `13`; crypto_alt avg `3.2142` n `239`; crypto_major avg `4.7503` n `8`; equity avg `1.4172` n `166`; fx avg `-0.0117` n `6`; index avg `0.1663` n `27`; metal avg `0.1653` n `20`; unknown avg `604.3063` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
