# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T18:52:37.522771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0532` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4208` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3159` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8128` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.5725` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5154` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.7841` n `235`; crypto_major avg `-0.5764` n `8`; equity avg `0.0494` n `143`; fx avg `0.0018` n `6`; index avg `0.0064` n `26`; metal avg `-0.0001` n `20`; unknown avg `8.1971` n `984`
- 1h: commodity avg `0.0394` n `13`; crypto_alt avg `-2.5781` n `235`; crypto_major avg `-1.5318` n `8`; equity avg `-0.1076` n `143`; fx avg `-0.0055` n `6`; index avg `-0.0164` n `26`; metal avg `0.0407` n `20`; unknown avg `3.7249` n `982`
- 4h: commodity avg `0.4991` n `13`; crypto_alt avg `-3.8698` n `235`; crypto_major avg `-2.5541` n `8`; equity avg `-0.7413` n `143`; fx avg `-0.0122` n `6`; index avg `-0.1333` n `26`; metal avg `-0.2382` n `20`; unknown avg `3.479` n `976`
- 24h: commodity avg `-0.1886` n `13`; crypto_alt avg `-1.8666` n `235`; crypto_major avg `-1.1998` n `8`; equity avg `0.617` n `142`; fx avg `-0.1284` n `6`; index avg `0.2678` n `26`; metal avg `-0.2447` n `20`; unknown avg `99.636` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
