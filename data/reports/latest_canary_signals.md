# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T15:57:19.116518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9415` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.7053` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.112` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.2437` n `228`; crypto_major avg `0.2698` n `8`; equity avg `0.0096` n `86`; fx avg `0.0128` n `6`; index avg `0.0141` n `23`; metal avg `0.1514` n `20`; unknown avg `-0.2421` n `765`
- 1h: commodity avg `0.352` n `12`; crypto_alt avg `-0.2403` n `228`; crypto_major avg `-0.1341` n `8`; equity avg `-0.3683` n `86`; fx avg `0.054` n `6`; index avg `-0.0514` n `23`; metal avg `0.2886` n `20`; unknown avg `-0.487` n `765`
- 4h: commodity avg `0.3545` n `12`; crypto_alt avg `-1.9007` n `228`; crypto_major avg `-2.3508` n `8`; equity avg `-2.4323` n `86`; fx avg `0.0861` n `6`; index avg `-0.2388` n `23`; metal avg `0.5907` n `20`; unknown avg `0.8361` n `765`
- 24h: commodity avg `0.3692` n `12`; crypto_alt avg `-1.4099` n `228`; crypto_major avg `-1.285` n `8`; equity avg `-1.0837` n `86`; fx avg `0.0789` n `6`; index avg `0.2657` n `23`; metal avg `0.2905` n `20`; unknown avg `0.0655` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
