# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T18:52:31.073116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8984` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7877` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6625` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0408` n `13`; crypto_alt avg `-0.3612` n `236`; crypto_major avg `-0.4912` n `8`; equity avg `-0.2675` n `151`; fx avg `0.0045` n `6`; index avg `-0.0307` n `26`; metal avg `-0.0167` n `20`; unknown avg `64.6135` n `1177`
- 1h: commodity avg `0.1183` n `13`; crypto_alt avg `-0.6186` n `236`; crypto_major avg `-0.4831` n `8`; equity avg `-0.6387` n `151`; fx avg `-0.001` n `6`; index avg `-0.1064` n `26`; metal avg `-0.0604` n `20`; unknown avg `235.1891` n `1175`
- 4h: commodity avg `0.7749` n `13`; crypto_alt avg `-2.7973` n `236`; crypto_major avg `-2.1235` n `8`; equity avg `-2.2676` n `151`; fx avg `-0.0392` n `6`; index avg `-0.461` n `26`; metal avg `-0.3358` n `20`; unknown avg `3.5566` n `1134`
- 24h: commodity avg `0.3166` n `13`; crypto_alt avg `-2.3638` n `236`; crypto_major avg `-2.1666` n `8`; equity avg `-2.9021` n `151`; fx avg `0.0024` n `6`; index avg `-0.5254` n `26`; metal avg `-0.0896` n `20`; unknown avg `0.0859` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1565`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0741`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
