# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T00:52:24.878271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8976` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7704` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0412` n `12`; crypto_alt avg `0.0021` n `231`; crypto_major avg `-0.1309` n `8`; equity avg `-0.0729` n `128`; fx avg `-0.0186` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0363` n `20`; unknown avg `-0.0523` n `793`
- 1h: commodity avg `-0.0974` n `12`; crypto_alt avg `1.1315` n `231`; crypto_major avg `0.5555` n `8`; equity avg `0.1671` n `128`; fx avg `0.0039` n `6`; index avg `0.0394` n `26`; metal avg `0.1157` n `20`; unknown avg `0.3508` n `791`
- 4h: commodity avg `-0.3632` n `12`; crypto_alt avg `-1.7651` n `231`; crypto_major avg `-2.005` n `8`; equity avg `-0.9078` n `128`; fx avg `0.0205` n `6`; index avg `-0.2346` n `26`; metal avg `-0.1074` n `20`; unknown avg `3.3251` n `789`
- 24h: commodity avg `0.1273` n `12`; crypto_alt avg `-0.625` n `231`; crypto_major avg `-1.7865` n `8`; equity avg `-0.8646` n `128`; fx avg `0.0283` n `6`; index avg `-0.2332` n `26`; metal avg `-0.0524` n `20`; unknown avg `-0.3987` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
