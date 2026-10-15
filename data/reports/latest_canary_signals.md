# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T18:07:35.310099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5943` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5132` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0401` n `13`; crypto_alt avg `-0.0859` n `236`; crypto_major avg `-0.2` n `8`; equity avg `-0.2414` n `151`; fx avg `0.0053` n `6`; index avg `-0.0525` n `26`; metal avg `0.0067` n `20`; unknown avg `0.2629` n `1134`
- 1h: commodity avg `0.1141` n `13`; crypto_alt avg `0.4192` n `236`; crypto_major avg `0.2731` n `8`; equity avg `0.1784` n `151`; fx avg `0.0167` n `6`; index avg `0.0119` n `26`; metal avg `0.0926` n `20`; unknown avg `0.0504` n `1134`
- 4h: commodity avg `0.1828` n `13`; crypto_alt avg `4.0312` n `236`; crypto_major avg `2.696` n `8`; equity avg `2.051` n `151`; fx avg `-0.0123` n `6`; index avg `0.2068` n `26`; metal avg `0.1017` n `20`; unknown avg `2.613` n `1116`
- 24h: commodity avg `-0.0766` n `13`; crypto_alt avg `0.9432` n `236`; crypto_major avg `0.7158` n `8`; equity avg `-1.2` n `151`; fx avg `0.2185` n `6`; index avg `-0.2105` n `26`; metal avg `0.4546` n `20`; unknown avg `0.5858` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0849`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0828`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0594`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0541`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
