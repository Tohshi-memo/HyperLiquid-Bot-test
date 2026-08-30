# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T22:49:59.391000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2519` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8814` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8477` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5398` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.0855` n `231`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0289` n `128`; fx avg `0.0002` n `6`; index avg `-0.0101` n `26`; metal avg `0.0337` n `20`; unknown avg `-0.1436` n `793`
- 1h: commodity avg `-0.208` n `12`; crypto_alt avg `-0.6106` n `231`; crypto_major avg `-0.6146` n `8`; equity avg `-0.2714` n `128`; fx avg `-0.0064` n `6`; index avg `-0.0822` n `26`; metal avg `-0.0441` n `20`; unknown avg `1.0438` n `791`
- 4h: commodity avg `0.2411` n `12`; crypto_alt avg `-1.6852` n `231`; crypto_major avg `-2.0108` n `8`; equity avg `-0.471` n `128`; fx avg `-0.0073` n `6`; index avg `-0.1294` n `26`; metal avg `-0.1631` n `20`; unknown avg `1.0698` n `791`
- 24h: commodity avg `0.2932` n `12`; crypto_alt avg `0.2756` n `231`; crypto_major avg `-0.7989` n `8`; equity avg `-0.2771` n `128`; fx avg `0.0332` n `6`; index avg `-0.0976` n `26`; metal avg `-0.0569` n `20`; unknown avg `-0.1089` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
