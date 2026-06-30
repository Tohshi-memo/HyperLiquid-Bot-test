# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T12:22:22.673018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1065` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0976` n `12`; crypto_alt avg `-0.2929` n `228`; crypto_major avg `-0.3014` n `8`; equity avg `-0.1862` n `88`; fx avg `-0.0022` n `6`; index avg `0.0042` n `23`; metal avg `-0.1213` n `20`; unknown avg `0.1962` n `765`
- 1h: commodity avg `0.2771` n `12`; crypto_alt avg `-0.9754` n `228`; crypto_major avg `-0.9168` n `8`; equity avg `-0.3661` n `88`; fx avg `-0.0054` n `6`; index avg `-0.0008` n `23`; metal avg `-0.172` n `20`; unknown avg `0.1187` n `765`
- 4h: commodity avg `0.3582` n `12`; crypto_alt avg `-1.5034` n `228`; crypto_major avg `-1.099` n `8`; equity avg `-0.2848` n `88`; fx avg `-0.033` n `6`; index avg `0.0075` n `23`; metal avg `0.0053` n `20`; unknown avg `-0.0056` n `765`
- 24h: commodity avg `0.4036` n `12`; crypto_alt avg `-2.8446` n `228`; crypto_major avg `-1.7285` n `8`; equity avg `0.8491` n `88`; fx avg `0.1049` n `6`; index avg `0.1545` n `23`; metal avg `0.0932` n `20`; unknown avg `8.8954` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
