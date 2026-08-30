# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T22:37:29.321451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4001` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0149` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9303` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6825` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.2551` n `231`; crypto_major avg `-0.1916` n `8`; equity avg `-0.0992` n `128`; fx avg `0.0087` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.0632` n `793`
- 1h: commodity avg `-0.205` n `12`; crypto_alt avg `-0.6399` n `231`; crypto_major avg `-0.6956` n `8`; equity avg `-0.2348` n `128`; fx avg `-0.0002` n `6`; index avg `-0.0845` n `26`; metal avg `-0.0999` n `20`; unknown avg `3.1349` n `791`
- 4h: commodity avg `0.2687` n `12`; crypto_alt avg `-1.5462` n `231`; crypto_major avg `-2.1314` n `8`; equity avg `-0.4489` n `128`; fx avg `-0.0049` n `6`; index avg `-0.1165` n `26`; metal avg `-0.2011` n `20`; unknown avg `1.4862` n `791`
- 24h: commodity avg `0.3382` n `12`; crypto_alt avg `0.4284` n `231`; crypto_major avg `-0.7237` n `8`; equity avg `-0.2615` n `128`; fx avg `0.0366` n `6`; index avg `-0.0643` n `26`; metal avg `-0.0889` n `20`; unknown avg `-0.0569` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
