# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T10:37:28.654627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5405` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.0294` n `239`; crypto_major avg `-0.1067` n `8`; equity avg `-0.0237` n `162`; fx avg `-0.0007` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0344` n `1263`
- 1h: commodity avg `-0.0287` n `13`; crypto_alt avg `0.3681` n `239`; crypto_major avg `0.3157` n `8`; equity avg `-0.0422` n `162`; fx avg `-0.0006` n `6`; index avg `-0.003` n `27`; metal avg `0.0076` n `20`; unknown avg `0.0105` n `1261`
- 4h: commodity avg `-0.0615` n `13`; crypto_alt avg `0.9074` n `239`; crypto_major avg `1.7144` n `8`; equity avg `0.3637` n `162`; fx avg `-0.0173` n `6`; index avg `0.0394` n `27`; metal avg `0.1739` n `20`; unknown avg `0.7444` n `1245`
- 24h: commodity avg `0.0106` n `13`; crypto_alt avg `-3.7768` n `239`; crypto_major avg `-3.2429` n `8`; equity avg `-0.7444` n `162`; fx avg `0.0315` n `6`; index avg `-0.061` n `27`; metal avg `-0.3425` n `20`; unknown avg `-0.122` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
