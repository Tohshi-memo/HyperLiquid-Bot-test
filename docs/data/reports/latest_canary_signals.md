# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T17:22:31.083733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6659` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0684` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6722` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0493` n `13`; crypto_alt avg `-0.695` n `236`; crypto_major avg `-0.5771` n `8`; equity avg `-0.2648` n `151`; fx avg `0.0007` n `6`; index avg `-0.0761` n `26`; metal avg `0.0074` n `20`; unknown avg `0.2781` n `1177`
- 1h: commodity avg `0.1793` n `13`; crypto_alt avg `-1.7007` n `236`; crypto_major avg `-1.1827` n `8`; equity avg `-0.9012` n `151`; fx avg `-0.0017` n `6`; index avg `-0.2235` n `26`; metal avg `-0.0919` n `20`; unknown avg `-0.2435` n `1172`
- 4h: commodity avg `0.4852` n `13`; crypto_alt avg `-2.8429` n `236`; crypto_major avg `-2.1807` n `8`; equity avg `-2.8517` n `151`; fx avg `0.0015` n `6`; index avg `-0.5085` n `26`; metal avg `-0.1123` n `20`; unknown avg `1.0877` n `996`
- 24h: commodity avg `0.147` n `13`; crypto_alt avg `-2.6677` n `236`; crypto_major avg `-2.5947` n `8`; equity avg `-2.3256` n `151`; fx avg `0.0122` n `6`; index avg `-0.4906` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.4253` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1348`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0868`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
