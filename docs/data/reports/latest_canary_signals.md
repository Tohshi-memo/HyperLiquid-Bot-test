# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T17:22:24.874909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6139` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5802` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5672` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.0174` n `239`; crypto_major avg `0.0025` n `8`; equity avg `-0.0581` n `162`; fx avg `0.007` n `6`; index avg `-0.0198` n `27`; metal avg `-0.0172` n `20`; unknown avg `18.8588` n `1263`
- 1h: commodity avg `0.0011` n `13`; crypto_alt avg `-0.1754` n `239`; crypto_major avg `0.1635` n `8`; equity avg `0.1283` n `162`; fx avg `0.0046` n `6`; index avg `-0.022` n `27`; metal avg `-0.0059` n `20`; unknown avg `179.6671` n `1263`
- 4h: commodity avg `-0.0806` n `13`; crypto_alt avg `-1.5361` n `239`; crypto_major avg `-1.6145` n `8`; equity avg `-0.0473` n `162`; fx avg `0.01` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0343` n `20`; unknown avg `18.1637` n `1256`
- 24h: commodity avg `0.0429` n `13`; crypto_alt avg `-1.2779` n `239`; crypto_major avg `-0.2953` n `8`; equity avg `0.2009` n `162`; fx avg `-0.0085` n `6`; index avg `0.0251` n `27`; metal avg `-0.1733` n `20`; unknown avg `9.0407` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
