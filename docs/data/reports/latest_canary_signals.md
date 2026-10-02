# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T18:22:28.853644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9663` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9834` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7458` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `-0.705` n `235`; crypto_major avg `-0.4111` n `8`; equity avg `-0.0425` n `143`; fx avg `0.0023` n `6`; index avg `-0.0131` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.5919` n `984`
- 1h: commodity avg `0.146` n `13`; crypto_alt avg `-1.3049` n `235`; crypto_major avg `-0.5441` n `8`; equity avg `0.0042` n `143`; fx avg `-0.0063` n `6`; index avg `-0.013` n `26`; metal avg `0.0137` n `20`; unknown avg `2.6184` n `982`
- 4h: commodity avg `0.8242` n `13`; crypto_alt avg `-2.7745` n `235`; crypto_major avg `-2.1421` n `8`; equity avg `-0.8899` n `143`; fx avg `0.0146` n `6`; index avg `-0.1587` n `26`; metal avg `-0.3963` n `20`; unknown avg `2.782` n `952`
- 24h: commodity avg `-0.0837` n `13`; crypto_alt avg `-0.3683` n `235`; crypto_major avg `-0.2394` n `8`; equity avg `0.811` n `142`; fx avg `-0.0997` n `6`; index avg `0.3216` n `26`; metal avg `-0.2759` n `20`; unknown avg `100.1367` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
