# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T05:52:34.038572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3719` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.3059` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.2221` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.0896` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.1189` n `239`; crypto_major avg `-0.1752` n `8`; equity avg `0.0813` n `166`; fx avg `-0.003` n `6`; index avg `0.0098` n `27`; metal avg `0.0128` n `20`; unknown avg `-0.1909` n `1262`
- 1h: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.7638` n `239`; crypto_major avg `-0.8188` n `8`; equity avg `-0.0123` n `166`; fx avg `-0.0058` n `6`; index avg `0.0097` n `27`; metal avg `-0.032` n `20`; unknown avg `357.2281` n `1258`
- 4h: commodity avg `-0.0253` n `13`; crypto_alt avg `-3.5151` n `239`; crypto_major avg `-4.3972` n `8`; equity avg `-1.3076` n `166`; fx avg `-0.0378` n `6`; index avg `-0.0913` n `27`; metal avg `-0.1751` n `20`; unknown avg `0.7799` n `1242`
- 24h: commodity avg `0.3564` n `13`; crypto_alt avg `-7.3991` n `239`; crypto_major avg `-9.4402` n `8`; equity avg `-5.6945` n `166`; fx avg `-0.0636` n `6`; index avg `-0.5813` n `27`; metal avg `-0.246` n `20`; unknown avg `12.7796` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
