# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T04:22:21.133192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8207` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2252` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0759` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.7683` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5852` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.9282` n `228`; crypto_major avg `-0.7172` n `8`; equity avg `-0.2977` n `74`; fx avg `0.0077` n `6`; index avg `-0.1057` n `23`; metal avg `-0.0646` n `18`; unknown avg `-0.4311` n `425`
- 1h: commodity avg `-0.1889` n `12`; crypto_alt avg `-2.2255` n `228`; crypto_major avg `-1.6718` n `8`; equity avg `-0.0866` n `74`; fx avg `0.0317` n `6`; index avg `0.0965` n `23`; metal avg `-0.1895` n `18`; unknown avg `-0.9084` n `425`
- 4h: commodity avg `0.04` n `12`; crypto_alt avg `-3.902` n `228`; crypto_major avg `-2.7807` n `8`; equity avg `-1.8165` n `74`; fx avg `-0.0135` n `6`; index avg `-0.7048` n `23`; metal avg `-0.5555` n `18`; unknown avg `0.3977` n `425`
- 24h: commodity avg `-1.2688` n `12`; crypto_alt avg `-7.7517` n `228`; crypto_major avg `-6.282` n `8`; equity avg `-6.8038` n `74`; fx avg `-0.2016` n `6`; index avg `-3.9329` n `23`; metal avg `-4.2561` n `18`; unknown avg `-1.1467` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
