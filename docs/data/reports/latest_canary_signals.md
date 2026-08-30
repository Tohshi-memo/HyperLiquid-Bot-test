# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T23:52:25.524878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8008` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6423` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5986` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7573` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2971` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.4` n `231`; crypto_major avg `-0.1377` n `8`; equity avg `-0.1948` n `128`; fx avg `-0.0005` n `6`; index avg `-0.0839` n `26`; metal avg `-0.0655` n `20`; unknown avg `0.1729` n `793`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `-2.0507` n `231`; crypto_major avg `-1.4796` n `8`; equity avg `-0.7561` n `128`; fx avg `0.0094` n `6`; index avg `-0.1825` n `26`; metal avg `-0.102` n `20`; unknown avg `1.1477` n `791`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `-3.159` n `231`; crypto_major avg `-2.8992` n `8`; equity avg `-1.1419` n `128`; fx avg `0.0135` n `6`; index avg `-0.3006` n `26`; metal avg `-0.2569` n `20`; unknown avg `1.8668` n `789`
- 24h: commodity avg `0.223` n `12`; crypto_alt avg `-1.8133` n `231`; crypto_major avg `-2.3748` n `8`; equity avg `-1.0399` n `128`; fx avg `0.0324` n `6`; index avg `-0.2535` n `26`; metal avg `-0.1761` n `20`; unknown avg `-0.4804` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
