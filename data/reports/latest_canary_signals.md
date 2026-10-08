# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T21:52:39.492756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5435` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.381` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6598` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0467` n `13`; crypto_alt avg `0.0401` n `235`; crypto_major avg `-0.0282` n `8`; equity avg `0.009` n `150`; fx avg `0.0026` n `6`; index avg `0.0007` n `26`; metal avg `-0.0029` n `20`; unknown avg `5.5631` n `1077`
- 1h: commodity avg `-0.0096` n `13`; crypto_alt avg `-0.1151` n `235`; crypto_major avg `0.0503` n `8`; equity avg `0.0338` n `150`; fx avg `0.0129` n `6`; index avg `0.0023` n `26`; metal avg `0.0087` n `20`; unknown avg `4.3222` n `1067`
- 4h: commodity avg `-0.1085` n `13`; crypto_alt avg `3.0898` n `235`; crypto_major avg `2.435` n `8`; equity avg `0.7752` n `150`; fx avg `0.0358` n `6`; index avg `0.1288` n `26`; metal avg `0.054` n `20`; unknown avg `6.6567` n `1007`
- 24h: commodity avg `0.6329` n `13`; crypto_alt avg `-2.2371` n `235`; crypto_major avg `-3.0455` n `8`; equity avg `-2.723` n `150`; fx avg `0.0576` n `6`; index avg `-0.3497` n `26`; metal avg `-0.0231` n `20`; unknown avg `6.1924` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
