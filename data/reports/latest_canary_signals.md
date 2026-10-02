# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T16:37:28.378579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1644` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8334` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5971` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0728` n `13`; crypto_alt avg `-0.4568` n `235`; crypto_major avg `-0.1845` n `8`; equity avg `-0.0931` n `143`; fx avg `0.0009` n `6`; index avg `-0.0122` n `26`; metal avg `0.0001` n `20`; unknown avg `0.1062` n `984`
- 1h: commodity avg `0.136` n `13`; crypto_alt avg `-0.1975` n `235`; crypto_major avg `-0.0608` n `8`; equity avg `0.0458` n `143`; fx avg `-0.0038` n `6`; index avg `0.0121` n `26`; metal avg `-0.0263` n `20`; unknown avg `-0.1483` n `976`
- 4h: commodity avg `0.2667` n `13`; crypto_alt avg `-0.9298` n `235`; crypto_major avg `-1.8977` n `8`; equity avg `-0.3006` n `142`; fx avg `0.0856` n `6`; index avg `-0.0643` n `26`; metal avg `-0.6718` n `20`; unknown avg `0.8478` n `934`
- 24h: commodity avg `-0.2412` n `13`; crypto_alt avg `2.1437` n `235`; crypto_major avg `1.1118` n `8`; equity avg `1.564` n `142`; fx avg `-0.139` n `6`; index avg `0.4418` n `26`; metal avg `-0.2216` n `20`; unknown avg `101.0611` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
