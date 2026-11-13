# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T05:52:25.547871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5885` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4139` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3603` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `0.4656` n `239`; crypto_major avg `0.341` n `8`; equity avg `-0.0921` n `162`; fx avg `-0.0117` n `6`; index avg `-0.0022` n `27`; metal avg `-0.1701` n `20`; unknown avg `6.8017` n `1260`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.5826` n `239`; crypto_major avg `0.3573` n `8`; equity avg `-0.595` n `162`; fx avg `-0.0027` n `6`; index avg `-0.0613` n `27`; metal avg `-0.1777` n `20`; unknown avg `7.0452` n `1254`
- 4h: commodity avg `-0.0361` n `13`; crypto_alt avg `-2.15` n `239`; crypto_major avg `-2.6246` n `8`; equity avg `-1.9811` n `162`; fx avg `0.0177` n `6`; index avg `-0.2107` n `27`; metal avg `-0.2643` n `20`; unknown avg `1.4418` n `1242`
- 24h: commodity avg `0.8217` n `13`; crypto_alt avg `-2.3907` n `239`; crypto_major avg `-3.9699` n `8`; equity avg `-1.0269` n `162`; fx avg `0.0041` n `6`; index avg `0.0101` n `27`; metal avg `-0.6072` n `20`; unknown avg `99.7291` n `1121`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
